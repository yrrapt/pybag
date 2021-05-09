# -*- coding: utf-8 -*-
# Stubs for pybag.core (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from builtins import int
from builtins import str
from pybag.enum import LogLevel
from pybag.enum import Orient2D
from pybag.enum import SigType
from pybag.enum import Orientation
from typing import overload
from typing import Optional
from typing import Tuple
from typing import Iterator
from typing import Any
from typing import List
from typing import Iterable
from typing import Union

COORD_MAX: int = ...
COORD_MIN: int = ...
SUPPLY_SUFFIX: str = ...


def convert_cdba_name_bit(name: str, design_output_code: int = 2) -> str: ...


def coord_to_custom_htr(coord: int, pitch: int, off: int, round_mode: int, even: bool) -> int: ...


def gds_equal(lhs_file: str, rhs_file: str) -> bool: ...


def get_bag_logger() -> FileLogger: ...


def get_cdba_name_bits(name: str, design_output_code: int = 2) -> List[str]: ...


def get_cv_header(cv: PySchCellView, cell_name: str, fmt_code: int) -> str: ...


def get_wire_iterator(grid: PyRoutingGrid, tr_colors: TrackColoring, tid: PyTrackID, lower: int, upper: int) -> Iterator[Tuple[str, str, BBox]]: ...


def implement_gds(fname: str, lib_name: str, layer_map: str, obj_map: str, cv_list: Iterable[Tuple[str, PyLayCellView]]) -> None: ...


def implement_netlist(fname: str, content_list: List[Tuple[str, Tuple[PySchCellView, str]]], top_list: List[str], fmt_code: int, flat: bool, shell: bool, top_subckt: bool, square_bracket: bool, rmin: int, precision: int, sup_code: int, prim_fname: str, cv_info_list: List[PySchCellViewInfo], cv_netlist: str, cv_info_out: Optional[List[PySchCellViewInfo]]) -> None: ...


def implement_yaml(fname: str, content_list: Iterable[Tuple[str, Tuple[PySchCellView, str]]]) -> None: ...


def make_tr_colors(tech: PyTech) -> TrackColoring: ...


def read_gds(fname: str, layer_map: str, obj_map: str, grid: PyRoutingGrid, tr_colors: TrackColoring) -> List[PyLayCellView]: ...


class BBox:
    @property
    def h(self) -> int: ...
    @property
    def w(self) -> int: ...
    @property
    def xh(self) -> int: ...
    @property
    def xl(self) -> int: ...
    @property
    def xm(self) -> int: ...
    @property
    def yh(self) -> int: ...
    @property
    def yl(self) -> int: ...
    @property
    def ym(self) -> int: ...
    @overload
    def __init__(self, xl: int, yl: int, xh: int, yh: int) -> None: ...
    @overload
    def __init__(self, orient_code: int, tl: int, th: int, pl: int, ph: int) -> None: ...
    def __eq__(self, other: BBox) -> bool: ...
    def expand(self, dx: int = 0, dy: int = 0) -> BBox: ...
    def extend(self, x: Optional[int] = None, y: Optional[int] = None) -> BBox: ...
    def extend_orient(self, orient_code: int, ct: Optional[int] = None, cp: Optional[int] = None) -> BBox: ...
    def flip_xy(self) -> BBox: ...
    def get_center(self, orient_code: int) -> int: ...
    def get_coord(self, orient_code: int, bnd_code: bool) -> int: ...
    def get_dim(self, orient_code: int) -> int: ...
    def get_expand(self, dx: int = 0, dy: int = 0) -> BBox: ...
    def get_extend(self, x: Optional[int] = None, y: Optional[int] = None) -> BBox: ...
    def get_extend_orient(self, orient_code: int, ct: Optional[int] = None, cp: Optional[int] = None) -> BBox: ...
    def get_flip_xy(self) -> BBox: ...
    def get_immutable_key(self) -> Tuple[int, int, int, int]: ...
    def get_intersect(self, bbox: BBox) -> BBox: ...
    def get_interval(self, orient_code: int) -> Tuple[int, int]: ...
    @staticmethod
    def get_invalid_bbox() -> BBox: ...
    def get_merge(self, bbox: BBox) -> BBox: ...
    def get_move_by(self, dx: int = 0, dy: int = 0) -> BBox: ...
    def get_move_by_orient(self, orient_code: int, dt: int = 0, dp: int = 0) -> BBox: ...
    def get_transform(self, xform: Transform) -> BBox: ...
    def intersect(self, bbox: BBox) -> BBox: ...
    def is_physical(self) -> bool: ...
    def is_valid(self) -> bool: ...
    def merge(self, bbox: BBox) -> BBox: ...
    def move_by(self, dx: int = 0, dy: int = 0) -> BBox: ...
    def move_by_orient(self, orient_code: int, dt: int = 0, dp: int = 0) -> BBox: ...
    def overlaps(self, bbox: BBox) -> bool: ...
    def set_interval(self, orient_code: int, lo: int, hi: int) -> BBox: ...
    def transform(self, xform: Transform) -> BBox: ...


