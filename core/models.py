from __future__ import annotations

from typing import List,Optional

from pydantic import BaseModel, Field

from datetime import datetime



class Lang(BaseModel):
    id: int
    input_caption: str
    pre_info_html: str
    pre_info_print_text: str
    ticket_text: str
    tablo_text: str
    description: str
    lang: str
    name: str
    buttonText: str


class ToService(BaseModel):
    id: int
    status: int
    point: int
    duration: int
    exp: int
    sound_template: str
    advance_limit: int
    day_limit: int
    person_day_limit: int
    inputed_as_number: int
    advance_limit_period: int
    advance_time_period: int
    enable: int
    result_required: bool
    input_required: bool
    input_required_for_standard_q: bool
    inputed_as_ext: bool
    input_caption: str
    pre_info_html: str
    pre_info_print_text: str
    ticket_text: str
    tablo_text: str
    but_x: int
    but_y: int
    but_b: int
    but_h: int
    countPerDay: int
    day: int
    description: str
    service_prefix: str
    name: str
    buttonText: str
    parentId: int
    langs: List[Lang]
    inner_services: List


class BackupItem(BaseModel):
    id: int
    number: int
    stateIn: int
    state: str
    priority: int
    to_service: ToService
    prefix: str
    stand_time: str
    need_back: bool
    temp_comments: str
    post_status: str
    postpone_period: int
    recall_cnt: int
    start_postpone_period: int
    finish_postpone_period: int
    complex_id: List
    lng: str


class ToService1(BaseModel):
    id: int
    status: int
    point: int
    duration: int
    exp: int
    sound_template: str
    advance_limit: int
    day_limit: int
    person_day_limit: int
    inputed_as_number: int
    advance_limit_period: int
    advance_time_period: int
    enable: int
    result_required: bool
    input_required: bool
    input_required_for_standard_q: bool
    inputed_as_ext: bool
    input_caption: str
    pre_info_html: str
    pre_info_print_text: str
    ticket_text: str
    tablo_text: str
    but_x: int
    but_y: int
    but_b: int
    but_h: int
    countPerDay: int
    day: int
    description: str
    service_prefix: str
    name: str
    buttonText: str
    parentId: int
    langs: List
    inner_services: List


class Service(BaseModel):
    id: int
    status: int
    point: int
    duration: int
    exp: int
    sound_template: str
    advance_limit: int
    day_limit: int
    person_day_limit: int
    inputed_as_number: int
    advance_limit_period: int
    advance_time_period: int
    enable: int
    result_required: bool
    input_required: bool
    input_required_for_standard_q: bool
    inputed_as_ext: bool
    input_caption: str
    pre_info_html: str
    pre_info_print_text: str
    ticket_text: str
    tablo_text: str
    but_x: int
    but_y: int
    but_b: int
    but_h: int
    countPerDay: int
    day: int
    description: str
    service_prefix: str
    name: str
    buttonText: str
    parentId: int
    langs: List
    inner_services: List


class PlanItem(BaseModel):
    id: int
    coeff: int
    flex: bool
    flex_invt: bool
    service: Service


class Shadow(BaseModel):
    id_old_service: int
    id_old_customer: int
    old_nom: int
    old_pref: str
    old_start_time: str
    old_cust_state: str


class FromUser(BaseModel):
    id: int
    enable: int
    is_admin: bool
    is_report_access: bool
    is_parallel: bool
    pass_: str = Field(..., alias='pass')
    point: str
    name: str
    adress_rs: int
    point_ext: str
    tablo_text: str
    plan: List[PlanItem]
    services_cnt: int
    pause: bool
    shadow: Shadow


class ParallelBackupItem(BaseModel):
    id: int
    number: int
    stateIn: int
    state: str
    priority: int
    to_service: ToService1
    from_user: FromUser
    prefix: str
    stand_time: str
    start_time: Optional[str]
    need_back: bool
    temp_comments: str
    post_status: str
    postpone_period: int
    recall_cnt: int
    start_postpone_period: int
    finish_postpone_period: int
    complex_id: List
    lng: str


class Model(BaseModel):
    backup: List[BackupItem]
    parallelBackup: List[ParallelBackupItem]
    postponed: List
    pauses: List
    date: int

class Ticket(BaseModel):
    status: str
    service_id: str
    service_name: str
    user_name: Optional[str]
    stand_time: str
    start_time: Optional[datetime]
    waite_start_time: Optional[int]
    waite_stand_time: Optional[int]

