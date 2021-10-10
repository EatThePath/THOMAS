# Texture Helper/Organizer: Move And reSave

A Miserable Pile Of Scrpts intended to help shuffle and process freespace open textures. Very unfinished, very crude, posted anyway.

Current structure:

* 00-mkdirs: Creates the directories that everything else needs
* 01-pullfromdds: converts all .dds files from a currently hard-coded source into tga files in ./01-oldtga-covert
* 02-decompose: Does nothing. Intended to split the textures in ./01 into component channels, undoing the FSO-specific composition of maps
* 03-stageforconvert: Takes textures in ./03-forconvert and places them in subfolders of ./04-sorted. Also renames certain forms of filename into the names FSO expects, with very specific-to-my-workflow particulars.
* 04-converttodds: Converts everything in ./04-sorted into bc7 files in ./05-gameready. These files are, as the name implies, theoreticly ready for direct placement into FSO.

These tools all assume you have AMD's compressonator tool in your path.