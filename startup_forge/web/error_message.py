from enum import Enum


class ErrorMessage(str, Enum):
    """Error messages"""

    PROFILE_DOES_NOT_EXIST = "PROFILE_DOES_NOT_EXIST"
    PROFILE_ALREADY_EXISTS = "PROFILE_ALREADY_EXISTS"
    EXPERIENCES_NOT_FOUND = "EXPERIENCES_NOT_FOUND"
    EXPERIENCE_NOT_FOUND = "EXPERIENCE_NOT_FOUND"
    EXPERIENCE_DOES_NOT_EXIST = "EXPERIENCE_DOES_NOT_EXIST"
    UNAUTHORIZED = "UNAUTHORIZED"
    USER_NOT_ASSOCIATED_WITH_AN_ACTIVE_PROFILE = (
        "USER_NOT_ASSOCIATED_WITH_AN_ACTIVE_PROFILE"
    )
    NO_VALID_MENTOR_MENTEE_RECORD = "NO_VALID_MENTOR_MENTEE_RECORD"
    MENTOR_NOT_ASSOCIATED_WITH_AN_ACTIVE_PROFILE = (
        "MENTOR_NOT_ASSOCIATED_WITH_AN_ACTIVE_PROFILE"
    )
    USER_HAS_A_MENTOR_ALREADY = "USER_HAS_A_MENTOR_ALREADY"


class ProfileErrorDetails(str, Enum):
    """Profile error details"""

    USER_IS_ALREADY_ASSOCIATED_WITH_A_PROFILE = (
        "USER_IS_ALREADY_ASSOCIATED_WITH_A_PROFILE"
    )
    PROFILE_DOES_NOT_EXIST = "PROFILE_DOES_NOT_EXIST"
    PROFILE_NOT_WITH_MENTOR_ROLE = "PROFILE_NOT_WITH_MENTOR_ROLE"
    PROFILE_WITH_ID_DOES_NOT_EXIST = "PROFILE_WITH_ID_DOES_NOT_EXIST"
    USER_NOT_MENTEE_OR_PROFILE_NOT_MENTOR = "USER_NOT_MENTEE_OR_PROFILE_NOT_MENTOR"
    UNAUTHORIZED = "UNAUTHORIZED"
    PROFILE_ROLE_NOT_MENTOR = "PROFILE_ROLE_NOT_MENTOR"
    PROFILE_ROLE_NOT_MENTEE = "PROFILE_ROLE_NOT_MENTEE"
    PROFILE_ALREADY_EXISTS = "PROFILE_ALREADY_EXISTS"


class EducationErrorDetails(str, Enum):
    """Education error details"""

    EDUCATION_DOES_NOT_EXIST = "EDUCATION_DOES_NOT_EXIST"


class ConnectionErrorDetails(str, Enum):
    """Connection error details"""

    NO_SUCH_CONNECTION_REQUEST = "NO_SUCH_CONNECTION_REQUEST"


class BookingErrorDetails(str, Enum):
    """Booking error details"""

    TIME_SLOT_NOT_FOUND = "TIME_SLOT_NOT_FOUND"
    PROFILE_ROLE_NOT_MENTEE = "PROFILE_ROLE_NOT_MENTEE"
    INVALID_TIME_SLOT = "INVALID_TIME_SLOT"
    TIMESLOT_OCCUPIED = "TIMESLOT_OCCUPIED"
    BOOKING_NOT_FOUND = "BOOKING_NOT_FOUND"
    BOOKING_NOT_MADE_BY_CURRENT_USER = "BOOKING_NOT_MADE_BY_CURRENT_USER"


class CommunityErrorDetails(str, Enum):
    """Community error details"""

    POST_NOT_FOUND = "POST_NOT_FOUND"
    COMMENT_NOT_FOUND = "COMMENT_NOT_FOUND"


class ReviewErrorDetails(str, Enum):
    """Review error details"""

    REVIEW_DOES_NOT_EXIST = "REVIEW_DOES_NOT_EXIST"
