# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mistk.transform.server.models.base_model_ import Model
from mistk.transform.server.models.mistk_dataset import MistkDataset  # noqa: F401,E501
from mistk.transform.server import util


class TransformSpecificationInitParams(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, input_datasets: List[MistkDataset]=None, output_dataset: MistkDataset=None, properties: object=None):  # noqa: E501
        """TransformSpecificationInitParams - a model defined in Swagger

        :param input_datasets: The input_datasets of this TransformSpecificationInitParams.  # noqa: E501
        :type input_datasets: List[MistkDataset]
        :param output_dataset: The output_dataset of this TransformSpecificationInitParams.  # noqa: E501
        :type output_dataset: MistkDataset
        :param properties: The properties of this TransformSpecificationInitParams.  # noqa: E501
        :type properties: object
        """
        self.swagger_types = {
            'input_datasets': List[MistkDataset],
            'output_dataset': MistkDataset,
            'properties': object
        }

        self.attribute_map = {
            'input_datasets': 'inputDatasets',
            'output_dataset': 'outputDataset',
            'properties': 'properties'
        }

        self._input_datasets = input_datasets
        self._output_dataset = output_dataset
        self._properties = properties

    @classmethod
    def from_dict(cls, dikt) -> 'TransformSpecificationInitParams':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TransformSpecificationInitParams of this TransformSpecificationInitParams.  # noqa: E501
        :rtype: TransformSpecificationInitParams
        """
        return util.deserialize_model(dikt, cls)

    @property
    def input_datasets(self) -> List[MistkDataset]:
        """Gets the input_datasets of this TransformSpecificationInitParams.

        A list of directory paths where input files can be found.  # noqa: E501

        :return: The input_datasets of this TransformSpecificationInitParams.
        :rtype: List[MistkDataset]
        """
        return self._input_datasets

    @input_datasets.setter
    def input_datasets(self, input_datasets: List[MistkDataset]):
        """Sets the input_datasets of this TransformSpecificationInitParams.

        A list of directory paths where input files can be found.  # noqa: E501

        :param input_datasets: The input_datasets of this TransformSpecificationInitParams.
        :type input_datasets: List[MistkDataset]
        """
        if input_datasets is None:
            raise ValueError("Invalid value for `input_datasets`, must not be `None`")  # noqa: E501

        self._input_datasets = input_datasets

    @property
    def output_dataset(self) -> MistkDataset:
        """Gets the output_dataset of this TransformSpecificationInitParams.

        A list of directory paths where output files will be saved  # noqa: E501

        :return: The output_dataset of this TransformSpecificationInitParams.
        :rtype: MistkDataset
        """
        return self._output_dataset

    @output_dataset.setter
    def output_dataset(self, output_dataset: MistkDataset):
        """Sets the output_dataset of this TransformSpecificationInitParams.

        A list of directory paths where output files will be saved  # noqa: E501

        :param output_dataset: The output_dataset of this TransformSpecificationInitParams.
        :type output_dataset: MistkDataset
        """

        self._output_dataset = output_dataset

    @property
    def properties(self) -> object:
        """Gets the properties of this TransformSpecificationInitParams.

        A dictionary of key value pairs for transform plugin arguments.  # noqa: E501

        :return: The properties of this TransformSpecificationInitParams.
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties: object):
        """Sets the properties of this TransformSpecificationInitParams.

        A dictionary of key value pairs for transform plugin arguments.  # noqa: E501

        :param properties: The properties of this TransformSpecificationInitParams.
        :type properties: object
        """

        self._properties = properties
