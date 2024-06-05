import pytest
from survey import AnonymousSurvey  # import class to test

@pytest.fixture # decorator/fixture from pytest module applied to the following language_survey generator function
def language_survey():  # new language_survey generator function (of AnonymousSurvey class instances/objects) available to all test functions 
        question = "What language did you first learn to speak?"
        language_survey = AnonymousSurvey(question) #initialize language_survey as an instance of the AnonymousSurvey class 
        return language_survey

def test_store_single_response(language_survey):   
    # test function that tests that the function properly stores a single response
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):    
    # test function that tests that the function properly stores multiple responses
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
        assert response in language_survey.responses
