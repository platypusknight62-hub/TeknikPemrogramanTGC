from abc to import ABC ,abstractmethod  

class survey(ABC):
    @abstractmethod
    def run(self):
        pass
    class seismicsurvey(survey):
       def process(self):
          print("Processing seismic survey data...")

    class gravitysurvey(survey):
       def process(self):
          print("Processing gravity survey data...")
    
    class magneticcsurvey(survey):
       def process(self):
          print("Processing magnetic survey data...")

surver = [
    seismicsurvey(),
    gravitysurvey(),
    magneticcsurvey()
]

for s in survey:
   s.run()