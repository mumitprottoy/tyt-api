from django.contrib import admin
from .models import *


admin.site.register([
    Therapist,
    TherapistExperience,
    TherapistExpertise,
    TherapistProfilePicture,
    TherapistQualification,
    TherapistWorkplace,
    ExpertiseField
])