class BBoxArray:
    @property
    def base(self) -> BBox: ...
    @property
    def bound_box(self) -> BBox: ...
    @property
    def nx(self) -> int: ...
    @property
    def ny(self) -> int: ...
    @property
    def spx(self) -> int: ...
    @property
    def spy(self) -> int: ...
    @property
    def xh(self) -> int: ...
    @property
    def xl(self) -> int: ...
    @property
    def xm(self) -> int: ...
    @property
    def yh(self) -> int: ...
    @property
    def yl(self) -> int: ...
    @property
    def ym(self) -> int: ...
    @overload
    def __init__(self, base: BBox, nx: int = 1, ny: int = 1, spx: int = 0, spy: int = 0) -> None: ...
    @overload
    def __init__(self, base: BBox, orient_code: int, nt: int = 1, spt: int = 0, np: int = 1, spp: int = 0) -> None: ...
    def __eq__(self, other: BBoxArray) -> bool: ...
    def __iter__(self) -> Iterator[BBox]: ...
    def extend_orient(self, orient_code: int, ct: Optional[int] = None, cp: Optional[int] = None) -> BBoxArray: ...
    def get_array_info(self, orient_code: int) -> Tuple[int, int]: ...
    def get_bbox(self, idx: int) -> BBox: ...
    def get_coord(self, orient_code: int, bnd_code: bool) -> int: ...
    def get_copy(self) -> BBoxArray: ...
    def get_extend_orient(self, orient_code: int, ct: Optional[int] = None, cp: Optional[int] = None) -> BBoxArray: ...
    def get_move_by(self, dx: int = 0, dy: int = 0) -> BBoxArray: ...
    def get_num(self, orient_code: int) -> int: ...
    def get_sp(self, orient_code: int) -> int: ...
    def get_sub_array(self, orient_code: int, div_num: int, idx: int) -> BBoxArray: ...
    def get_transform(self, xform: Transform) -> BBoxArray: ...
    def move_by(self, dx: int = 0, dy: int = 0) -> BBoxArray: ...
    def set_interval(self, orient_code: int, lo: int, hi: int) -> BBoxArray: ...
    def transform(self, xform: Transform) -> BBoxArray: ...


class BBoxCollection:
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator[BBoxArray]: ...
    def __len__(self) -> int: ...
    def add_rect_arr(self, box: BBox, nx: int = 1, ny: int = 1, spx: int = 0, spy: int = 0) -> None: ...


class FileLogger:
    @property
    def flush_level(self) -> LogLevel: ...
    @property
    def level(self) -> LogLevel: ...
    @property
    def log_basename(self) -> str: ...
    def __init__(self, name: str, log_fname: str, stdout_level: int) -> None: ...
    def critical(self, msg: str) -> None: ...
    def debug(self, msg: str) -> None: ...
    def error(self, msg: str) -> None: ...
    def flush(self) -> None: ...
    def flush_on(self, level: int) -> None: ...
    def info(self, msg: str) -> None: ...
    def log(self, level: int, msg: str) -> None: ...
    def set_level(self, level: int) -> None: ...
    def trace(self, msg: str) -> None: ...
    def warn(self, msg: str) -> None: ...


class PyBlockage:
    def __init__(self) -> None: ...
    def commit(self) -> None: ...


class PyBoundary:
    def __init__(self) -> None: ...
    def commit(self) -> None: ...


