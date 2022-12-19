import os
import uuid
import datetime


def create_cloud_event_attributes():
    """Create a dictionary of CloudEvent attributes.

    Returns:
        A dictionary of CloudEvent attributes, including the specversion, type,
        dataschema, source, subject, id, time, and datacontenttype.
    """
    cloudevents_time = datetime.datetime.utcnow().isoformat() + "Z"
    cloudevent_id = uuid.uuid4().int
    cloudevent_type = "GitHub Action"
    cloudevent_dataschema = "github-action://cloud-event:1.0.0"
    cloudevent_subject = "Test GHA"

    attributes = {
        "specversion": "1.0",
        "type": cloudevent_type,
        "dataschema": cloudevent_dataschema,
        "source": "/test/gha",
        "subject": cloudevent_subject,
        "id": cloudevent_id,
        "time": cloudevents_time,
        "datacontenttype": "application/json"
    }

    return attributes


def create_cloud_event_data():
    """Create a dictionary of data to include in the CloudEvent.

    Returns:
        A dictionary of data, including the repository name, branch name, commit
        SHA, and build ID.
    """
    repository = os.getenv("GITHUB_REPOSITORY")
    commit_sha = os.getenv("GITHUB_SHA")
    build_id = os.getenv("GITHUB_RUN_ID")

    ref = os.getenv("GITHUB_REF")
    branch = ref.split("/")[-1]

    data = {
        "repository": repository,
        "branch": branch,
        "commit_sha": commit_sha,
        "build_id": build_id
    }

    return data


def create_connection():
    pass


def main():
    event = [create_cloud_event_attributes(), create_cloud_event_data()]
    print(event)


if __name__ == "__main__":
    main()
