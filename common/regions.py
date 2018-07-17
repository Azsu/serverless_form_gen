from enum import Enum


class REGIONS:
    '''
    TODO: get this from an API
    '''
    AP_SOUTH_1 = 'ap-south-1'
    AP_SOUTHEAST_1 = 'ap-southeast-1'
    AP_SOUTHEAST_2 = 'ap-southeast-2'
    AP_NORTHEAST_1 = 'ap-northeast-1'
    SA_EAST_1 = 'sa-east-1'
    CN_NORTH_1 = 'cn-north-1'

    class EU(Enum):
        EU_WEST_1 = 'eu-west-1'
        EU_CENTRAL_1 = 'cn-north-1'

    class US(Enum):
        US_WEST_1 = 'us-west-1'
        US_WEST_2 = 'us-west-2'


