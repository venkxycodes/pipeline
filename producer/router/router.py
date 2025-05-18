from fastapi import APIRouter, status
from producer.domain.event import Event
from producer.service.aws_lambda import invoke_lambda


router = APIRouter()

@router.post("/event", status_code=status.HTTP_202_ACCEPTED)
def receive_event(event: Event):
    invoke_lambda(payload=event.model_dump())
    return {"status": "accepted"}
