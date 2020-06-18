import joy
import wolframalpha
def math_solver(ask):
    qsn = ask
    appid = "your app-id" 
    # we have to create an instances of w-alpha client class
    client = wolframalpha.Client(appid)
    output = client.query(qsn)
    final_answer = next(output.results).text
    print("Result:", final_answer)
    joy.speak("Your calculation result is, "+final_answer)
    return


def search(qsn):
    question = qsn
    app_id =  "your app-id"
    output = client.query(question)
    final_output = next(output.results).text
    print("Result:", final_output)
    joy.speak("It is "+final_output)
    return


def weather(qsn):
    w_query = qsn
    app_id =  "your app-id"
    client = wolframalpha.Client(app_id)
    res = client.query(w_query)
    final_res = next(res.results).text
    print("weather update is: ", final_res)
    joy.speak("Weather update is, "+final_res)
    return
