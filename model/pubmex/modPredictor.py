from predictor import *

class ModPredictor(Predictor):
    
    def __init__(self, cfg):
        super().__init__(cfg)

    def __call__(self, original_image):

        # Apply pre-processing to image.
        if self.input_format == "RGB":
            original_image = original_image[:, :, ::-1]
        height, width = original_image.shape[:2]
        image = self.transform_gen.get_transform(original_image).apply_image(original_image)
        image = torch.as_tensor(image.astype("float32").transpose(2, 0, 1))
        inputs = {"image": image, "height": height, "width": width}

        with torch.no_grad():
           
            images = self.model.preprocess_image([inputs])
            features = self.model.backbone(images.tensor)                       # Backbone
            proposals, _ = self.model.proposal_generator(images, features)      # RPN

            features_ = [features[f] for f in self.model.roi_heads.box_in_features]
            box_features = self.model.roi_heads.box_pooler(features_, [x.proposal_boxes for x in proposals])
            box_features = self.model.roi_heads.box_head(box_features)  # features of all 1k candidates
            predictions = self.model.roi_heads.box_predictor(box_features)
            pred_instances, pred_inds = self.model.roi_heads.box_predictor.inference(predictions, proposals)
            score = self.model.roi_heads.box_predictor.predict_probs(predictions, proposals)
            output = self.model([inputs])[0]

            instance_bounding_box = output['instances']._fields['pred_boxes'].tensor
            instance_score = score[0][pred_inds]

            result = list(zip(instance_bounding_box, instance_score))

            return result
