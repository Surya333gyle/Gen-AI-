"""
Configuration file for the Employee Feedback Analysis System
"""

import os

# Flask Configuration
FLASK_HOST = os.getenv('FLASK_HOST', '0.0.0.0')
FLASK_PORT = int(os.getenv('FLASK_PORT', 5000))
FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'

# Model Configuration
MODEL_FILE = 'sentiment_model.pkl'
VECTORIZER_FILE = 'vectorizer.pkl'
DATASET_FILE = 'final_dataset.csv'
KEYWORDS_FILE = 'extracted_keywords.txt'

# Model Paths
MODEL_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILE)
VECTORIZER_PATH = os.path.join(MODEL_DIR, VECTORIZER_FILE)
DATASET_PATH = os.path.join(MODEL_DIR, DATASET_FILE)
KEYWORDS_PATH = os.path.join(MODEL_DIR, KEYWORDS_FILE)

# API Configuration
MAX_FEEDBACK_LENGTH = 10000  # Maximum characters for feedback text
MIN_FEEDBACK_LENGTH = 3      # Minimum characters for feedback text

# Model Metrics (update after training)
MODEL_METRICS = {
    'accuracy': 0.7210,
    'precision': 0.6604,
    'recall': 0.7210,
    'f1_score': 0.6485,
    'confusion_matrix': {
        'negative': {'negative': 714, 'neutral': 90, 'positive': 987},
        'neutral': {'negative': 226, 'neutral': 108, 'positive': 2131},
        'positive': {'negative': 155, 'neutral': 73, 'positive': 8643}
    }
}

# HR Keywords (fallback if extracted_keywords.txt not found)
DEFAULT_HR_KEYWORDS = [
    'salary', 'workload', 'culture', 'management', 'stress',
    'growth', 'team', 'support', 'bonus', 'environment'
]

# Emotion Keywords
EMOTION_KEYWORDS = {
    'joy': ['happy', 'great', 'amazing', 'wonderful', 'excellent', 'fantastic', 
            'love', 'enjoy', 'pleased', 'satisfied', 'delighted', 'excited', 'thrilled'],
    'stress': ['stress', 'stressful', 'pressure', 'overwhelming', 'anxious', 'worried', 
               'tension', 'burnout', 'exhausted', 'tired', 'drained'],
    'anger': ['angry', 'furious', 'mad', 'rage', 'hate', 'disgusted', 'annoyed', 
              'irritated', 'frustrated'],
    'frustration': ['frustrated', 'frustrating', 'disappointed', 'disappointing', 
                    'upset', 'unhappy', 'dissatisfied', 'let down'],
    'motivation': ['motivated', 'inspired', 'encouraged', 'energized', 'enthusiastic', 
                   'passionate', 'driven', 'ambitious', 'determined'],
    'neutral': ['okay', 'fine', 'average', 'normal', 'regular', 'standard', 'typical']
}

# Common HR Terms for Theme Extraction
COMMON_HR_TERMS = {
    'salary': ['salary', 'pay', 'compensation', 'wage', 'income'],
    'workload': ['workload', 'work load', 'pressure', 'demand'],
    'culture': ['culture', 'environment', 'atmosphere'],
    'management': ['management', 'manager', 'leadership', 'boss'],
    'stress': ['stress', 'stressful', 'pressure', 'overwhelming'],
    'growth': ['growth', 'development', 'career', 'advancement'],
    'team': ['team', 'colleague', 'coworker', 'peer'],
    'support': ['support', 'supportive', 'help'],
    'benefit': ['benefit', 'perk', 'bonus', 'reward'],
    'balance': ['balance', 'work life', 'work-life']
}

# Negative Indicators for Sentiment Override
NEGATIVE_INDICATORS = [
    'too high', 'too much', 'too many', 'pressure', 'stressful', 'stress',
    'overwhelming', 'difficult', 'hard', 'bad', 'very bad', 'terrible', 'awful',
    'not good', 'not great', 'disappointed', 'frustrated', 'worst',
    'no work life balance', 'work life balance bad', 'burnout',
    'some negatives', 'negative', 'aggressive', 'caustic', 'toxic',
    'problem', 'issue', 'concern', 'worry', 'complaint', 'dissatisfied',
    'unhappy', 'poor', 'weak', 'lack', 'missing', 'fail', 'failure',
    'stress is high', 'high stress'
]

STRONG_NEGATIVE_PHRASES = [
    'caustic work', 'caustic work environment', 'caustic work environments',
    'toxic environment', 'toxic environments',
    'aggressive personality', 'aggressive personalities',
    'difficult to have balance', 'difficult to have a balance', 'very difficult', 
    'some negatives', 'work life balance', 'no balance', 'poor management', 
    'bad culture', 'caustic', 'aggressive', 'toxic', 'make for caustic'
]

