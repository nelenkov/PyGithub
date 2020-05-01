from typing import Any, Dict, List

from github.GithubObject import CompletableGithubObject

class License(CompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def body(self) -> str: ...
    @property
    def conditions(self) -> List[str]: ...
    @property
    def description(self) -> str: ...
    @property
    def html_url(self) -> str: ...
    @property
    def implementation(self) -> str: ...
    @property
    def key(self) -> str: ...
    @property
    def limitations(self) -> List[str]: ...
    @property
    def name(self) -> str: ...
    @property
    def permissions(self) -> List[str]: ...
    @property
    def url(self) -> str: ...
    @property
    def spdx_id(self) -> str: ...