# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


def getTheClosestBoxIndex(bs_det, b_trk, max_spread=128):
    matched_det_index = -1
    spread_list = []

    if len(bs_det) > 0 and len(b_trk) == 4:
        for b_det in bs_det:
            max_spread = -1
            for i in range(0, 4):
                sub_spread = abs(b_trk[i] - b_det[i])
                if sub_spread > max_spread:
                    max_spread = sub_spread
            spread_list.append(max_spread)
        
        if len(spread_list) > 0:
            sml_spread = min(spread_list)
            if sml_spread <= max_spread:
                matched_det_index = spread_list.index(sml_spread)

    return matched_det_index


def matchDetTrkByXYXY(bs_xyxy_det, bs_xyxy_trk, ids_trk, max_spread=128):
    bs_det = bs_xyxy_det
    bs_trk = bs_xyxy_trk
    len_bs_trk = len(bs_xyxy_trk)
    len_ids_trk = len(ids_trk)

    if len_ids_trk != len_bs_trk:
        print("Track result is not valid!")
        return []
    
    match_ids = [-1 for i in bs_det]
    if len_bs_trk > 0:
        i = 0
        for b_trk in bs_trk:
            b_det_idex = getTheClosestBoxIndex(bs_det, b_trk, max_spread=max_spread)
            if b_det_idex >= 0:
                match_ids[b_det_idex] = int(ids_trk[i])
            i += 1

    return match_ids

def matchDetTrkByXYXYForSORT(bs_xyxy_det, sort_track, max_spread=128):
    bs_det = bs_xyxy_det
    bs_trk = sort_track.tolist()
    len_bs_trk = len(sort_track)
    
    match_ids = [-1 for i in bs_det]
    if len_bs_trk > 0:
        i = 0
        for b_trk in bs_trk:
            b_det_idex = getTheClosestBoxIndex(bs_det, b_trk[:-1], max_spread=max_spread)
            if b_det_idex >= 0:
                match_ids[b_det_idex] = int(b_trk[4])
            i += 1

    return match_ids
