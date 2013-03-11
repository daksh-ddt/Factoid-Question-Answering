# -*- coding: utf-8 *-*
'''
Predict a coarse and fine answer type for a question.

'''
import os
try:
    import cPickle as pickle
except:
    import pickle  # lint:ok


class Answer_classifier:

    def __init__(self):
        self.base_path = os.path.dirname(__file__)
        self.coarse_target_names = [
            'ABBR', 'DESC', 'ENTY', 'HUM', 'LOC', 'NUM', 'UTIL']
        self.fine_target_names = {
            'ABBR': ['abb', 'exp'],
            'DESC': ['def', 'desc', 'manner', 'reason'],
            'ENTY': ['animal', 'body', 'color', 'cremat', 'currency', 'dismed',
                    'event', 'food', 'instru', 'lang', 'letter', 'other',
                    'plant', 'product', 'religion', 'sport', 'substance',
                    'symbol', 'techmeth',
                    'termeq', 'veh', 'word'],
            'HUM': ['desc', 'gr', 'ind', 'title'],
            'LOC': ['address', 'airport', 'artificial', 'biome', 'bodwat',
                    'celestial_body', 'city', 'constellation', 'continent',
                    'coordinate', 'country', 'county', 'desert', 'direction',
                    'island', 'lake', 'mountain', 'ocean', 'other', 'park',
                    'planet', 'region', 'restaurant', 'retail', 'river',
                    'school', 'sea', 'source', 'state', 'street', 'vague',
                    'web_address'],
            'NUM': ['code', 'count', 'date', 'dist', 'money', 'ord', 'other',
                    'perc', 'period', 'speed', 'temp', 'volsize', 'weight'],
            'UTIL': ['more', 'wrong'],
        }

        # Load the coarse and fine classifiers
        model_pickle = open(
            os.path.join(self.base_path, 'training_models/coarse.p'))
        self.coarse_classifier = pickle.load(model_pickle)
        model_pickle.close()

        model_pickle = open(
            os.path.join(self.base_path, 'training_models/fine_abbr.p'))
        fine_abbr_classifier = pickle.load(model_pickle)
        model_pickle.close()

        model_pickle = open(
            os.path.join(self.base_path, 'training_models/fine_desc.p'))
        fine_desc_classifier = pickle.load(model_pickle)
        model_pickle.close()

        model_pickle = open(
            os.path.join(self.base_path, 'training_models/fine_enty.p'))
        fine_enty_classifier = pickle.load(model_pickle)
        model_pickle.close()

        model_pickle = open(
            os.path.join(self.base_path, 'training_models/fine_hum.p'))
        fine_hum_classifier = pickle.load(model_pickle)
        model_pickle.close()

        model_pickle = open(
            os.path.join(self.base_path, 'training_models/fine_loc.p'))
        fine_loc_classifier = pickle.load(model_pickle)
        model_pickle.close()

        model_pickle = open(
            os.path.join(self.base_path, 'training_models/fine_num.p'))
        fine_num_classifier = pickle.load(model_pickle)
        model_pickle.close()

        model_pickle = open(
            os.path.join(self.base_path, 'training_models/fine_util.p'))
        fine_util_classifier = pickle.load(model_pickle)
        model_pickle.close()

        self.fine_classifiers = {
            'ABBR': fine_abbr_classifier,
            'DESC': fine_desc_classifier,
            'ENTY': fine_enty_classifier,
            'HUM': fine_hum_classifier,
            'LOC': fine_loc_classifier,
            'NUM': fine_num_classifier,
            'UTIL': fine_util_classifier,
        }

    def predict_answer_type(self, question):
        # Predict a coarse type
        predicted_coarse = self.coarse_target_names[
            self.coarse_classifier.predict(question)]
        print 'Predicting coarse type: %s for question: %s' % (predicted_coarse,
            question)

        # Load the appropriate fine classifier
        fine_classifier = self.fine_classifiers[predicted_coarse]

        # Predict a fine type
        predicted_fine = self.fine_target_names[
            predicted_coarse][fine_classifier.predict(question)]
        print 'Predicting fine type: %s for question: %s' % (predicted_fine,
            question)
        return predicted_coarse.lower(), predicted_fine


if __name__ == '__main__':
    question = ['where is the largest mall in america?']
    answer_classifier = Answer_classifier()
    predicted_coarse, predicted_fine = answer_classifier.predict_answer_type(
        question)
    print predicted_coarse, predicted_fine
