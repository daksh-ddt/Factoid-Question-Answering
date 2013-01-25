# -*- coding: utf-8 *-*
'''


'''
try:
    import cPickle as pickle
except:
    import pickle  # lint:ok


class Answer_classifier:

    def __init__(self):
        self.coarse_target_names = [
            'ABBR', 'DESC', 'ENTY', 'HUM', 'LOC', 'NUM']
        self.fine_target_names = {
            'ABBR': ['abb', 'exp'],
            'DESC': ['def', 'desc', 'manner', 'reason'],
            'ENTY': ['animal', 'body', 'color', 'cremat', 'currency', 'dismed',
                    'event', 'food', 'instru', 'lang', 'letter', 'other',
                    'plant', 'product', 'religion', 'sport', 'substance',
                    'symbol', 'techmeth',
                    'termeq', 'veh', 'word'],
            'HUM': ['desc', 'gr', 'ind', 'title'],
            'LOC': ['city', 'country', 'mount', 'other', 'state'],
            'NUM': ['code', 'count', 'date', 'dist', 'money', 'ord', 'other',
                    'perc', 'period', 'speed', 'temp', 'volsize', 'weight']
        }

        model_pickle = open('training_model/coarse.p')
        self.coarse_classifier = pickle.load(model_pickle)
        model_pickle.close()

    def predict_answer_type(self, question):
        print self.coarse_classifier.predict(question)
        predicted_coarse = self.coarse_target_names[
            self.coarse_classifier.predict(question)]
        fine_model_pickle = open(
            'training_model/fine_%s.p' % predicted_coarse.lower())
        fine_classifier = pickle.load(fine_model_pickle)
        fine_model_pickle.close()
        predicted_fine = self.fine_target_names[
            predicted_coarse][fine_classifier.predict(question)]
        return predicted_coarse.lower(), predicted_fine


if __name__ == '__main__':
    question = ['Who was the first president of spain?']
    answer_classifier = Answer_classifier()
    predicted_coarse, predicted_fine = answer_classifier.predict_answer_type(
        question)
    print predicted_coarse, predicted_fine
