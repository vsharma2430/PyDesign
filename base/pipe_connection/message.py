message_select_beams = lambda beam_nos : {"type": "staad_ui", "feature": "select", "payload": beam_nos}
message_lx = lambda lx :{"type": "ui", "feature": "lx", "payload": lx}
message_ly = lambda ly :{"type": "ui", "feature": "ly", "payload": ly}
message_lz = lambda lz :{"type": "ui", "feature": "lz", "payload": lz}
message_dj = lambda dj :{"type": "ui", "feature": "dj", "payload": dj}
message_main = lambda main :{"type": "ui", "feature": "main", "payload": main}
message_parameter_no = lambda parameter_no :{"type": "ui", "feature": "parameter", "payload": parameter_no}
message_apply = {"type": "command", "action": "apply_parameters"}