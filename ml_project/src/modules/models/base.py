from __future__ import annotations

import numpy
import typing

from entities import (
	BaseLoader,
	ModuleParams,
)


class BaseModel:

	def __init__(
		self,
		config_path: str,
	) -> BaseModel:

		self.params = BaseLoader(ModuleParams).read_params(config_path)

		pass


	def train(
		self,
		data: typing.Tuple[numpy.ndarray],
	) -> typing.NoReturn:

		pass
		

	def eval(
		self,
		data: typing.Tuple[numpy.ndarray],
	) -> typing.NoReturn:

		pass


	def save(
		self,
	) -> typing.NoReturn:

		pass