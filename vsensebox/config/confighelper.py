# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


import json
import yaml
from yaml.loader import SafeLoader

from vsensebox.config.strings import UnifiedStrings
from vsensebox.utils.commontools import getAbsPathFDS, isExist
from vsensebox.utils.logtools import add_error_log


unified_strings = UnifiedStrings()


def isDictString(input_string):
    """Check whether the :obj:`input_string` is a valid raw dictionary.

    Parameters
    ----------
    input_string : str
        An input of raw string.

    Returns
    -------
    bool
        Validation status.
    """
    res = True
    if (
        isinstance(input_string, str) and 
        len(input_string) > 4 and
        input_string[0] == '[' and
        input_string[1] == '{' and  
        input_string[-1] == ']' and 
        input_string[-2] == '}'
    ):
        try:
            yaml.load(input_string, Loader=SafeLoader)
        except ValueError as e:
            res = False
    else:
        res = False
    return res

def getCFGDict(input):
    """Get a configuration dictionary of a single document from the given :obj:`input`.

    Parameters
    ----------
    input : str or dict
        A YAML/JSON file path, or a raw/ready dictionary.

    Returns
    -------
    dict
        A configuration dictionary of a single document.
    """
    doc = {}
    if isinstance(input, str):
        if ".yaml" in input.lower() or ".json" in input.lower():
            doc = loadDocument(getAbsPathFDS(input))
        else:
            doc = loadRawYAMLString(input)
    elif isinstance(input, dict):
        doc = input
    return doc

def getListCFGDoc(input):
    """Get a list of configuration dictionary of document from the given :obj:`input`.

    Parameters
    ----------
    input : str or dict
        A YAML/JSON file path, or a raw/ready dictionary.

    Returns
    -------
    list[dict, ...]
        A list of configuration dictionary.
    """
    doc_list = []
    if isinstance(input, str):
        if ".yaml" in input.lower():
            doc_list = loadListDocument(getAbsPathFDS(input))
        else:
            doc_list = loadRawYAMLStringMT(input)
    elif isinstance(input, dict):
        for doc in input:
            doc_list.append(doc)
    return doc_list

def loadDocument(yaml_json):
    """Return a configuration dictionary of a single document from the given file 
    :obj:`yaml_json`.

    Parameters
    ----------
    yaml_json : str
        A path of a YAML/JSON file.

    Returns
    -------
    dict
        A configuration dictionary of a single document.
    """
    document = {}
    if isExist(yaml_json):
        with open(yaml_json, 'rb') as cfg:
            try:
                if '.json' in yaml_json.lower():
                    document = json.load(cfg)
                elif '.yaml' in yaml_json.lower():
                    document = yaml.load(cfg, Loader=SafeLoader)
            except ValueError as e:
                msg = 'loadDocument() -> ' + str(e)
                add_error_log(msg)
                raise ValueError(msg)
    else:
        msg = "loadDocument() -> " + str(yaml_json) + "' does not exist!"
        add_error_log(msg)
        raise ValueError(msg)
    return document

def loadListDocument(yaml_json):
    """Return a list of configuration dictionary from the given file :obj:`yaml_json`.

    Parameters
    ----------
    yaml_json : str
        A path of a YAML/JSON file.
    
    Returns
    -------
    list[dict, ...]
        A list of configuration dictionary.
    """
    document_list = []
    if isExist(yaml_json):
        with open(yaml_json, 'rb') as cfg:
            try:
                if '.json' in yaml_json.lower():
                    docs = json.load(cfg)
                elif '.yaml' in yaml_json.lower():
                    docs = yaml.load_all(cfg, Loader=SafeLoader)
            except ValueError as e:
                msg = 'loadListDocument() -> ' + str(e)
                add_error_log(msg)
                raise ValueError(msg)
            for doc in docs:
                document_list.append(doc)
    else:
        msg = "loadListDocument() -> " + str(yaml_json) + "' does not exist!"
        add_error_log(msg)
        raise ValueError(msg)
    return document_list

def loadRawYAMLString(raw_string):
    """Return a configuration dictionary of a single document from the given string 
    :obj:`raw_string`.

    Parameters
    ----------
    raw_string : str
        A raw string of JSON or YAML; for example, 
        :code:`raw_string="[{'tk_name': 'SORT'}]"`.
    
    Returns
    -------
    dict
        A configuration dictionary of a single document.
    """
    document = {}
    try:
        d = yaml.load(raw_string, Loader=SafeLoader)
        document = next(iter(d))
    except ValueError as e:
        msg = 'loadRawYAMLString() -> ' + str(e)
        add_error_log(msg)
        raise ValueError(msg)
    return document

def loadRawYAMLStringMT(raw_string):
    """Return a list of multiple YAML dictionary from the given string :obj:`raw_string`.

    Parameters
    ----------
    raw_string : str
        A raw string of JSON or YAML; for example, 
        :code:`raw_string="[{'tk_name': 'SORT'}, {'tk_name': 'DeepSORT'}]"`.
    
    Returns
    -------
    list[dict, ...]
        A list of configuration dictionary.
    """
    document_list = []
    try:
        ds = yaml.load_all(raw_string, Loader=SafeLoader)
        for d in ds:
            document_list.append(d)
    except ValueError as e:
        msg = 'loadRawYAMLStringMT() -> ' + str(e)
        add_error_log(msg)
        raise ValueError(msg)
    return document_list

def dumpDocDict(output_file, doc, header):
    """Dump a configuration dictionary of a single document into a YAML file 
    with simple format.

    Parameters
    ----------
    output_file : str
        A path file to dump.
    doc : dict
        A configuration dictionary of a single document.
    header : str
        A file header descriptoin.
    """
    try:
        with open(output_file, 'w') as dumping:
            dumping.write(header)
            for key, value in doc.items():
                key = str(key).lower()
                if str(value) == "None" or value is None:
                    value = "null # NULL=Null=null is None in Python"
                if key == "detector" or key == "tracker":
                    value = unified_strings.getUnifiedFormat(value)
                dumping.write('%s: %s\n' % (key, value))
    except ValueError as e:
        msg = 'dumpDocDict() -> ' + str(e)
        add_error_log(msg)
        raise ValueError(msg)

def dumpListDocDict(output_file, doc_list, header):
    """Dump a list of YAML dictionary into a YAML file with simple format.

    Parameters
    ----------
    output_file : str
        A path file to dump.
    doc_list : list[dict, ...]
        A list of configuration dictionary.
    header : str
        A file header descriptoin.
    """
    try: 
        with open(output_file, 'w') as dumping:
            dumping.write(header)
            sep_index = 1
            for d in doc_list:
                for key, value in d.items():
                    key = str(key).lower()
                    if str(value) == "None" or value is None:
                        value = "null # NULL=Null=null is None in Python"
                    if key == "detector" or key == "tracker":
                        value = unified_strings.getUnifiedFormat(value)
                    dumping.write('%s: %s\n' % (key, value))
                if sep_index < len(doc_list):
                    dumping.write("---\n")
                    sep_index += 1
    except ValueError as e:
        msg = 'dumpListDocDict() -> ' + str(e)
        add_error_log(msg)
        raise ValueError(msg)

