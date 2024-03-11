def all_peak_finder_rec(self,index_range,tols,peak__=[]):
        try:
            max_intensity_index= np.argmax(self.intensity[index_range[0]:index_range[1]])
            min_hight , bottom = tols
            i = max_intensity_index
            result_ = []
            result__ = []
            if self.intensity[max_intensity_index] > min_hight:
                while self.intensity[i-1] > bottom:
                    result__.append((self.angle[i],self.intensity[i]))
                    i = i - 1
                left__ = i
                i = max_intensity_index + 1 
                result_ = result__[::-1]
                while self.intensity[i+1] > bottom:
                    result_.append((self.angle[i],self.intensity[i]))
                    i = i + 1
                right__ = i
                peak__.append(result_)
                self.all_peak_finder_rec([right__,index_range[1]],tols,peak__)
                self.all_peak_finder_rec([index_range[0],left__],tols,peak__)
               
        except:
            pass