class PyDisjointIntervals:
    @property
    def start(self) -> int: ...
    @property
    def stop(self) -> int: ...
    def __init__(self) -> None: ...
    def __bool__(self) -> bool: ...
    def __contains__(self, key: Tuple[int, int]) -> bool: ...
    def __iter__(self) -> Iterator[Tuple[int, int]]: ...
    def __len__(self) -> int: ...
    def add(self, intv: Tuple[int, int], val: Any = None, merge: bool = False, abut: bool = False, check_only: bool = False) -> bool: ...
    @overload
    def covers(self, key: Tuple[int, int]) -> bool: ...
    @overload
    def covers(self, key: int) -> bool: ...
    def get_complement(self, total_intv: Tuple[int, int]) -> PyDisjointIntervals: ...
    def get_copy(self) -> PyDisjointIntervals: ...
    def get_first_overlap_item(self, key: Tuple[int, int]) -> Optional[Tuple[Tuple[int, int], Any]]: ...
    def get_intersection(self, other: PyDisjointIntervals) -> PyDisjointIntervals: ...
    def get_next(self, val: int, even: bool = True) -> int: ...
    def get_prev(self, val: int, even: bool = True) -> int: ...
    def get_transform(self, scale: int = 1, shift: int = 0) -> PyDisjointIntervals: ...
    def intervals(self) -> Iterator[Tuple[int, int]]: ...
    def items(self) -> Iterator[Tuple[Tuple[int, int], Any]]: ...
    def overlap_intervals(self, key: Tuple[int, int]) -> Iterator[Tuple[int, int]]: ...
    def overlap_items(self, key: Tuple[int, int]) -> Iterator[Tuple[Tuple[int, int], Any]]: ...
    def overlap_values(self, key: Tuple[int, int]) -> Iterator[Any]: ...
    def overlaps(self, key: Tuple[int, int]) -> bool: ...
    def remove(self, key: Tuple[int, int]) -> bool: ...
    def remove_overlaps(self, key: Tuple[int, int]) -> bool: ...
    def subtract(self, key: Tuple[int, int]) -> bool: ...
    def values(self) -> Iterator[Any]: ...


class PyLayCellView:
    @property
    def cell_name(self) -> str: ...
    @property
    def is_empty(self) -> bool: ...
    def __init__(self, grid: PyRoutingGrid, tr_colors: TrackColoring, cell_name: str) -> None: ...
    def __eq__(self, other: PyLayCellView) -> bool: ...
    def add_blockage(self, layer: str, blk_code: int, points: List[Tuple[int, int]], commit: bool) -> PyBlockage: ...
    def add_boundary(self, bnd_code: int, points: List[Tuple[int, int]], commit: bool) -> PyBoundary: ...
    def add_instance(self, cv: PyLayCellView, name: str, xform: Transform, nx: int, ny: int, spx: int, spy: int, commit: bool) -> PyLayInstRef: ...
    def add_label(self, layer: str, purpose: str, xform: Transform, label: str, height: int) -> None: ...
    def add_path(self, layer: str, purpose: str, points: List[Tuple[int, int]], half_width: int, style0: int, style1: int, stylem: int, commit: bool) -> PyPath: ...
    def add_path45_bus(self, layer: str, purpose: str, points: List[Tuple[int, int]], widths: List[int], spaces: List[int], style0: int, style1: int, stylem: int, commit: bool) -> PyPath: ...
    def add_pin(self, layer: str, net: str, label: str, bbox: BBox) -> None: ...
    def add_pin_arr(self, net: str, label: str, tid: PyTrackID, lower: int, upper: int) -> None: ...
    def add_poly(self, layer: str, purpose: str, points: List[Tuple[int, int]], commit: bool) -> PyPolygon: ...
    def add_prim_instance(self, lib: str, cell: str, view: str, name: str, xform: Transform, nx: int, ny: int, spx: int, spy: int, commit: bool) -> PyLayInstRef: ...
    def add_rect(self, layer: str, purpose: str, bbox: BBox, commit: bool) -> PyRect: ...
    @overload
    def add_rect_arr(self, layer: str, purpose: str, box: BBox, nx: int, ny: int, spx: int, spy: int) -> None: ...
    @overload
    def add_rect_arr(self, layer: str, purpose: str, barr: BBoxArray) -> None: ...
    def add_rect_list(self, layer: str, purpose: str, bcol: BBoxCollection) -> None: ...
    def add_via(self, xform: Transform, via_id: str, params: ViaParam, add_layers: bool, commit: bool) -> PyVia: ...
    def add_via_arr(self, xform: Transform, via_id: str, params: ViaParam, add_layers: bool, nx: int, ny: int, spx: int, spy: int) -> None: ...
    def add_via_on_intersections(self, tid1: PyTrackID, tid2: PyTrackID, l1: int, u1: int, l2: int, u2: int, extend: bool, contain: bool) -> Tuple[Tuple[int, int], Tuple[int, int]]: ...
    def add_warr(self, tid: PyTrackID, lower: int, upper: int, is_dummy: bool = False) -> None: ...
    def connect_barr_to_tracks(self, lev_code: int, layer: str, purpose: str, barr: BBoxArray, tid: PyTrackID, tr_lower: Optional[int], tr_upper: Optional[int], min_len_code: int, w_lower: Optional[int], w_upper: Optional[int]) -> Tuple[Tuple[int, int], Tuple[int, int]]: ...
    def connect_warr_to_tracks(self, w_tid: PyTrackID, tid: PyTrackID, w_lower: int, w_upper: int) -> Tuple[Tuple[int, int], Tuple[int, int]]: ...
    def do_max_space_fill(self, level: int, bbox: BBox, fill_boundary: bool, fill_info: Tuple[int, int, int, int, float]) -> None: ...
    def get_intersect(self, layer: int, bnd_box: BBox, spx: int, spy: int, no_sp: bool) -> List[BBox]: ...
    def get_rect_bbox(self, layer: str, purpose: str) -> BBox: ...
    def set_grid(self, grid: PyRoutingGrid) -> None: ...


