from django.shortcuts import render
import random
from time import *

# Test data
test_data = [
    "Psychiatry is the medical specialty devoted to the study, diagnosis, treatment, and prevention of mental disorders. These include various affective, behavioural, cognitive and perceptual abnormalities. Initial psychiatric assessment of a person typically begins with a case history and mental status examination. Psychological tests and physical examinations may be conducted, including on occasion the use of neuroimaging or other neurophysiological techniques. The combined treatment of psychiatric medication and psychotherapy has become the most common mode of psychiatric treatment in current practice.","In the centre of the room, clamped to an upright easel, stood the full-length portrait of a young man of extraordinary personal beauty, and in front of it, some little distance away, was sitting the artist himself, Basil Hallward, whose sudden disappearance some years ago caused, at the time, such public excitement and gave rise to so many strange conjectures. ('The Picture of Dorian Gray' by Oscar Wilde)","The role of analytical CRM systems is to analyze customer data collected through multiple sources, and present it so that business managers can make more informed decisions. Analytical CRM systems use techniques such as data mining, correlation, and pattern recognition to analyze the customer data. These analytics help improve customer service by finding small problems which can be solved, perhaps, by marketing to different parts of a consumer audience differently. For example, through the analysis of a customer base's buying behavior, a company might see that this customer base has not been buying a lot of products recently. After scanning through this data, the company might think to market to this subset of consumers differently, in order to best communicate how this company's products might benefit this group specifically.","The scientific method is a body of techniques for investigating phenomena, acquiring new knowledge, or correcting and integrating previous knowledge. To be termed scientific, a method of inquiry is commonly based on empirical or measurable evidence subject to specific principles of reasoning. The Oxford Dictionaries Online defines the scientific method as 'a method or procedure that has characterized natural science since the 17th century, consisting in systematic observation, measurement, and experiment, and the formulation, testing, and modification of hypotheses'. Experiments are a procedure designed to test hypotheses. Experiments are an important tool of the scientific method. The method is a continuous process that begins with observations about the natural world. People are naturally inquisitive, so they often come up with questions about things they see or hear, and they often develop ideas or hypotheses about why things are the way they are. The best hypotheses lead to predictions that can be tested in various ways. The strongest tests of hypotheses come from carefully controlled experiments that gather empirical data. Depending on how well additional tests match the predictions, the original hypothesis may require refinement, alteration, expansion or even rejection. If a particular hypothesis becomes very well supported, a general theory may be developed.","He examined a few subjects and very quickly recognized pox? Mixing home jobs with office tasks penalized my quiet Vera? Crazy viewers jumping frequently excite bored hockey idols. The quick onyx goblin jumps over the lazy dwarf! Jovial Debra Frantz swims quickly with grace and expertise?"


]

# Function to calculate errors
def errorfind(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

# Function to calculate typing speed
def speed_time(start, end, userinput):
    time_delay = end - start
    time_R = round(time_delay, 2)
    speed = len(userinput) / time_R
    return round(speed)

# Main view
def typing_test_view(request):
    if request.method == 'POST':
        original_text = request.POST.get('original_text')
        user_input = request.POST.get('user_input')
        start_time = float(request.POST.get('start_time'))
        end_time = time()

        speed = speed_time(start_time, end_time, user_input)
        errors = errorfind(original_text, user_input)

        return render(request, 'typing_result.html', {
            'original_text': original_text,
            'user_input': user_input,
            'speed': speed,
            'errors': errors,
        })
    else:
        test_text = random.choice(test_data)
        start_time = time()
        return render(request, 'typing_test.html', {
            'test_text': test_text,
            'start_time': start_time
        })
