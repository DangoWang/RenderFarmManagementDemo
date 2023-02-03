#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dayu_widgets import dayu_theme
import os


def score_color(score, y):
    if score < 60:
        return dayu_theme.error_color
    elif score < 80:
        return dayu_theme.warning_color
    elif score >= 90:
        return dayu_theme.success_color
    return dayu_theme.info_color


def path_icon(path_str):
    if '.' not in str(path_str):
        return os.environ['ROOTPATH'] + '/icons/custom/folder.svg'
    return os.environ['ROOTPATH'] + f'/icons/custom/filetype_{path_str.split(".")[-1]}.svg'


header_list = [
    {
        'label': '路径',
        'key': 'path',
        'checkable': False,
        'searchable': True,
        'width': 600,
        # 'font': lambda x, y: {'underline': True},
        'icon': lambda x, y: path_icon(x)
    }, {
        'label': '大小',
        'key': 'size',
        'searchable': False,
        'selectable': False,
        'icon': ''
    }, {
        'label': '类型',
        'key': 'type',
        'width': 90,
        'searchable': False,
        'editable': False,
        'font': lambda x, y: {'bold': True},
    }, {
        'label': '修改时间',
        'key': 'lastModify',
        'selectable': False,
        'searchable': False,
        'width': 120,
    }
]

tree_data_list = [
    {
        'path': 'C',
        'size': '0',
        'type': 'folder',
        'lastModify': '2016-10-03',
        'children': [
            {
                'path': 'projects',
                'size': '0',
                'type': 'folder',
                'lastModify': '2016-10-03',
                'children': [
                    {
                        'path': 'testProject',
                        'size': '0',
                        'type': 'folder',
                        'lastModify': '2016-10-03',
                        'children': [
                            {
                                'path': 'assets',
                                'size': '0',
                                'type': 'folder',
                                'lastModify': '2016-10-03',
                                'children':[
                                    {
                                        'path': 'myfile.ma',
                                        'size': '103MB',
                                        'type': 'ma',
                                        'lastModify': '2016-10-03',
                                    }
                                ]
                            }

                        ]}
                ]
            }, {
                'path': 'configs',
                'size': '0',
                'type': 'folder',
                'lastModify': '2016-10-03',
            },
        ]
    }, {
        'path': 'D',
        'size': '0',
        'type': 'folder',
        'lastModify': '2016-10-03',
    }
]
tree_data_list_2 = [
    {
        'path': 'temp',
        'size': '0',
        'type': 'folder',
        'lastModify': '2016-10-03'
    }
]


def status_color(status):
    if status == '分析中':
        return dayu_theme.info_color
    if status == '出错':
        return dayu_theme.error_color
    if status == '警告':
        return dayu_theme.warning_color
    if status == '成功':
        return dayu_theme.success_color


analysis_header_list = [
    {
        'label': '作业ID',
        'key': 'id',
        'checkable': True,
        'width': 120,
        'searchable': True,
    }, {
        'label': '场景名',
        'key': 'fileName',
        'width': 200,
        'icon': lambda x, y: path_icon(x),
        'searchable': True,
    }, {
        'label': '状态',
        'key': 'status',
        'searchable': False,
        'color': lambda x, y: status_color(x),
        'editable': False,
    }, {
        'label': '开始时间',
        'key': 'begin',
        'width': 200,
        'selectable': False,
        'searchable': False,
    }, {
        'label': '结束时间',
        'key': 'end',
        'width': 200,
        'selectable': False,
        'searchable': False,
    }, {
        'label': '历时',
        'key': 'timeUse',
        'selectable': False,
        'searchable': False,
    }, {
        'label': '分析方式',
        'key': 'maxTime',
        'selectable': False,
        'searchable': False,
    }
]
analysis_data_list = [
    {
        'id': '1W154569',
        'fileName': 'example.ma',
        'status': '分析中',
        'begin': '2021-4-12 14:51:17',
        'end': '2021-4-12 14:52:05',
        'timeUse': '48秒',
        'maxTime': '本地'
    },
    {
        'id': '1W154570',
        'fileName': 'example2.ma',
        'status': '警告',
        'begin': '2021-4-12 14:51:17',
        'end': '2021-4-12 14:52:05',
        'timeUse': '48秒',
        'maxTime': '云端'
    },
    {
        'id': '1W154535',
        'fileName': 'example3.ma',
        'status': '成功',
        'begin': '2021-4-12 14:51:17',
        'end': '2021-4-12 14:52:05',
        'timeUse': '48秒',
        'maxTime': '云端'
    },
    {
        'id': '1W154535',
        'fileName': 'example4.ma',
        'status': '出错',
        'begin': '2021-4-12 14:51:17',
        'end': '2021-4-12 14:52:05',
        'timeUse': '48秒',
        'maxTime': '本地'
    }
]*5

