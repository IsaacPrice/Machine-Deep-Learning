import numpy as np

def gradent_descent(x,y):
    m_curr = b_curr = 0
    iterations = 1000000 # This is how many steps there are to get to the point
    n = len(x)
    learning_rate = 0.0002 # This is how large the steps are to get to the total

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in y-y_predicted])

        # If the cost is under the set amount 1e-20, then it will quit
        if cost < 1e-20:
            break

        m_derivitative = -(2 / n) * sum(x * (y - y_predicted))
        b_derivitative = -(2 / n) * sum(y - y_predicted)
        m_curr = m_curr - learning_rate * m_derivitative
        b_curr = b_curr - learning_rate * b_derivitative
        print("m {}, b {}, iteration {} cost {}".format(m_curr,b_curr,i + 1,cost))


x = np.array([92, 56, 88, 70, 80, 49, 65, 35, 66, 67])
y = np.array([98, 68, 81, 80, 83, 52, 66, 30, 68, 73])

gradent_descent(x,y)