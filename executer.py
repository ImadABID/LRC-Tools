import lrc

lrc.extract_data("lrc.lrc")
lrc.cut([0,0],[0,8])
lrc.exportdata("out.lrc")