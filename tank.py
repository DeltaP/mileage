class Tank:
    def __init__(self):
        self.full = 15.9
        self.brand = {}
        self.brand['oem'] = self.full
        
    def update(self, brand, n_gallons):
        assert ((n_gallons > 0) and (n_gallons <= self.full)), "Must enter a valid number of gallons of gasoline in the range (0,%.2f]" % self.full
        used = float(self.full - n_gallons)
        ratio = used / self.full
        for key, value in self.brand.iteritems():
            self.brand[key]=value*ratio
        if brand in self.brand:
            self.brand[brand] += n_gallons
        else:
            self.brand[brand] = n_gallons
    
    def summary(self):
        print "Current state of gas tank is:\n"
        for key, value in sorted(self.brand.iteritems(), key=lambda x: x[1], reverse = True):
            if round(value,3) > 0:
                print "%.3f gallons of '%s' gasoline" % (round(value,3), key)
                
    def return_state(self):
        l = []
        for key, value in sorted(self.brand.iteritems(), key=lambda x: x[1], reverse = True):
            l.append((key, value/self.full))
        return l
