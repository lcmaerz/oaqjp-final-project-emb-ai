from EmotionDetection import emotion_detector

def test_joy():
    result = emotion_detector("I am glad this happened")
    assert result['dominant_emotion'] == 'joy'
    print("PASS: joy")

def test_anger():
    result = emotion_detector("I am really mad about this")
    assert result['dominant_emotion'] == 'anger'
    print("PASS: anger")


def test_disgust():
    result = emotion_detector("I feel disgusted just hearing about this")
    assert result['dominant_emotion'] == 'disgust'
    print("PASS: disgust")


def test_sadness():
    result = emotion_detector("I am so sad about this")
    assert result['dominant_emotion'] == 'sadness'
    print("PASS: sadness")

def test_fear():
    result = emotion_detector("I am really afraid that this will happen")
    assert result['dominant_emotion'] == 'fear'
    print("PASS: fear")

test_joy()
test_anger()
test_disgust()
test_sadness()
test_fear()