class PyLayInstRef:
    @property
    def committed(self) -> bool: ...
    @property
    def inst_name(self) -> str: ...
    @property
    def nx(self) -> int: ...
    @nx.setter
    def nx(self, val: int) -> None: ...
    @property
    def ny(self) -> int: ...
    @ny.setter
    def ny(self, val: int) -> None: ...
    @property
    def spx(self) -> int: ...
    @spx.setter
    def spx(self, val: int) -> None: ...
    @property
    def spy(self) -> int: ...
    @spy.setter
    def spy(self, val: int) -> None: ...
    @property
    def xform(self) -> Transform: ...
    def __init__(self, *args: Any, **kwargs: Any) -> Any: ...
    def commit(self) -> None: ...
    def move_by(self, dx: int, dy: int) -> None: ...
    def set_master(self, new_master: PyLayCellView) -> None: ...
    def transform(self, xform: Transform) -> None: ...


class PyOADatabase:
    def __init__(self, lib_def_fname: str) -> None: ...
    def add_primitive_lib(self, lib_name: str) -> None: ...
    def add_yaml_path(self, lib_name: str, yaml_path: str) -> None: ...
    def create_lib(self, lib_name: str, lib_path: str, tech_lib: str) -> None: ...
    def get_cells_in_lib(self, lib_name: str) -> List[str]: ...
    def get_lib_path(self, lib_name: str) -> str: ...
    def implement_lay_list(self, lib_name: str, view: str, cv_list: Iterable[Tuple[str, PyLayCellView]]) -> None: ...
    def implement_sch_list(self, lib_name: str, sch_view: str, sym_view: str, cv_list: Iterable[Tuple[str, Tuple[PySchCellView, str]]]) -> None: ...
    def import_gds(self, gds_fname: str, lib_name: str, layer_map: str, obj_map: str, grid: PyRoutingGrid, colors: TrackColoring) -> None: ...
    def is_primitive_lib(self, lib_name: str) -> None: ...
    def read_library(self, lib_name: str, view_name: str) -> List[Tuple[str, str]]: ...
    def read_sch_recursive(self, lib_name: str, cell_name: str, view_name: str) -> List[Tuple[str, str]]: ...


class PyPath:
    def __init__(self) -> None: ...
    def commit(self) -> None: ...


class PyPolygon:
    def __init__(self) -> None: ...
    def commit(self) -> None: ...


class PyPolygon45:
    def __init__(self) -> None: ...
    def commit(self) -> None: ...


class PyPolygon90:
    def __init__(self) -> None: ...
    def commit(self) -> None: ...


