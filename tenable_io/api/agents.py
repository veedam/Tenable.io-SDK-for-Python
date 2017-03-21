from tenable_io.api.base import BaseApi
from tenable_io.api.models import Agent, AgentList


class AgentsApi(BaseApi):

    def delete(self, scanner_id, agent_id):
        """Delete an agent.

        :param scanner_id: The scanner ID.
	:param agent_id: The agent ID.
        :raise TenableIOApiException:  When API error is encountered.
        :return: True if successful.
        """
        self._client.delete('scanners/%(scanner_id)s/agents/%(agent_id)s', {'scanner_id': scanner_id, 'agent_id': agent_id})
        return True

    def list(self, scanner_id):
        """Return the agent list.

	:param scanner_id: The scanner ID.
        :raise TenableIOApiException:  When API error is encountered.
        :return: An instance of :class:`tenable_io.api.models.Agentlist`.
        """
        response = self._client.get('scanners/%(scanner_id)s/agents', {'scanner_id': scanner_id})
        return AgentList.from_json(response.text)
