import pathlib
import ntpath

from argo.workflows.dsl import template
from argo.workflows.dsl import Workflow
from argo.workflows.dsl.templates import V1Container


class HelloWorld(Workflow):

    entrypoint = "whalesay"

    @template
    def whalesay(self) -> V1Container:
        container = V1Container(
            image="docker/whalesay:latest",
            name="whalesay",
            command=["cowsay"],
            args=["hello world"],
        )
        return container


if __name__ == "__main__":
    wf = HelloWorld()
    wf_file = ntpath.basename(__file__).replace(".py", ".yaml")
    wf.to_file(f"{pathlib.Path(__file__).parent}/{wf_file}")
