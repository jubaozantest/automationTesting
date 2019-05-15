class GlobalExtract:
    DIT={}

    def set_extract(self,data):
        self.DIT=data

    def get_extract(self,key):
        return self.DIT[key]