class PyRect:
    def __init__(self) -> None: ...
    def commit(self) -> None: ...


class PyRoutingGrid:
    @property
    def bot_layer(self) -> int: ...
    @property
    def layout_unit(self) -> float: ...
    @property
    def resolution(self) -> float: ...
    @property
    def top_ignore_layer(self) -> int: ...
    @property
    def top_layer(self) -> int: ...
    @property
    def top_private_layer(self) -> int: ...
    @overload
    def __init__(self, tech: PyTech, fname: str) -> None: ...
    @overload
    def __init__(self, grid: PyRoutingGrid) -> None: ...
    def __eq__(self, other: PyRoutingGrid) -> bool: ...
    def __hash__(self) -> int: ...
    def coord_to_htr(self, layer_id: int, coord: int, round_mode: int, even: bool) -> int: ...
    def find_next_htr(self, layer_id: int, coord: int, ntr: int, round_mode: int, even: bool) -> int: ...
    def get_block_size(self, layer_id: int, include_private: bool = False, half_blk_x: bool = False, half_blk_y: bool = False) -> Tuple[int, int]: ...
    def get_copy_with(self, top_ignore_lay: int, top_private_lay: int, tr_specs: List[Tuple[int, int, int, int, int]]) -> PyRoutingGrid: ...
    def get_direction(self, lay_id: int) -> Orient2D: ...
    def get_line_end_sep_htr(self, lev_code: int, lay_id: int, ntr: int, adj_ntr: int) -> int: ...
    def get_line_end_space(self, lay_id: int, num_tr: int, even: bool = False) -> int: ...
    def get_min_cont_length(self, lay_id: int, num_tr: int) -> int: ...
    def get_min_space(self, lay_id: int, num_tr: int, same_color: bool = False, even: bool = False) -> int: ...
    def get_min_track_width(self, layer_id: int, idc: float = 0, iac_rms: float = 0, iac_peak: float = 0, length: int = -1, bot_ntr: int = 0, top_ntr: int = 0, dc_temp: int = -1000, rms_dt: int = -1000) -> int: ...
    def get_next_length(self, lay_id: int, num_tr: int, cur_len: int, even: bool = False) -> int: ...
    def get_prev_length(self, lay_id: int, num_tr: int, cur_len: int, even: bool = False) -> int: ...
    def get_sep_htr(self, lay_id: int, ntr1: int, ntr2: int, same_color: bool) -> int: ...
    def get_size_pitch(self, layer_id: int) -> Tuple[int, int]: ...
    def get_space(self, lay_id: int, num_tr: int, same_color: bool = False, even: bool = False) -> int: ...
    def get_track_coloring_at(self, tr_colors: TrackColoring, xform: Transform, child: PyRoutingGrid, top_layer: int) -> TrackColoring: ...
    def get_track_info(self, lay_id: int) -> TrackInfo: ...
    def get_track_offset(self, lay_id: int) -> int: ...
    def get_track_pitch(self, lay_id: int) -> int: ...
    def get_via_extensions(self, lev_code: int, lay_id: int, num_tr: int, adj_num_tr: int) -> Tuple[int, int]: ...
    def get_via_extensions_dim(self, lev_code: int, lay_id: int, dim: int, adj_dim: int) -> Tuple[int, int]: ...
    def get_via_extensions_dim_tr(self, lev_code: int, lay_id: int, dim: int, adj_num_tr: int) -> Tuple[int, int]: ...
    def get_wire_bounds_htr(self, layer_id: int, htr: int, ntr: int) -> Tuple[int, int]: ...
    def get_wire_em_specs(self, layer_id: int, num_tr: int, length: int = -1, vertical: bool = False, dc_temp: int = -1000, rms_dt: int = -1000) -> Tuple[float, float, float]: ...
    def get_wire_total_width(self, layer_id: int, ntr: int) -> int: ...
    def htr_to_coord(self, layer_id: int, htr: int) -> int: ...
    def size_defined(self, layer_id: int) -> bool: ...
    def transform_htr(self, layer_id: int, htr: int, xform: Transform) -> int: ...


