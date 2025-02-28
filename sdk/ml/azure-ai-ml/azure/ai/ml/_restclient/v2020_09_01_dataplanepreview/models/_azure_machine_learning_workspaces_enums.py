# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class BatchLoggingLevel(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Log verbosity for batch inferencing.
    Increasing verbosity order for logging is : Warning, Info and Debug.
    The default value is Info.
    """

    INFO = "Info"
    WARNING = "Warning"
    DEBUG = "Debug"

class CreatedByType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class DatasetType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    SIMPLE = "Simple"
    DATAFLOW = "Dataflow"

class InferenceDataInputType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    DATASET_VERSION = "DatasetVersion"
    DATASET_ID = "DatasetId"
    DATA_URL = "DataUrl"

class InputDeliveryMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to determine the input data delivery mode.
    """

    READ_ONLY_MOUNT = "ReadOnlyMount"
    READ_WRITE_MOUNT = "ReadWriteMount"
    DOWNLOAD = "Download"
    DIRECT = "Direct"
    EVAL_MOUNT = "EvalMount"
    EVAL_DOWNLOAD = "EvalDownload"

class JobInputType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to determine the Job Input Type.
    """

    URI_FILE = "UriFile"
    URI_FOLDER = "UriFolder"
    ML_TABLE = "MLTable"
    LITERAL = "Literal"
    CUSTOM_MODEL = "CustomModel"
    ML_FLOW_MODEL = "MLFlowModel"
    TRITON_MODEL = "TritonModel"

class JobOutputType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to determine the Job Output Type.
    """

    URI_FILE = "UriFile"
    URI_FOLDER = "UriFolder"
    ML_TABLE = "MLTable"
    CUSTOM_MODEL = "CustomModel"
    ML_FLOW_MODEL = "MLFlowModel"
    TRITON_MODEL = "TritonModel"

class JobProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    IN_PROGRESS = "InProgress"

class JobStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The status of a job.
    """

    NOT_STARTED = "NotStarted"
    STARTING = "Starting"
    PROVISIONING = "Provisioning"
    PREPARING = "Preparing"
    QUEUED = "Queued"
    RUNNING = "Running"
    FINALIZING = "Finalizing"
    CANCEL_REQUESTED = "CancelRequested"
    COMPLETED = "Completed"
    FAILED = "Failed"
    CANCELED = "Canceled"
    NOT_RESPONDING = "NotResponding"
    PAUSED = "Paused"
    UNKNOWN = "Unknown"

class OutputDeliveryMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Output data delivery mode enums.
    """

    READ_WRITE_MOUNT = "ReadWriteMount"
    UPLOAD = "Upload"
