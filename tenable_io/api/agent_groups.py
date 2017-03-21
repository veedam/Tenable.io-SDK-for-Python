from tenable_io.api.base import BaseApi, BaseRequest
from tenable_io.api.models import AgentGroup, AgentGroupList


class AgentGroupsApi(BaseApi):

    def add_agent(self, scanner_id, group_id, agent_id):
	"""Adds a new agent to group.

	:param scanner_id: The scanner ID.
        :param group_id: The group ID.
	:param agent_id: The agent ID.
        :raise TenableIOApiException:  When API error is encountered.
        :return: True if successful
        """
	response = self._client.put('scanners/%(scanner_id)s/agent-groups/%(group_id)s/agents/%(agent_id)s', {}, {'scanner_id': scanner_id, 'group_id': group_id, 'agent_id': agent_id})
	return True

    def configure(self, scanner_id, group_id, agent_group_configure):
	"""Changes name of agent group.

	:param scanner_id: The scanner ID.
        :param group_id: The group ID.
        :param agent_group_create: An instance of :class:`AgentGroupConfigureRequest`.
        :raise TenableIOApiException:  When API error is encountered.
        :return: True if successful
        """
	response = self._client.put('scanners/%(scanner_id)s/agent-groups/%(group_id)s', agent_group_configure, {'scanner_id': scanner_id, 'group_id': group_id})
	return True

    def create(self, scanner_id, agent_group_create):
        """Create a new agent group.

	:param scanner_id: The scanner ID.
        :param agent_group_create: An instance of :class:`AgentGroupCreateRequest`.
        :raise TenableIOApiException:  When API error is encountered.
        :return: An instance of :class:`tenable_io.api.models.TargetGroup`.
        """
        response = self._client.post('scanners/%(scanner_id)s/agent-groups', agent_group_create, {'scanner_id': scanner_id})
        return AgentGroup.from_json(response.text)

    def delete(self, scanner_id, group_id):
        """Delete an agent group.

	:param scanner_id: The scanner ID.
        :param group_id: The group ID.
        :raise TenableIOApiException:  When API error is encountered.
        :return: True if successful
        """
        self._client.delete('scanners/%(scanner_id)s/agent-groups/%(group_id)s', {'scanner_id': scanner_id, 'group_id': group_id})
        return True

    def delete_agent(self, scanner_id, group_id, agent_id):
	"""Deletes an agent from group.

	:param scanner_id: The scanner ID.
        :param group_id: The group ID.
	:param agent_id: The agent ID.
        :raise TenableIOApiException:  When API error is encountered.
        :return: True if successful
        """
	response = self._client.delete('scanners/%(scanner_id)s/agent-groups/%(group_id)s/agents/%(agent_id)s', {'scanner_id': scanner_id, 'group_id': group_id, 'agent_id': agent_id})
	return True

    def details(self, scanner_id, group_id):
        """Return details of the agent group.

	:param scanner_id: The scanner ID.
        :param group_id: The group ID.
        :raise TenableIOApiException:  When API error is encountered.
        :return: An instance of :class:`tenable_io.api.models.AgentGroup`.
        """
        response = self._client.get('scanners/%(scanner_id)s/agent-groups/%(group_id)s', {'scanner_id': scanner_id, 'group_id': group_id})
        return AgentGroup.from_json(response.text)

    def list(self, scanner_id):
        """Return the current agent groups for scanner.

	:param scanner_id: The scanner ID.
        :raise TenableIOApiException:  When API error is encountered.
        :return: An instance of :class:`tenable_io.api.models.AgentGroupList`
        """
        response = self._client.get('scanners/%(scanner_id)s/agent-groups', {'scanner_id': scanner_id})
        return AgentGroupList.from_json(response.text)


class AgentGroupCreateRequest(BaseRequest):

    def __init__(
            self,
            name=None,
    ):
        self.name = name


class AgentGroupConfigureRequest(BaseRequest):

    def __init__(
            self,
            name=None,
    ):
        self.name = name