class PySchCellView:
    @property
    def cell_name(self) -> str: ...
    @cell_name.setter
    def cell_name(self, val: str) -> None: ...
    @property
    def lib_name(self) -> str: ...
    @lib_name.setter
    def lib_name(self, val: str) -> None: ...
    @property
    def view_name(self) -> str: ...
    def __init__(self, yaml_fname: str, sym_view: str = '') -> None: ...
    def add_pin(self, new_name: str, term_type: int, sig_type: int, is_symbol: bool = False) -> None: ...
    def array_instance(self, old_name: str, dx: int, dy: int, name_conn_range: Iterable[Tuple[str, Iterable[Tuple[str, str]]]]) -> None: ...
    def clear_params(self) -> None: ...
    def get_copy(self) -> PySchCellView: ...
    def get_inst_ref(self, name: str) -> Optional[PySchInstRef]: ...
    def get_signal_type(self, term: str) -> SigType: ...
    def has_terminal(self, term: str) -> bool: ...
    def inst_refs(self) -> Iterator[Tuple[str, PySchInstRef]]: ...
    def remove_instance(self, name: str) -> bool: ...
    def remove_pin(self, name: str, is_symbol: bool = False) -> bool: ...
    def rename_instance(self, old_name: str, new_name: str) -> None: ...
    def rename_pin(self, old_name: str, new_name: str, is_symbol: bool = False) -> None: ...
    def set_param(self, name: str, val: Union[int, float, bool, str]) -> None: ...
    def set_pin_attribute(self, pin_name: str, key: str, val: str) -> None: ...
    def terminals(self) -> Iterator[Tuple[str, int]]: ...
    def to_yaml(self) -> str: ...


class PySchCellViewInfo:
    @property
    def cell_name(self) -> str: ...
    @property
    def lib_name(self) -> str: ...
    def __init__(self, yaml_fname: str) -> None: ...
    def to_file(self, yaml_fname: str) -> None: ...


class PySchInstRef:
    @property
    def cell_name(self) -> str: ...
    @cell_name.setter
    def cell_name(self, val: str) -> None: ...
    @property
    def height(self) -> int: ...
    @property
    def is_primitive(self) -> bool: ...
    @is_primitive.setter
    def is_primitive(self, val: bool) -> None: ...
    @property
    def lib_name(self) -> str: ...
    @lib_name.setter
    def lib_name(self, val: str) -> None: ...
    @property
    def width(self) -> int: ...
    def __init__(self, *args: Any, **kwargs: Any) -> Any: ...
    def check_connections(self, pin_iter: Iterable[str]) -> None: ...
    def get_connection(self, term_name: str) -> str: ...
    def set_param(self, name: str, val: Union[int, float, bool, str]) -> None: ...
    def update_connection(self, inst_name: str, term: str, net: str) -> None: ...
    def update_master(self, lib: str, cell: str, prim: bool, keep_connections: bool) -> None: ...


class PyTech:
    @property
    def bot_layer(self) -> int: ...
    @property
    def default_purpose(self) -> str: ...
    @property
    def layout_unit(self) -> float: ...
    @property
    def make_pin(self) -> bool: ...
    @property
    def pin_purpose(self) -> str: ...
    @property
    def resolution(self) -> float: ...
    @property
    def tech_lib(self) -> str: ...
    @property
    def use_track_coloring(self) -> bool: ...
    def __init__(self, tech_fname: str) -> None: ...
    def get_lay_purp_list(self, layer_id: int) -> List[Tuple[str, str]]: ...
    def get_layer_id(self, layer: str, purpose: str = '') -> Optional[int]: ...
    def get_metal_em_specs(self, layer: str, purpose: str, width: int, length: int = -1, vertical: bool = False, dc_temp: int = -1000, rms_dt: int = -1000) -> Tuple[float, float, float]: ...
    def get_min_line_end_space(self, layer: str, width: int, purpose: str = '', even: bool = False) -> int: ...
    def get_min_space(self, layer: str, width: int, purpose: str = '', same_color: bool = False, even: bool = False) -> int: ...
    def get_next_length(self, layer: str, purpose: str, tr_dir_code: int, width: int, cur_len: int, even: bool = False) -> int: ...
    def get_prev_length(self, layer: str, purpose: str, tr_dir_code: int, width: int, cur_len: int, even: bool = False) -> int: ...
    def get_via_em_specs(self, layer_dir: int, layer: str, purpose: str, adj_layer: str, adj_purpose: str, cut_w: int, cut_h: int, m_w: int = -1, m_l: int = -1, adj_m_w: int = -1, adj_m_l: int = -1, array: bool = False, dc_temp: int = -1000, rms_dt: int = -1000) -> Tuple[float, float, float]: ...
    def get_via_id(self, lev_code: int, lay: str, purp: str, adj_lay: str, adj_purp: str) -> str: ...
    def get_via_param(self, w: int, h: int, via_id: str, lev_code: int, ex_dir: int, adj_ex_dir: int, extend: bool) -> ViaParam: ...


