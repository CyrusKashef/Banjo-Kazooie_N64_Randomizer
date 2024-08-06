###################
##### IMPORTS #####
###################

from randomizer.constants.int_values.transformation_enums import TRANSFORMATION_ENUMS as TRANSFORMATIONS

###################################
##### ALLOWED TRANSFORMATIONS #####
###################################

class ALLOWED_TRANSFORMATIONS():
    # Only One Transformation
    only_crocodile = [
        TRANSFORMATIONS.crocodile]
    only_walrus = [
        TRANSFORMATIONS.walrus]
    only_pumpkin = [
        TRANSFORMATIONS.pumpkin]
    only_bee = [
        TRANSFORMATIONS.bee]
    # Mumbo Huts
    mumbos_hut_termite = [
        TRANSFORMATIONS.banjo_kazooie,
        TRANSFORMATIONS.termite]
    mumbos_hut_crocodile = [
        TRANSFORMATIONS.banjo_kazooie,
        TRANSFORMATIONS.crocodile]
    mumbos_hut_walrus = [
        TRANSFORMATIONS.banjo_kazooie,
        TRANSFORMATIONS.walrus]
    mumbos_hut_pumpkin = [
        TRANSFORMATIONS.banjo_kazooie,
        TRANSFORMATIONS.pumpkin]
    mumbos_hut_bee = [
        TRANSFORMATIONS.banjo_kazooie,
        TRANSFORMATIONS.bee]
    # Groups
    any_transformation = [
        TRANSFORMATIONS.banjo_kazooie,
        TRANSFORMATIONS.termite,
        TRANSFORMATIONS.crocodile,
        TRANSFORMATIONS.walrus,
        TRANSFORMATIONS.pumpkin,
        TRANSFORMATIONS.bee]
    non_banjo_transformation = [
        TRANSFORMATIONS.termite,
        TRANSFORMATIONS.crocodile,
        TRANSFORMATIONS.walrus,
        TRANSFORMATIONS.pumpkin,
        TRANSFORMATIONS.bee]