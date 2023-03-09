import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

class SmallCactus( Obstacle ):
    
    def __init__(self):
        cactus  = [SMALL_CACTUS,LARGE_CACTUS]
        cactus_var = random.randint(0,2)
        cactus_type = cactus[random.randint(0,1)]
        image = cactus_type [cactus_var]
        super ().__init__(image)
        if cactus_type == SMALL_CACTUS:
            self.rect.y = 325
        else:
            self.rect.y = 300

    #def __init__(self):
    #    cactus_type = random.randint( 0,2)
    #    image = SMALL_CACTUS [cactus_type]
    #    super ().__init__(image)
    #    self.rect.y = 325
        
        