class PyTrackID:
    @property
    def base_htr(self) -> int: ...
    @base_htr.setter
    def base_htr(self, val: int) -> None: ...
    @property
    def htr_pitch(self) -> int: ...
    @htr_pitch.setter
    def htr_pitch(self, val: int) -> None: ...
    @property
    def layer_id(self) -> int: ...
    @property
    def num(self) -> int: ...
    @property
    def width(self) -> int: ...
    def __init__(self, layer_id: int, htr: int, ntr: int, num: int, htr_pitch: int) -> None: ...
    def __eq__(self, other: PyTrackID) -> bool: ...
    def __hash__(self) -> int: ...
    def get_bounds(self, grid: PyRoutingGrid) -> Tuple[int, int]: ...


class PyVia:
    @property
    def bottom_box(self) -> BBox: ...
    @property
    def top_box(self) -> BBox: ...
    @property
    def via_cuts(self) -> List[BBox]: ...
    def __init__(self) -> None: ...
    def commit(self) -> None: ...


class RTree:
    @property
    def bound_box(self) -> BBox: ...
    def __init__(self) -> None: ...
    def __bool__(self) -> bool: ...
    def __getitem__(self, obj_id: int) -> object: ...
    def __iter__(self) -> Iterator[Tuple[BBox, int]]: ...
    def insert(self, obj: object, box: BBox) -> int: ...
    def intersect_iter(self, box: BBox) -> Iterator[Tuple[BBox, int]]: ...
    def overlap_iter(self, box: BBox) -> Iterator[Tuple[BBox, int]]: ...
    def pop(self, obj_id: int) -> object: ...


class TrackColoring:
    def __init__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __eq__(self, other: TrackColoring) -> bool: ...
    def __hash__(self) -> int: ...
    def get_htr_parity(self, level: int, htr: int) -> int: ...


class TrackInfo:
    @property
    def offset(self) -> int: ...
    @property
    def pitch(self) -> int: ...
    @property
    def space(self) -> int: ...
    @property
    def width(self) -> int: ...
    def __init__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __eq__(self, other: TrackInfo) -> bool: ...
    def __hash__(self) -> int: ...
    def compatible(self, other: TrackInfo) -> bool: ...


class Transform:
    @property
    def axis_scale(self) -> Tuple[int, int]: ...
    @property
    def flips_xy(self) -> bool: ...
    @property
    def location(self) -> Tuple[int, int]: ...
    @property
    def orient(self) -> Orientation: ...
    @property
    def x(self) -> int: ...
    @property
    def y(self) -> int: ...
    def __init__(self, dx: int = 0, dy: int = 0, mode: int = 0) -> None: ...
    def get_inverse(self) -> Transform: ...
    def get_move_by(self, dx: int = 0, dy: int = 0) -> Transform: ...
    def get_transform_by(self, xform: Transform) -> Transform: ...
    def invert(self) -> Transform: ...
    def move_by(self, dx: int = 0, dy: int = 0) -> Transform: ...
    def transform_by(self, xform: Transform) -> Transform: ...


class ViaParam:
    @property
    def cut_dim(self) -> Tuple[int, int]: ...
    @property
    def empty(self) -> bool: ...
    @property
    def nx(self) -> int: ...
    @property
    def ny(self) -> int: ...
    @property
    def priority(self) -> int: ...
    def __init__(self, vnx: int, vny: int, w: int, h: int, vspx: int, vspy: int, enc1l: int, enc1r: int, enc1t: int, enc1b: int, enc2l: int, enc2r: int, enc2t: int, enc2b: int, priority: int) -> None: ...
    def get_box(self, xform: Transform, level: int) -> BBox: ...