render_tasks_header_list = [
    {
        'label': '作业ID',
        'key': 'id',
        'checkable': True,
        'width': 120,
        'searchable': True,
    }, {
        'label': '场景名',
        'key': 'fileName',
        'width': 200,
        'icon': lambda x, y: path_icon(x),
        'searchable': True,
    }, {
        'label': '状态',
        'key': 'status',
        'searchable': False,
        'color': lambda x, y: status_color(x),
        'editable': False,
    }, {
        'label': '进度',
        'key': 'progress',
        'searchable': False,
        'icon': os.environ['ROOTPATH'] + '/icons/custom/progress.svg',
        'editable': False,
    }, {
        'label': '失败帧',
        'key': 'fail',
        'searchable': False,
        'editable': False,
    }, {
        'label': '帧范围',
        'key': 'frameRange',
        'searchable': False,
        'editable': False,
    }, {
        'label': '费用',
        'key': 'price',
        'searchable': False,
        'editable': False,
    }, {
        'label': '优先级',
        'key': 'priority',
        'searchable': False,
        'editable': False,
    },
    {
        'label': '开始时间',
        'key': 'begin',
        'width': 200,
        'selectable': False,
        'searchable': False,
    }, {
        'label': '结束时间',
        'key': 'end',
        'width': 200,
        'selectable': False,
        'searchable': False,
    }, {
        'label': '历时',
        'key': 'timeUse',
        'selectable': False,
        'searchable': False,
    }
]

render_tasks_data_list = [
             {
                 'id': '1w234235',
                 'fileName': 'example.ma',
                 'status': '成功',
                 'progress': '',
                 'fail': '5',
                 'frameRange': '1-100[1]',
                 'price': 'C 0.55',
                 'priority': '0',
                 'begin': '2021-4-12 14:51:17',
                 'end': '2021-4-12 15:52:05',
                 'timeUse': '1小时48秒',
             },
             {
                 'id': '1w234235',
                 'fileName': 'example.ma',
                 'status': '出错',
                 'progress': '',
                 'fail': '5',
                 'frameRange': '1-100[1]',
                 'price': 'C 0.55',
                 'priority': '0',
                 'begin': '2021-4-12 14:51:17',
                 'end': '2021-4-12 15:52:05',
                 'timeUse': '1小时48秒',
             },
             {
                 'id': '1w234235',
                 'fileName': 'example.ma',
                 'status': '警告',
                 'progress': '',
                 'fail': '5',
                 'frameRange': '1-100[1]',
                 'price': 'C 0.55',
                 'priority': '0',
                 'begin': '2021-4-12 14:51:17',
                 'end': '2021-4-12 15:52:05',
                 'timeUse': '1小时48秒',
             },

]*10

job_detail_header_list = [
{
        'label': '帧任务',
        'key': 'frame',
        'checkable': True,
        'width': 120,
        'searchable': True,
    }, {
        'label': '状态',
        'key': 'status',
        'searchable': False,
        'color': lambda x, y: status_color(x),
        'editable': False,
    }, {
        'label': '耗时',
        'key': 'timeUse',
        'searchable': False,
        'editable': False,
    }, {
        'label': '费用',
        'key': 'price',
        'searchable': False,
        'editable': False,
    },
    {
        'label': '开始时间',
        'key': 'begin',
        'width': 200,
        'selectable': False,
        'searchable': False,
    }, {
        'label': '结束时间',
        'key': 'end',
        'width': 200,
        'selectable': False,
        'searchable': False,
    }
]

job_detail_data_list = [

    {
        'frame': '1-5',
        'status': '成功',
        'timeUse': '1分钟',
        'price': 'C0.5',
        'begin': '2021-5-19 15:56:02',
        'end': '2021-5-19 15:57:02',
    },
    {
        'frame': '6-10',
        'status': '警告',
        'timeUse': '1分钟',
        'price': 'C0.5',
        'begin': '2021-5-19 15:56:02',
        'end': '2021-5-19 15:57:02',
    },
    {
        'frame': '11-15',
        'status': '出错',
        'timeUse': '1分钟',
        'price': 'C0.5',
        'begin': '2021-5-19 15:56:02',
        'end': '2021-5-19 15:57:02',
    }
]*5