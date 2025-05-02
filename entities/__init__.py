"""Entities package.

This package contains entity definitions for Graphiti MCP Server.
"""

from entities.entity_registry import (
    register_entity,
    get_entities,
    get_entity_subset,
)

# Import all entity modules to ensure they're registered
# This is optional but helps with discoverability
from entities.base import metadata
from entities.connectors import agent, developer, goal, project
from entities.actions import action, procedure
from entities.constraints import requirement
from entities.interaction import feedback, interaction_model, preferences
from entities.resources import artifact, documentation, resource, tool