"""
Provides functions for converting between different units of length.
It considers meters as the base unit.
"""
from validations import validate_input


def kilometers_to_meters(km: float) -> float:
    validate_input(km)
    return 1000 * km


def centimeters_to_meters(cm: float) -> float:
    validate_input(cm)
    return 0.01 * cm


def millimeters_to_meters(mm: float) -> float:
    validate_input(mm)
    return 0.001 * mm


def miles_to_meters(miles: float) -> float:
    validate_input(miles)
    return 1609.344 * miles


def yards_to_meters(yards: float) -> float:
    validate_input(yards)
    return 0.9144 * yards


def feet_to_meters(feet: float) -> float:
    validate_input(feet)
    return 0.3048 * feet


def inches_to_meters(inches: float) -> float:
    validate_input(inches)
    return 0.0254 * inches


"""Conversions from meters to another units"""

def meters_to_kilometers(meters: float) -> float:
    validate_input(meters)
    return 0.001 * meters


def meters_to_centimeters(meters: float) -> float:
    validate_input(meters)
    return 100 * meters


def meters_to_millimeters(meters: float) -> float:
    validate_input(meters)
    return 1000 * meters


def meters_to_miles(meters: float) -> float:
    validate_input(meters)
    return 0.000621371 * meters


def meters_to_yards(meters: float) -> float:
    validate_input(meters)
    return 1.09361 * meters


def meters_to_feet(meters: float) -> float:
    validate_input(meters)
    return 3.28084 * meters


def meters_to_inches(meters: float) -> float:
    validate_input(meters)
    return 39.3701 * meters