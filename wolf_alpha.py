import joy
import wolframalpha
def math_solver(ask):
    qsn = ask
    appid = "HT44W6-36W9HQUE6X" # optional :8REQUG-YQ7JGY96T8
    # we have to create an instances of w-alpha client class
    client = wolframalpha.Client(appid)
    output = client.query(qsn)
    final_answer = next(output.results).text
    print("Result:", final_answer)
    joy.speak("Your calculation result is, "+final_answer)
    return


def search(qsn):
    question = qsn
    app_id = "HT44W6-36W9HQUE6X" # optional :8REQUG-YQ7JGY96T8
    client = wolframalpha.Client(app_id)
    output = client.query(question)
    final_output = next(output.results).text
    print("Result:", final_output)
    joy.speak("It is "+final_output)
    return


def weather(qsn):
    w_query = qsn
    app_id = "HT44W6-36W9HQUE6X"
    client = wolframalpha.Client(app_id)
    res = client.query(w_query)
    final_res = next(res.results).text
    print("weather update is: ", final_res)
    joy.speak("Weather update is, "+final_res)
    return