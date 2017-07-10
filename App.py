import numpy

def step_gradient(m,b,points,learning_rate):
    b_gr=0
    m_gr=0
    N = len(points)
    for i in range(len(points)):
            x = points[i,0]
            y = points[i,1]
            b_gr+= -(2/N)*(y-((m*x)+b))
            m_gr+= -(2/N)*x*(y-((m*x)+b))
    B_new = b -(learning_rate * b_gr)
    M_new = m -(learning_rate * m_gr)
    return[B_new,M_new]

def gradient_descent(points,learning_rate,number_of_iterations):
    b = 0
    m = 0
    for i in range(number_of_iterations):
        b,m=step_gradient(m,b,numpy.array(points),learning_rate)
    return[b,m]


def run():
    points = numpy.genfromtxt("#insert here the full path of a .csv data table ", delimiter=",")
    learning_rate = 0.0001
    number_of_iterations=1000
    b,m=gradient_descent(points,learning_rate,number_of_iterations)
    print('the b and m values for the best fitting y=mx+b line are b = {0}, m = {1}'.format(b,m))

if __name__ == '__main__':
    
    run()
