from abc import ABC, abstractmethod


class Survey(ABC):
    @abstractmethod
    def run(self):
        pass

class SeismicSurvey(Survey):
    def run(self):
        print("Processing seismic survey data...")

class GravitySurvey(Survey):
    def run(self):
        print("Processing gravity survey data...")

class MagneticSurvey(Survey):
    def run(self):
        print("Processing magnetic survey data...")


Survey = [
    SeismicSurvey(),
    GravitySurvey(),
    MagneticSurvey()
]

# Iterasi objek
for s in Survey:
    s.run()
