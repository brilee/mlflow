from typing import Optional

from mlflow.entities._mlflow_object import _MlflowObject
from mlflow.entities.assessment_source import AssessmentSource
from mlflow.protos.service_pb2 import Assessment as ProtoAssessment


class Assessment(_MlflowObject):
    """Assessment on a Trace."""

    def __init__(
        self,
        assessment_id: str,
        assessment_name: str,
        created_timestamp_ms: int,
        last_updated_timestamp_ms: int,
        trace_id: Optional[str] = None,
        span_id: Optional[str] = None,
        source: Optional[AssessmentSource] = None,
    ) -> None:
        self._assessment_id = assessment_id
        self._assessment_name = assessment_name
        self._trace_id = trace_id
        self._span_id = span_id
        self._source = source
        self._created_timestamp_ms = created_timestamp_ms
        self._last_updated_timestamp_ms = last_updated_timestamp_ms

    def __eq__(self, other: _MlflowObject) -> bool:
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    # def to_proto(self):
    #     assessment = ProtoAssessment()
    #     assessment.assessment_id = self.assessment_id
    #     assessment.assessment_name = self.assessment_name
    #     assessment.trace_id = self.trace_id
    #     assessment.span_id = self.span_id
    #     if self.source:
    #         assessment.source = self.sources
    #     # TODO: figure out how to interconvert google.protobuf.Timestamp <-> timestamp_ms
    #     assessment.created_timestamp_ms = self.created_timestamp_ms
    #     assessment.last_updated_timestamp_ms = self.last_updated_timestamp_ms
    #     return assessment

    # @classmethod
    # def from_proto(cls, proto):
    #     return cls(
    #         proto.assessment_id,
    #         proto.assessment_name,
    #         proto.trace_id,
    #         proto.span_id,
    #         proto.source if proto.HasField("source") else None,
    #     )
