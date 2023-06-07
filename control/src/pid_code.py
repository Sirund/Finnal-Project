class PID:
    def __init__(self, P, I, D, Target):
        self.__p = P
        self.__i = I
        self.__d = D
        self.__target = Target
        self.__feedback = 0
        self.__last_err = 0

        self.__max_i = 1000

        self.__max_out = 1000
        self.__min_out = 0

        self.__cur_err = 0
        self.__integral_cum = 0 
        self.__cycle_derivative = 0 



    def calculation(self):
        self.__cur_err = self.__target - self.__feedback
        self.__integral_cum += self.__cur_err
        self.__cycle_derivative = self.__cur_err - self.__last_err
 
        if self.__integral_cum > self.__max_i:
            self.__integral_cum = self.__max_i
        elif self.__integral_cum < -self.__max_i:
            self.__integral_cum = -self.__max_i
        
        output = (self.__cur_err * self.__p) + (self.__integral_cum * self.__i) + (self.__cycle_derivative * self.__d)
        if output > self.__max_out:
            output = self.__max_out
        elif output < self.__min_out:
            output = self.__min_out

        self.__last_err = self.__cur_err
        
        return output
    
#==================================================================================================================#

    @property
    def value_p(self):
        return self.__p
    
    @property
    def value_i(self):
        return self.__i
    
    @property
    def value_d(self):
        return self.__d    

    @property
    def value_proporsional(self):
        return self.__cur_err * self.__p
    
    @property
    def value_integral(self):
        return self.__integral_cum * self.__i

    @property
    def value_derivative(self):
        return self.__cycle_derivative * self.__d 

    @property
    def value_integral_cumulation(self):
        return self.__integral_cum 
    
    @property
    def target(self):
        pass

    @property
    def pid(self):
        pass

    @property
    def feedback(self):
        pass

    @property
    def integral_limit(self):
        pass

    @property
    def output_bound(self):
        pass

#==================================================================================================================#

    @value_p.setter
    def value_p(self, input):
        self.__p = input

    @value_i.setter
    def value_i(self, input):
        self.__i = input

    @value_d.setter
    def value_d(self, input):
        self.__d = input

    @target.setter
    def target(self, input):
        self.__target = input

    @pid.setter
    def set_pid(self, P, I, D):
        self.__p = P
        self.__i = I
        self.__d = D

    @feedback.setter
    def set_feedback(self, input):
        self.__feedback = input

    @integral_limit.setter
    def integral_limit(self, max):
        self.__max_i = max

    @output_bound.setter
    def output_bound(self, upper, lower):
        self.__max_out = upper
        self.__min_out = lower
