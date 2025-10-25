from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.course_exercises_partial_update_validation_error import CourseExercisesPartialUpdateValidationError
from ...models.error_response_401 import ErrorResponse401
from ...models.error_response_403 import ErrorResponse403
from ...models.error_response_404 import ErrorResponse404
from ...models.error_response_405 import ErrorResponse405
from ...models.error_response_406 import ErrorResponse406
from ...models.error_response_415 import ErrorResponse415
from ...models.error_response_500 import ErrorResponse500
from ...models.exercise import Exercise
from ...models.parse_error_response import ParseErrorResponse
from ...models.patched_exercise_request import PatchedExerciseRequest
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: Union[
        PatchedExerciseRequest,
        PatchedExerciseRequest,
        PatchedExerciseRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/core/course/exercises/{id}/",
    }

    if isinstance(body, PatchedExerciseRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedExerciseRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedExerciseRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse404,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Exercise,
        Union["CourseExercisesPartialUpdateValidationError", "ParseErrorResponse"],
    ]
]:
    if response.status_code == 400:

        def _parse_response_400(
            data: object,
        ) -> Union["CourseExercisesPartialUpdateValidationError", "ParseErrorResponse"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_course_exercises_partial_update_error_response_400_type_0 = (
                    CourseExercisesPartialUpdateValidationError.from_dict(data)
                )

                return componentsschemas_course_exercises_partial_update_error_response_400_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_course_exercises_partial_update_error_response_400_type_1 = ParseErrorResponse.from_dict(
                data
            )

            return componentsschemas_course_exercises_partial_update_error_response_400_type_1

        response_400 = _parse_response_400(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ErrorResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ErrorResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ErrorResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 405:
        response_405 = ErrorResponse405.from_dict(response.json())

        return response_405
    if response.status_code == 406:
        response_406 = ErrorResponse406.from_dict(response.json())

        return response_406
    if response.status_code == 415:
        response_415 = ErrorResponse415.from_dict(response.json())

        return response_415
    if response.status_code == 500:
        response_500 = ErrorResponse500.from_dict(response.json())

        return response_500
    if response.status_code == 200:
        response_200 = Exercise.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse404,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Exercise,
        Union["CourseExercisesPartialUpdateValidationError", "ParseErrorResponse"],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedExerciseRequest,
        PatchedExerciseRequest,
        PatchedExerciseRequest,
    ],
) -> Response[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse404,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Exercise,
        Union["CourseExercisesPartialUpdateValidationError", "ParseErrorResponse"],
    ]
]:
    """Exercises

    Args:
        id (int):
        body (PatchedExerciseRequest):
        body (PatchedExerciseRequest):
        body (PatchedExerciseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse401, ErrorResponse403, ErrorResponse404, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Exercise, Union['CourseExercisesPartialUpdateValidationError', 'ParseErrorResponse']]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedExerciseRequest,
        PatchedExerciseRequest,
        PatchedExerciseRequest,
    ],
) -> Optional[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse404,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Exercise,
        Union["CourseExercisesPartialUpdateValidationError", "ParseErrorResponse"],
    ]
]:
    """Exercises

    Args:
        id (int):
        body (PatchedExerciseRequest):
        body (PatchedExerciseRequest):
        body (PatchedExerciseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse401, ErrorResponse403, ErrorResponse404, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Exercise, Union['CourseExercisesPartialUpdateValidationError', 'ParseErrorResponse']]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedExerciseRequest,
        PatchedExerciseRequest,
        PatchedExerciseRequest,
    ],
) -> Response[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse404,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Exercise,
        Union["CourseExercisesPartialUpdateValidationError", "ParseErrorResponse"],
    ]
]:
    """Exercises

    Args:
        id (int):
        body (PatchedExerciseRequest):
        body (PatchedExerciseRequest):
        body (PatchedExerciseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse401, ErrorResponse403, ErrorResponse404, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Exercise, Union['CourseExercisesPartialUpdateValidationError', 'ParseErrorResponse']]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedExerciseRequest,
        PatchedExerciseRequest,
        PatchedExerciseRequest,
    ],
) -> Optional[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse404,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Exercise,
        Union["CourseExercisesPartialUpdateValidationError", "ParseErrorResponse"],
    ]
]:
    """Exercises

    Args:
        id (int):
        body (PatchedExerciseRequest):
        body (PatchedExerciseRequest):
        body (PatchedExerciseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse401, ErrorResponse403, ErrorResponse404, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Exercise, Union['CourseExercisesPartialUpdateValidationError', 'ParseErrorResponse']]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
