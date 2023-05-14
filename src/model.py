"""
This file implements the two dimensional linear regression model.
"""



class LinearRegression:
    "class for linear regression model."


    def __init__(self):
        self.x = 0
        self.y = 0
        self.m = 0
        self.b = 0
        
        #save  Sum of Squared Errors of each iteration:
        self.SSE = []


        #save derivative of SSE respect to slope m of each iteration:
        self.SSE_derivative_m = []

        #save derivative of SSE respect to intercept b of each iteration:
        self.SSE_derivative_b = []


    
    def fit(self, data_set, lr=0.001, max_iterations=10000):
        """
        A function to 'train the model' to the given train dataset.

        
        :param data_set: Given dataset.
        :type data_set: list[list[float, float]]

        :param lr: Given learning rate.
        :type lr: float

        :param max_iterations: Given maximum number of iterations until algorithm terminates.
        :type max_iterations: int
        """
        self.__check(data_set)
        if len(data_set[0]) != 2:
            raise Exception("dataset isn't two dimensional!")
        

        self.x = [point[0] for point in data_set]
        self.y = [point[1] for point in data_set]

        #Formula of line: y = m * x + b

        self.m = sum(self.x) / len(self.x)
        self.b = sum(self.y) / len(self.y)


        i = 0

        while i < max_iterations:
            sse = 0
            sse_derivation_m = 0
            sse_derivation_b = 0

            for x, y in zip(self.x, self.y):
                
                #Formula of SSE respect to above mentioned formula for line: SSE = (real_y - predicted_y)²
                #Formula can be also described as: SSE = (real_y - (slope_m * x + intercept_b))²
                sse += (y - (self.m * x + self.b))

                #Derivative of Sum of Squared Residuals respect to slope m: 
                sse_derivation_m += (-2 * (x * (y - (self.b + self.m * x))))

                #Derivative of Sum of Squared Residuals respect to intercept b: 
                sse_derivation_b += (-2 * (y -(self.b + self.m * x)))


                self.SSE.append(sse)
                self.SSE_derivative_m.append(sse_derivation_m)
                self.SSE_derivative_m.append(sse_derivation_b)

                
            step_size_m = sse_derivation_m * lr
            step_size_b = sse_derivation_b * lr


            #update slope m and intercept b:
            self.m = self.m - step_size_m
            self.b = self.b - step_size_b

            i += 1


    def predict(self, data_set):
        """
        A function to 'train the model' to the given train dataset.

        
        :param data_set: Given dataset.
        :type data_set: list[list[float]]

        
        :return: Predictions of given dataset.
        :rtype: list[float]
        """

        self.__check(data_set)
        if len(data_set[0]) != 1:
            raise Exception("dataset isn't scaler!")

        predictions = []
        
        for data_point in data_set:
            predictions.append(self.m * data_point + self.b)


        return predictions
    


    def __check(self, data_set):
        """
        A function to check if given dataset fullfills all criterias.

        
        :param data_set: Given dataset.
        :type data_set: list[list[float, float]]
        """
        if len(data_set) < 1:
            raise Exception("dataset is empty!")
        
        lenght_of_previos_data_point = len(data_point[0])
        for i, data_point in enumerate(data_set):
            if i != 0:
                lenght_of_previos_data_point = len(data_point[i-1])

            if (type(data_point[0]) != float or  type(data_point[0]) != int) or (type(data_point[1]) != float or  type(data_point[1]) != int):
                raise Exception("type of data isn't float or integer!")
            

            if lenght_of_previos_data_point != len(data_point):
                raise Exception("dataset isn't evenly!")


    