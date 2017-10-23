import unittest
import numpy
from assignment2_logistic import *

class module_test(unittest.TestCase):
    def test_sigmoid(self):
        '''
        self.assertEqual(sigmoid([0,2]).shape,(1,2))
        print(sigmoid(np.array([0,2])))
        '''
        pass

    def test_initialize_with_zeros(self):
        '''
        dim = 2
        w, b = initialize_with_zeros(dim)
        self.assertEqual(w.shape, (2,1))
        print(str(w))
        print(str(b))
        '''
        pass

    def test_propagate(self):
        pass
        '''
        w, b, X, Y = np.array([[1],[2]]), 2, np.array([[1,2],[3,4]]), np.array([1,0])
        grads, cost = propagate(w, b, X, Y)
        print(str(grads["dw"]))
        print(str(grads["db"]))
        print(str(cost))
        '''
    def test_optimize(self):
        '''
        w, b, X, Y = np.array([[1],[2]]), 2, np.array([[1,2],[3,4]]), np.array([1,0])
        params, grads, costs = optimize(w, b, X, Y, num_iterations = 100, learning_rate = 0.009, print_cost = False)
        print("w = %s, b = %s, dw = %s, db = %s"%(str(params["w"]),str(params["b"]),str(grads["dw"]),str(grads["db"])))
        '''
        pass
    def test_predict(self):
        w, b, X, Y = np.array([[1],[2]]), 2, np.array([[1,2],[3,4]]), np.array([1,0])
        params, grads, costs = optimize(w, b, X, Y, num_iterations = 100, learning_rate = 0.009, print_cost = False)
        print(str(predict(w, b, X)))

if __name__ == '__main__':
    unittest.main()