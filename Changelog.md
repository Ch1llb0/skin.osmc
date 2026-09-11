**Changes to the OSMC Skin**

---

**_v22.0.0_**

_New_
- add support for Kodi v22 (Piers)
- add support for Skin Shortcuts v3
- add Dolby Vision profile to the HDR media flag
- add extra title info, parental rating and backend name to PVR items
- add live bitrates, queue levels and subtitle decoder to the player process info dialog
- add spinner to the weather widget while it updates
- add last update time to the weather window
- add an option to show two widgets on screen at once
- add the ungroup button to the video versions manager
- add the controller image to the peripheral settings dialog
- add the PVR providers window, which lists the broadcasters behind the channels and recordings
- add an option to show titles on the artwork, in the wall views and on the home widgets, from the skin settings or from a media view's sub menu while a wall view is on screen

_Improved_
- allow stepping through subtitles in both directions in the video OSD
- open the subtitle settings from the subtitle name in the video OSD
- name audio and subtitle streams by their stream name in the video OSD and fullscreen info
- detect Dolby Atmos and DTS:X from the stream instead of the file name
- separate genres, directors and writers with commas
- hide duration based information during live playback
- consolidate codec and audio channel labels into shared lookup maps
- allow any item limit to be set for main menu widgets
- localise the artwork type names in the main menu widget artwork pickers
- offer every artwork type when picking main menu widget artwork, rather than only the ones the widget's content provides
- remove the always show settings link setting, as the settings item can no longer be taken off the main menu
- offer date sorting on live TV and radio widgets
- disable the delete and hide buttons on menu items that cannot be removed, and the restore button while nothing has been deleted
- give every group in the shortcut and widget pickers its own icon
- name the reset button in the skin settings for everything it clears, which is every menu and every view selection
- reduce the skin's textures to the channels they actually use, cutting the texture memory the skin holds on the graphics card by roughly two thirds
- carry the sort of every pre-configured widget into the widget management dialog, so it shows what the widget already does and a change starts from the truth
- sort the unwatched music videos widget by title, as the other unwatched widgets are, rather than at random
- drop the fifty item cap on the most played album and song playlists, leaving the item limit the widget's own to set
- place the line under a focused row with the control rather than with empty rows in its texture, so it stays sharp however the screen is scaled
- stop windows and dialogs drawing a full screen fanart layer while there is no fanart to draw
- clear the screen on the windows that fill it, rather than drawing each frame over the one before
- scroll every label at a speed set by its own font size rather than the single speed Kodi applies to all of them, so small text no longer races past and large text no longer crawls
- return to the sub menu when the view picker is left with back, rather than closing both at once
- offer the artwork titles setting, and the watched and listened to indicator settings, from a media view's own sub menu as well as from the skin settings, so a view can be adjusted without leaving it

_Fixed_
- fix audio channel labels claiming layouts a channel count cannot identify
- fix the recently added artists widget pointing at a playlist that does not exist
- fix the music add-on widget resolving to nothing
- fix the widget property pickers showing a crossed circle beside every option
- fix the live TV and radio widgets opening the videos window rather than their own
- fix the video watched status setting leaving movie sets untouched
- fix the rip disc row and the artist widgets pointing at artwork the skin does not ship
- fix video widgets falling back to music artwork
- fix the movie sets, music nodes and custom widgets carrying a type that does not describe their content
- fix the weather widget being recognised by a property Skin Shortcuts v3 never sets
- fix the seeded live TV and radio widgets differing from the ones the picker writes
- fix the three widget artwork slots drawing over one another
- fix the Skin Shortcuts entry points showing while the add-on is disabled
- fix the login screen scrollbar covering the profile list
- fix the profile settings scrollbar rendering without a track or a bar
- fix the watched status bar and its overlay swapping size in the video wall with small info
- fix the debug grid ignoring its offset on the masked aspect ratios
- fix widgets picked from the picker drawing icons on the poster layout whatever their content
- fix the games widget not offering the sort orders it lists add-ons for
- fix the random movie, TV show and album widgets being named one thing in the picker and another on the menu
- fix the widget management dialog offering no sort order for the pre-configured widgets, which were sorted all along
- fix the random movie and music video widgets sorting the opposite way round to every other random widget
- fix rows in the video and music OSD moving nowhere when the button they pointed at was not on screen
- fix left and right leaving the subtitle stream row in the video OSD instead of moving between its buttons
- fix the channel label in the fullscreen OSD and the channel guide dialog being blank
- fix the twelfth line of system information not being shown
- fix the last row of the game controller lists being cut through
- fix drop shadows on the home menu icons and the PVR timer icon, which the icon set does not use elsewhere
- fix the PVR providers list leaving the focused row unmarked, which every other list in the skin underlines
- fix the focused status badge in the music wall low view being mis-sized and mis-placed at 16:9, where a width was written as a left offset

---

**_v21.2.2 - March 2026_**

_Improved_
- add new item limits to main menu widgets
- improve rendering of video media flags all over the skin for edge cases
- improve debug overlay

_Fixed_
- fix the date added sort order of main menu widgets

---

**_v21.2.1 - August 2025_**

_Improved_
- change masking bars to allow fully transparent colour values

_Fixed_
- fix missing OSD icon for auto masking feaure
- fix custom masking colour setting
- fix versions/extras management dialog

---

**_v21.2.0 - March 2025_**

_New_
- add new views for images section
- add new colour picker slider dialog

_Improved_
- adjust video addon views to work with multiple content types (videos, episodes, movies)
- add fixed video addon views setting to side menu
- add XL font to plot/description text size setting

---

**_v21.1.0 - October 2024_**

_New_
- add new notification icon

_Improved_
- add skinshortcuts script as an optional dependency to avoid removal of the addon when marked as unused

_Fixed_
- fix widget onclick options to avoid errors when widgets are pointing to addon directories

---

**_v21.0.0 - August 2024_**

_New_
- support Omega skin engine features
- add new view type selection dialog

---

**_v20.2.1 - April 2024_**

_Improved_
- improve video info dialog button navigation when moving away from the cast list

_Fixed_
- fix select dialog icons
- fix dialog background fallback layers
- minor fixes before transition to v21

---

**_v20.2.0 - December 2023_**

_New_
- add new setting to adjust select action of album, TV show and movie set main menu widgets
- add consistent reminder icons for v20 PVR reminder feature
- add genre colours to TV/radio guide

_Improved_
- improve live TV and radio related localizes
- improve pre-playback behaviour of now playing information section in the top right corner of each window/dialog
- improve consistency between PVR windows and dialogs (feature parity as well as cosmetic appearance)
- improve media flags behaviour during window transitions and when encountering edge cases
- improve progress feedback of confirm dialog as well as the extended progress notification

_Fixed_
- fix focus cover animation in wide views
- fix media flags transition glitch
- fix radio button control text width
- fix behaviour when the correct view type or content type is not yet ready (especially related to addons loading new pages)

---

**_v20.1.0 - August 2023_**

_New_
- add composer info to fullscreen music playback window and music info dialog

_Improved_
- rework seek indicator and button behaviour

_Fixed_
- fix watched indicator background in wide and wall views
- fix episodes image to properly react to hide thumbs for unwatched episode setting

---

**_v20.0.0 - June 2023_**

_New_
- support Nexus skin engine features
- remove Skin Helper Service ColorPicker support
- add new video OSD audio and subtitle selection
- add missing PVR guide controls dialog
- use new OSMC specific video width and height info for media flags
- add new default widgets to movies, tv shows and music home screen items

_Improved_
- improve inital info dialog button focus behaviour

_Fixed_
- fix view type button supression behaviour in video media window while video addon force view setting is enabled

---

**_v19.1.4 - May 2023_**

_Improved_
- improve background overlay rendering
- improve media flags spacing and positioning
- improve rendering of all progress bar, scroll bar and slider controls
- improve non-focus fanart behaviour

_Fixed_
- fix seek slider mouse control

---

**_v19.1.3 - September 2022_**

_Improved_
- improve window draw performance
- rework home screen widget animation and heading/details behaviour

_Fixed_
- use proper localize for Player settings entry
- fix default (non-skinshortcuts) home menu widget headings

---

**_v19.1.2 - March 2022_**

_New_
- reset textboxes to top scrolling position during dialog or window switches

_Improved_
- improve inital window/dialog focus fix (only apply where needed)

_Fixed_
- always show OSD playlist button when expected

---

**_v19.1.1 - December 2021_**

_New_
- add new video/music OSD seek slider button functionality (also adds frame advance feature)
- add settings level button and settings description to addon settings dialog

_Improved_
- improve behaviour of OSD bookmarks dialog while other OSD dialogs are open (similar to previous OSD animation improvements)
- streamline addon settings and skinshortcuts customization dialogs

_Fixed_
- fix initial focus in all windows and dialogs

---

**_v19.1.0 - August 2021_**

_New_
- add ENABLE option for new skinshortcuts version
- add playback mode (shuffle and repeat) buttons to video OSD
- add comment tag line to music visualisation
- add new menu/OSD opacity/colour settings
- add new plain colour background overlay style option matching the new skin design

_Improved_
- improve background overlay colour management of new skin design
- streamline secondary information and widget detail labels
- improve weather widget
- add warning to add-ons currently not available from Kodi repo
- allow jumping from top to bottom of video playback settings dialog
- adjust list views to change depending on secondary label status
- improve settings window with new description and better list behaviour
- update translations
- handle movie set/collection indication more seamlessly
- improve dialog animations
- improve OSD animations
- change focus of info dialog button lists to extended info button

_Fixed_
- fix skinshortcuts management dialog
- add missing views to programs section for addons that set content type
- fix dialog select icons for movies and TV shows
- fix movie set information in media library views
- fix seek indicator

---

**_v19.0.0 - August 2021_**

_New_
- add new v19 features (music library, movie sets, PVR additions and chapter/EDL markers in video OSD)
- add channel sort by and sort order toggles to PVR guide side menu
- add artist, album and radio now/next/RDS information to fullscreen music/radio playback window
- add new info button to video and music OSD
- add trackt.tv ratings information to video info dialog
- add first WebLate translations
- new skin design

_Improved_
- rework look of default fullscreen music playback screen to match general skin look
- refine video fullscreen OSD and info dialog behaviour
- improve behaviour of weather widget when no weather information is available
- improve widget headings and general secondary label information
- improve localize consistency
- add missing custom colour settings
- improve skin setting select process for settings with a lot of options to choose from
- use translatable labels for skin setting options
- improve media flags positioning and edge case handling
- move My OSMC link from home menu to settings window

_Fixed_
- add missing "play recorded programme" button to PVR info dialog
- fix cut-off text of plot/description text boxes

---

**_v18.5.0 - November 2020_**

_Improved_
- add videos and music root directory to home menu entry and submenu customization dialog
- add picture and addon browser directory to home menu entry and submenu customization dialog

---

**_v18.4.0 - October 2020_**

_New_
- add channel group switching buttons to OSD PVR channels list
- add Library Node Editor support
- new square versions of existing views for video addons and music
- add automatic masking for scope skin version
- add second dialog page to music, PVR and addon info dialog
- add setting to force a specific view for video addons
- add missing PVR seek slider

_Improved_
- improve wording in skin settings
- improve watched/listened to indicator for all views/widgets
- adjust media window view positioning and size
- adjust wall and wide view for music
- improve spacing of wall low view
- improve PVR descriptions
- rework now playing information and fullscreen music playback information
- add missing detail labels to PVR and music info dialogs
- show TV show episode thumb in video info dialog
- use the more extended list view for more content types (addons, games, files and pictures)
- improve second label of more extended list view
- add wide view support to games and programs
- harmonize non-focus animations
- improve scrollbar size relative to their controls
- add favourites to home menu entry/submenu and widget customization dialog

_Fixed_
- fix default view music and video navigation
- fix PVR channels window heading label
- fix widget icon fallback
- fix PVR OSD dialogs

---

**_v18.3.0 - May 2020_**

_New_
- add standard Kodi 'Menu' key functionality to access side menu in all windows
- add new Wide low info view
- add support for Up Next addon
- add playlist button to video OSD
- add 3D depth information to GUI elements
- add new widget layouts (square and square small)
- add new 2.33:1 scope masking option

_Improved_
- make Wide low view accessible for music views
- make disabled text colour more readable
- improve widget details and window headings
- improve debug overlay
- improve overall handling of music videos
- improve playlist window
- add missing scrollbars
- rework most dialogs for consistency
- improve widget positioning and widget icon size
- improve skinshortcuts management dialog
- improve video info dialog button behaviour
- remove unnecessary song and picture list view

_Fixed_
- fix settings button labels for 21:9 and 4:3 modes
- fix music playlist editor window
- fix side menu return button behaviour
- fix edge alignment of dialogs and windows
- fix watched/listened to status for a play count higher than 1

---

**_v18.2.0 - March 2020_**

_New_
- add new pre-defined widgets
- add setting to change whether video info dialog shows details or plot first
- add setting to set a solid colour instead of background images
- add audio and subtitle language information to media flags
- add setting to toggle media flags information shown (first)
- add new seek indicator to audio and video player
- add new scope version
- add new scrolling label
- add new never hide music information during playback setting
- add skin settings explanations
- add setting to hide item count

_Improved_
- rework home menu customization dialogs
- improve sort by and sort order toggles
- improve video info dialog (animations and buttons)
- improve alignment and positioning of item count and media flags
- show view toggle only when more than one view is available
- improve info dialogs (more information/layout with video and addon info dialogs)
- update Artist Slideshow integration (v3 update)
- improve OSD animations
- show item count with empty containers
- improve music player during radio playback
- improve visible window elements when busy dialog is active
- let live TV and radio OSD listen to Kodi OSD settings

_Fixed_
- move hide scrollbars setting to skin settings window
- hide MyOSMC home menu entry and widget on non-OSMC systems
- fix overlapping in views with big horizontal titles
- add scrollbar to music album info dialog (if details list is too long)
- fix now playing dialog for radio and live TV playback
- fix kiosk mode behaviour

---

**_v18.1.0 - November 2019_**

_New_
- add 21:9 and 4:3 modes
- add option to show lock icon for encrypted PVR channels (show encrypted channel icons by default)

_Improved_
- use OSMC busy spinner for widget loading
- add Disabled option to Adjust OSD on-time during video pause button
- rework skin structure for Transifex localization
- improve widget icon animations
- rework dialog animations to prevent bright transition

_Fixed_
- don't show parts of weather widget during widget loading
- localize all labels

---

**_v18.0.1 - October 2019_**

_New_
- add new video player OSD settings (show OSD after beginning of playback and before end of playback)
- add new second video info dialog screen (with extended rating, audio and subtitle information and bigger plot text box)
- add new wall info view (based on wall view)
- add new adjust representation of video duration setting
- add new multi-image (folder) background option
- add new individual background option for home menu entries
- add new options for music OSD to automatically show
- add user rating to music and video library
- add new side-menu player controls
- add new options to hide watched indicator in video library and listened to indicator in music library

_Improved_
- add audio information to video info dialog
- use font type for bold, light and italic instead of label formatting (where possible)
- prevent stacking of window/dialog text during background video playback
- show special watched indicator icons for videos watched more than once
- add listened to indicator for music

_Fixed_
- only offer rip CD feature when an audio CD is present

---

**_v18.0.0 - May 2019_**

_New_
- add new subtitle selection to match v18 requirements
- add new games section to match v18 requirements
- add new resolution select button/dialog in video player
- add player icon to now playing dialog
- add new dependency button in addon info dialog to match v18 requirements
- new colour options (colour sets, background gradients, adjustable opacity)
- add PVR channel number input dialog
- add PVR timeshift status dialog
- add welcome dialog on non-OSMC devices
- add director button to video info dialog
- add new views (wide low, wall small, wall low, wall info, list info)
- add new sub-menu indicator icon
- add "Random TV shows" widget as new standard for TV shows home menu entry
- add new dialog navigation indicators
- add ratings toggle for IMDb, Metacritic, Rotten Tomatoes and TVDb
- add new video player OSD settings (show OSD after beginning of playback and before end of playback)

_Improved_
- adjust syntax, values, labels and infobools to match v18 requirements
- adjust PVR section to match v18 requirements
- highlighting colour now adjusts according to text color
- streamline OSD animations
- add missing adjustable plot fonts
- let favourites dialog behave like a normal window
- add file path and name to refresh button in video info dialog
- add song/album year to music player
- add wide list as music view
- add music OSD album art size switch
- adjust widget headings to always show and adjust animations to match widget animations
- add option to change widget labels

_Fixed_
- show proper game widget title when not using skinshortcuts script
- highlighting is now more consistent
- fix current position/time remaining and current time/end time for PVR playback
- hide deprecated previous/next channel buttons in PVR playback OSD
- fix background of subtitle settings window
- fix layout of PVR playback dialogs
- fix dialog list navigation
- change font size of media tags to prevent overlap with titles/details
- only offer rip CD feature when an audio CD is present

---

**_v17.0.5 - June 2018_**

_New_
- add option to adjust dim factor of unfocused art 
- add option for additional text highlight
- add channel icon to PVR info dialog
- add new widget options (through skin.helper.widgets script)
- add AURO media flags (based on file naming)
- add new cover art highlighting (size change depending on focused state)
- add new movie collection indicator

_Improved_
- add more weather information to weather window
- refine music icons
- remove watched status for music items (in views and widgets)
- adjust representation of object based audio codec tags
- refine positioning and scaling of media tag icons
- adjust viewtype 55 for music and add-ons to match viewtype 53 for movies and TV shows
- improve highlight colour of selected text
- change appearance of all progress icons to round shape
- add no dimming of cover art
- dim watched and collection indicator depending on cover dimming setting
- update watched overlay icon to match appearance of new movie collection indicator
- add current control ID to debug overlay
- change overlay colour setting to match appearance of background colour setting

_Fixed_
- fix scrollbar in music navigation
- fix item widths in various windows
- fix weather window
- fix focused items in addon list view (e.g. YouTube)
- fix PVR views to add scrolling and adapt season/episode representation
- fix widget details label for PVR items (when using skinshortcuts script)
- fix scrollbar in file browser

---

**_v17.0.4 - March 2018_**

_New_
- music track duration added to music info dialog
- 3D label shown under media flags now (after first playback and/or if named according to Kodi wiki)
- Atmos/DTS:X label shown under media flags now (if named according to Kodi wiki)
- show codec information in music “now playing” window
- show current audio/subtitle stream in info dialog during full screen video playback
- add file size label next to duration label in file view
- add adjustable font sizes/styles to plot/description texts (addon info, music info, full screen info, PVR info and video info dialog) – font sizes 27 (S), 30 (M), 33 (L) and 36 (XL) available in normal and light
- add option to show date above system time
- add option to adjust OSD on-time during video pause
- add option to hide thumbnail art of unwatched TV show episodes

_Improved_
- show resolution with “p”-suffix (global)
- show 4K resolution as 2160p (global)
- adjust playback time and finish time in “now playing” dialog to match representation in full screen video playback window
- show media flags in a two-line textbox
- translate video/audio codecs in media flags to more understandable labels
- add scrolling of long titles in “now playing” window for music
- add scrolling of long album titles/artist tags in music list view
- show more specific channel layout information (2.0, 5.1, 7.1, etc.)
- replace “Aired on” in details of TV show episodes (in list view) by translatable “First air date”
- adjust representation of season/episode titles to one syntax everywhere: S01E01
- replace "Loading…" upon widget loading at startup of mediacenter by translatable "Please wait…"
- add cycling of controls highlight in context menu

_Fixed_
- window heading and system clock moved slightly down and reduced width of “now playing” dialog to avoid overlaps
- adjust height of plot textbox in list view to avoid overlap with new media flag representation
- use titles when available instead of item labels
- recognize TV show specials and show them correctly (no season, just episode S1)
- adjust width of scrolling titles in wall view and wide list view to avoid overlap with new media flags
- “now playing” dialog now shows album/artist tags correctly even when one of them or both are not present in the currently playing music file
- fix custom background colour option
- bring back current playlist button in music OSD functionality

---

**_v17.0.3 - July 2017_**

---

**_v17.0.2 - March 2017_**

---

**_v17.0.1 - March 2017_**

---

**_v16.9.3 - January 2017_**

---

**_v16.9.2 - November 2016_**

Fix crash in PVR guide window; Font updates

---

**_v16.9.1 - November 2016_**

Library image fixes and now playing information

---

**_v16.9.0 - September 2016_**

Release

---

**Changelog v22.0.0**

strings.po:
- add string for unnamed audio channel counts (31444)
- add string for the player process info queue levels (31445)
- add string for the parental rating of PVR items (31446)
- adjust the widget item limit description text for the free-form number, saying that zero shows every available item (31375)
- reword the reset button to name everything it clears, as it removes every menu and every view selection rather than only the main menu items (31399)
- add string for the two widgets on screen setting (31447)
- add string describing what the two widgets on screen setting does (31448)
- add string for the artwork titles setting (31449)

backgrounds.xml:
- add the background list, splitting the v2 browse behaviour into the two v3 types the skin renders: browse for a single image, multi for a folder
- note that the type reaches the skin as backgroundType, which is what selects the renderer

menus.xml:
- add the menu structure: a menu for the main menu, a submenu per menu item, and a "<name>.widgets" submenu per widget list
- open a widget list through a subdialog on the manage widgets button, which is how v3 edits a second menu
- spell out the shortcut picker in groupings, as v3 owns no built-in shortcut list, and give the dynamic sources it used to resolve internally explicit content elements
- declare the visibility conditions v2's builder inferred from an item's action, as v3 emits only what the skin declares
- write out each seeded widget's path, type, target and artwork beside its name, as v3 derives those from the name only for items that carry no widget label yet
- bind the settings submenu to its menu item, which v2's baked output carried but the declaration had lost
- protect the settings item with required="true", replacing the v2 checkforshortcut probe and its always show settings link toggle
- seed the add-ons widget with source="addon", which is what the picker writes, so the seeded row and a picked one agree
- give the seeded live TV and radio widgets the names and icons of the picker widgets they duplicate, and target their own PVR windows rather than the videos window
- give the custom-typed widgets types that describe their content, so the sort options and fallback artwork match what they list
- point the rip disc row at an icon the skin ships
- scope the additional items group to the main menu, as the other menus have no use for it
- bake each PVR shortcut's availability into the item, rather than leaving the picker to infer it
- drop the content labels that only restate the group above them, and wrap dynamic picker content in a folder through the built-in attribute
- drop the HasAddon conjunct that AddonIsEnabled already implies
- give every group in the shortcut picker its own icon, as an unset group falls back to a plain folder
- drop the layout and artwork the seeded widgets spelled out, which the type keyed defaults now resolve to the same values, so the seeds no longer freeze a default that has moved on
- seed the sort of the five widgets whose definitions declare one and whose rows did not, as the add-on re-derives a widget's path, type and target on every build but never its sort

overrides.xml:
- remove the v2 groupings, widgets, backgrounds and property options, carried into menus.xml, widgets.xml, backgrounds.xml and properties.xml

properties.xml:
- add the widget property buttons mapped to their properties, which is how v3 opens a picker, stores the value and resolves its label
- give sort order, sort direction and item limit real button ids (502, 503, 504) instead of sharing one hidden control through a chooseProperty window property
- give the item limit v3's numeric type, so any limit can be set
- move the artwork options to the skin's own strings, as v2 listed them in English in the picker while the button underneath showed the localized name
- key the add-on sort options off widgetSource and the user rating option off the normalized "videos" target, neither of which the v2 conditions matched
- rename widgetSortDirection to v3's own widgetSortOrder through an overrides block, which moves the key on menus users have already saved
- restore requires="widget" on the item limit, so it is offered only where there is a widget to limit
- offer date sorting on live TV and radio widgets, which Kodi uses for timers and recordings
- match the PVR sort options to the types the picker actually produces
- drop showNone where true is already the default
- declare submenuPath templateonly, keeping a property the skin never reads out of the generated includes
- turn the icon column off on the five option pickers, as an option with no icon of its own is given a crossed circle
- key the layout and artwork defaults on the widget's type, so a picked widget takes the shape its content calls for rather than the poster layout with an icon
- note why those two need a default at all: neither has a home in a widget definition, so the picker never writes them and only the widgets the menu seeds carried them
- offer year for songs and playcount for albums and songs, the sorts the recently released and most played widgets of those types are ordered by and could not otherwise have shown
- offer top250 for movies under Kodi's own 13409, which is the label Kodi gives that sort method itself, so the Top 250 widget can say what it is ordered by

template.xml:
- remove the v2 widget templates, carried into templates.xml

templates.xml:
- carry the title font, scroll speed and spacing in the layout presets, beside the strip height and slide they belong with
- pass them at all eight overlay bar call sites, four single row and four two row
- add the widget templates in the v3 template language, keeping the generated controls unchanged so the widgets render as before
- address the main menu item and the widget as $PARENT[index] and $PROPERTY[index], replacing the v2 auto-rootID and id pair
- let v3 skip a template for any item with no widgets, rather than gating on a property no template condition can see
- replace $PYTHON with $MATH for the image geometry and with variables for the artwork selection
- collapse the six parallel layout property lists into one widgetLayout preset with a row per layout, and the four conditional layout includes into one include whose name interpolates the layout
- round the overlay bar's height and slide to the whole pixels v2 emitted, as $MATH keeps the fraction
- show the widget reloading spinner while the weather widget updates
- write the spinner's per menu item gate out explicitly, as the v2 marker that carried it only resolves in a menu template
- key the weather widget off its path, as the property v2 set for it is one v3 never writes
- compose the TV show, episode and PVR detail lines from fragment variables, taking the variables block from 26,058 characters to 8,535 and the longest line from 1,282 to 481
- hoist the widget container and focus tests into template properties, so each is written once rather than at every use
- move the widget overlay bar into a shared include, replacing four identical forty-two line blocks per widget with four calls
- make the three artwork slots mutually exclusive, so the primary, fallback and catch-all images no longer draw over one another
- default the shared artwork include's parameters instead of passing the same values at every call
- split the window background out of the per-widget variable, and isWeather out of the artwork property group
- use v3's sets type for the movie sets widget and the visibility marker where the template wrote the condition out by hand
- spell the emptiness test the way Kodi understands it
- indent the propertyGroup values under their parent
- emit a second layout per widget for the two row view, chosen at runtime by the setting, so both are always built and only an expression decides which is drawn
- give the selector items both pages they could sit on beside their widgetID, so a widget's page is arithmetic on its index rather than something stored, and the pair sharing a page is drawn together
- add the two buttons that turn the page under the shared widget of an odd numbered set without moving the selection, and have the movement buttons record which way they went
- add the widgetLayoutTwoRow preset, each layout carrying the stride that closes the gap under its own details block and art that is the same fraction of the art it has in the single widget view, so the four keep their sizes relative to one another
- sit the two row art in its slot through rowImageLeft, moving it right of centre where the box's leftover past its last whole slot would otherwise show a sliver of the next poster
- turn the two row focus zoom about the art's centre, as the art is neither the width of its slot nor centred in it
- draw each widget's own name below it and the detail text of its focused item, dropping both the moment focus leaves so neither flashes the next widget's item on the way out
- leave the weather widget on the single layout, marking it with a hidden label the two row tests read, as its hand placed internals cannot share a row

widgets.xml:
- add the widget list, giving every widget a unique name, as v3 looks a widget up by name to re-derive its path, type and target on every build
- resolve the four add-on categories through content source="addons" rather than restating their paths, which also offers the category root itself as an entry
- drop the install and enable rows for Skin Helper Service and ExtendedInfo, as v3 has no equivalent of the ::INSTALL:: and ::ENABLE:: markers, and the upnp sources, which have no v3 source
- point the recently added artists widget at extras/playlists/artists_recentlyadded.xsp, replacing a misplaced "s" that named a directory and a file that do not exist
- point the fourteen PVR widgets at the windows their paths belong to, as there is no pvr window to activate
- give the movie sets, music nodes and custom-typed widgets types that describe what they list
- stop using music icons on video widgets, and give the artist widgets a fallback texture the skin ships
- carry the seeded sort defaults on the widgets that define them
- give every group its own icon, as an unset group falls back to a plain folder
- spell the video target the way the rest of the configuration does
- drop the content labels that only restate their group, and wrap dynamic content in a folder through the built-in attribute
- drop the HasAddon conjunct that AddonIsEnabled already implies
- give the games widget the add-on source it lists add-ons through, so it offers the last used, install date and last updated sort orders the program add-ons widget already does
- label the random movie, TV show and album widgets with the strings the menu seeds use, so one widget carries one name; 31181, 31192 and 31211 held a title cased duplicate of each
- declare the sort of the fifty-three widgets whose order is knowable: thirty-one from the bundled playlist each points at, copied from its own <order>, and twenty-two from Kodi, whose PVR recording and timer defaults are read from its view states and whose remaining paths name their own order
- leave the eleven undeclared where a sort would reorder a list the user arranged: the node lists, the game sources, the channel groups, favourites, the two browse-into entry points and the two widgets whose path is an include rather than a directory
- sort the game and program add-on widgets by last used, as an add-on list is most useful with what was opened last at the front

movies_random.xsp and four other playlists:
- order the random movie and music video playlists ascending, as the six other random playlists are; the direction means nothing to a random sort, but the dialog shows it
- order the unwatched music videos playlist by title, matching the other unwatched playlists, rather than at random
- drop the fifty item limit from the most played album and song playlists; a limit applies after the order, so it left the order deciding which rows appear rather than only their order, and both already exclude anything unplayed

mainmenu.DATA.xml and the seventeen other seed files:
- remove the v2 seed files, carried into menus.xml

script-skinshortcuts-static.xml:
- pass the same title metrics at all eighty overlay bar call sites, so the fallback the skin falls back to matches what the template builds
- show the widget reloading spinner while the weather widget updates
- separate genres with commas in the widget details
- rebuild the no-addon fallback from a v3 build of this skin's own configuration, replacing the v2 build it still carried
- rebuild it against Skin Shortcuts 3.0.3 from a clean profile, taking it from 5,328 lines and 439 KB to 4,008 and 257 KB
- store it with unix line endings, which is what the add-on writes
- rebuild it again for the two row view, so it reaches the users the file exists for
- rebuild it once more for the seeded sorts, which reach the generated content elements of the five widgets that gained one

script-skinshortcuts.xml:
- draw the fanart layer only when the item has fanart, and drop the transparent fallback behind it
- tell the three editing contexts apart by menuname, which always holds the menu being edited, where skinshortcuts-menutype is only set for menus the configuration declares
- follow the v3 control ids: the widget picker moves 312 -> 309, restore moves 308 -> 311, and the hidden 404 property button goes along with the SetProperty(chooseProperty) calls that drove it
- rename a widget by clicking 305, whose v3 handler writes the widget label, so the rename no longer needs script.skin.helper.service
- treat a stored widget path as proof that a widget is configured, as the seeded add-on and PVR widgets carry a path but no name
- read the label the script has already resolved for the widget rows and for the heading above the widget buttons, as Kodi does not evaluate a $LOCALIZE inside a property value
- remove the hidden container that loaded a widget to offer only the art types it has, as v3 evaluates option conditions against an item's stored properties
- disable delete and hide on items the configuration protects, and restore while nothing has been deleted
- read backgroundType rather than guessing the renderer from the stored path
- merge the mirrored heading labels into one, and drop the SendClick proxy the change label button routed through
- name where each control id comes from, as the same numbers mean different things in this window and in the settings
- drop the orphan id from the dialog fanart image

AddonBrowser.xml:
- build with type=buildxml, as v3 takes the menu from the configuration rather than from arguments
- gate the entry point on the add-on being enabled

Coordinates_DialogGameControllers.xml:
- give the group title the height of every other row and make both lists ten whole rows, as a list 654 high could not divide into rows of 66 and 42 and cut the bottom one wherever the sum happened to land

Coordinates_DialogPlayerProcessInfo.xml:
- grow the info panel by two rows and move the debug overlay shortcut down accordingly

Coordinates_DialogSeekBar.xml:
- remove the file, as every family in it was an unreferenced 0x0 stub and DialogSeekBar.xml holds no coordinates include at all

Coordinates_DialogSelect.xml:
- remove the video version picker layouts, as Kodi v22 removed those windows

Coordinates_DialogSettings.xml:
- add the controller image coordinates in the column left of the settings list, and move the OSD variant's coordinates up by one to keep them in order of appearance

Coordinates_DialogVideoManager.xml:
- hide the item sublabel under the generic select dialog, which stacks over the manager in Kodi v22

Coordinates_Includes_Widgets.xml:
- add the two row details top, one number for all four layouts, as each lands its poster bottom twelve pixels above it and the lower row is the same block slid down
- add the widget arrow coordinates, at the home menu list's own height against the opposite margin
- give each widget box a second set of right alignment offsets for the two row slot, taken by a tworow parameter the weather slide never passes
- size every widget box to a whole number of slots in both layouts, as Kodi pages by the whole slots a box holds; 4:3 wide moves to a 640 box at 680, as square already was, which also ends the sliver of a third poster its 720 box has always shown

Coordinates_LoginScreen.xml:
- give the scrollbar its own LoginScreen_coords6 family, as its geometry was declared under the name the profile list already used and Kodi keeps only the first definition

Coordinates_MyPVRProviders.xml:
- add the provider list, its layouts and its scrollbar, taking the geometry of the timers list so the PVR windows stay of a piece
- underline the focused row, as the timers list the layout was taken from does
- draw each row's icon from the item itself, which is a provider logo at the top level and a channel or recording icon below it

Coordinates_MyPVRRecordings.xml:
- read the watched state from the named expression rather than repeating it at twenty-four sites

Coordinates_VideoOSD.xml:
- widen the subtitle name to fill the reworked subtitle stream row

Coordinates_Viewtype538.xml:
- pass the watched status bar and its overlay in the order MediaViewImageNF reads them, matching Viewtype536

Coordinates_Viewtype53.xml, Coordinates_Viewtype531.xml, Coordinates_Viewtype532.xml, Coordinates_Viewtype533.xml, Coordinates_Viewtype534.xml, Coordinates_Viewtype535.xml, Coordinates_Viewtype536.xml, Coordinates_Viewtype537.xml, Coordinates_Viewtype538.xml, Coordinates_Viewtype539.xml:
- hand the title strip the size of the strip the view already draws, once for the item layout and once for the focused one, so the title and its strip grow with the artwork as the focus animation runs
- call the strip from all eight layouts of each view, after the artwork, and inside the group the focus zoom is on, so it is carried by that animation rather than snapping to the focused size beside it
- give the focused badge in the music wall low view a width, which was written as a left offset on the 16:9 variant alone

Coordinates_script-skinshortcuts.xml:
- collapse the arrow mirror pairs into one control each, keyed on the button rather than on the list item

Coordinates_*.xml:
- place the focus line by the control: three pixels tall, eight pixels above the bottom of the row, rather than a texture as tall as the row with the line drawn into it and every other row left empty; 208 layouts across 32 files
- resolve the twenty-eight centred focus lines to an explicit top, as a three pixel control cannot be centred where a full height one was

Custom_Debug_Grid.xml:
- include the coordinates under the name they are defined with, restoring the offset the masked aspect ratios apply

DialogMusicInfo.xml:
- separate genres with commas

DialogPVRChannelGuide.xml:
- read the channel from the guide container, which is where the dialog's other labels read theirs, filling the heading on radio channels as well

DialogPVRInfo.xml:
- add extra title info above the plot
- add the parental rating to the end of the plot
- add the backend name to the channel row in multi client setups
- separate genres with commas

DialogPlayerProcessInfo.xml:
- add the live bitrate to the video and audio rows
- add a subtitle decoder row
- add a queue level row

DialogVideoInfo.xml:
- separate genres, directors and writers with commas

DialogVideoManager.xml:
- add the ungroup button, which returns a version to the library as a standalone movie; versions only, as it has no effect on extras

Every file with a scrolling label:
- set a scroll speed from the font, at the rate the skin already scrolled its largest one, which works out at about one and three quarter times the font size a second; Font36 is left alone, as Kodi's own default already matches it, and the three wall fadelabels that scrolled at the largest font's speed come down to their own

Font.xml:
- add six sizes below Font25, one per strip height the wall views and the home widgets use, so a title fits the strip it is in rather than the strip growing to fit the title

Home.xml:
- build with type=buildxml, as v3 takes the menu from the configuration rather than from arguments
- gate the entry point on the add-on being enabled

Includes.xml:
- pull in Includes_Maps.xml
- load the generated includes only while the add-on is enabled, and the static fallback otherwise, as a disabled add-on leaves its last build behind
- point at the regeneration notes for the fallback in the repository documentation
- pull in Coordinates_MyPVRProviders.xml
- stop loading Coordinates_DialogSeekBar.xml, which is removed

Includes_DialogSettings.xml:
- draw the controller being configured beside the settings, which the peripheral settings dialog fills through control 100

Includes_Home.xml:
- read the home submenu from skinshortcuts-mainmenu-submenu, as v3 names a menu's submenu include after that menu
- drop the settings fallback item, now that the settings item cannot be taken off the main menu

Includes_Maps.xml:
- add AudioCodecMap, AudioChannelsMap and VideoCodecMap as shared value to label maps
- add the immersive and profile codec values Kodi v22 reports e.g. Dolby Atmos and DTS:X
- label ambiguous channel counts with every layout they may represent, as a channel count cannot identify one

Includes_SubMenu.xml:
- offer the artwork titles setting in the seven sub menus that carry a view button, shown while a wall view is on screen
- offer the watched status setting in the video sub menu and the listened to status setting in the music one, beside it, as both change what a view draws over its artwork
- send back from the view picker to the sub menu it was opened from rather than out to the list, which closed both
- drop the HasAddon conjunct that AddonIsEnabled already implies
- add the provider window's sub menu, listing the other PVR sections as every PVR window does; nothing points into providers, which is reached from the TV and radio listings

Includes_Time_NowPlaying.xml:
- hide duration based information during live playback

Includes_Widgets.xml:
- carry the title in the widget overlay bar, which is the same strip over the same artwork the wall views draw, with the badges slid to the right hand end to make room
- take the title metrics as parameters, so each widget layout hands over the size of the strip it already draws
- add widgetOverlayBar, holding the status bar the widget templates repeated four times per widget
- draw each widget texture once, removing the second byte-identical image control in widget-image
- default the shared artwork include's parameters
- remove the widget includes the v3 rewrite orphaned, and the long dead favourites widget include
- take the window background over from the per-widget variable, reading it back through a hidden label as Kodi cannot test a variable for emptiness
- add widgetIndicators, the home menu's own arrows at its own height mirrored to the right of the screen, drawn for the widget that holds focus, and drop the two arrow buttons from the heading row those replace
- send up and down at the shared widget of an odd numbered set to the paging buttons, defaulting the menu name so a fallback built before this never takes that branch
- select the fading widget by page rather than by widget when two are on screen, keeping the effects and timings that move between single widgets
- hold the one widget details text to the three whole rows of its font the longest of it runs to, rather than letting the box grow to whatever it needs

Includes_Windows_Dialogs.xml:
- add MediaViewTitleStripNF and MediaViewTitleStripFO, which draw the title over the bottom of the artwork with the status badge to its right, taking their geometry as numbers so each view can hand over the strip size it already has
- scroll the focused title at the pace the skin scrolls everything else, which is about one and three quarter times the font size a second, rather than the flat sixty pixels a second Kodi falls back to
- stand the status strip down in the views the title strip serves, as the two occupy the same place
- draw the window and dialog fanart layers only when there is fanart to draw, and drop the transparent fallback that kept them covering the screen the rest of the time
- read the home background from backgroundPath, which is where v3 stores the path
- read the watched state from the named expressions rather than spelling it out

LoginScreen.xml:
- point the scrollbar at LoginScreen_coords6

MusicOSD.xml:
- name the button row so the option row moves to whichever of its buttons is on screen, rather than to a channel up button that only exists on radio
- send the seek slider to it as well, as it named a play button that is not built when the player cannot pause

MusicVisualisation.xml:
- hide end time, position, progress and cache bar during live playback
- separate genres with commas

MyPVRGuide.xml:
- add extra title info to the episode name fadelabel
- separate genres with commas

MyPVRProviders.xml:
- add the window Kodi has had since the provider browser landed and the skin never drew, so the entry in the TV and radio listings opens something
- read the provider name core writes into control 29 through a hidden label, as the other PVR windows do for their group name

MyWeather.xml:
- add the last update time to the provider label
- drop the spinner's coordinates include, which named a family that does not exist; DialogBusy renders the same spinner without one

SettingsCategory.xml:
- build with type=buildxml, as v3 takes the menu from the configuration rather than from arguments
- gate the entry point on the add-on being enabled

SettingsProfile.xml:
- style the scrollbar through the BackgroundOverlayStyleScrollbarVertical include, as the two textures were read as variables and resolved to empty paths, leaving the scrollbar with no track and no bar

SettingsSystemInfo.xml:
- add the twelfth information line, which the window has offered since a core change and the skin never drew

SkinSettings.xml:
- add the artwork titles setting, beside the other library display toggles
- build with type=buildxml and manage with type=manage,menu=mainmenu, as v3 takes the menu from the configuration rather than from arguments
- remove the always show settings link setting
- gate the entry points on the add-on being enabled, and drop the HasAddon conjunct that implies
- reword the reset button for everything it clears
- add the two widgets on screen setting, reloading the skin so the layout conditions are read again and putting focus back on the row

Startup.xml:
- drop the HideSettings reset, as nothing has read that setting since 2019

Variables.xml:
- name the pair of conditions that decide whether an item shows a status badge, which four controls repeated between them
- name the condition for a wall view being on screen, which is where the ten wall views are listed, and read the title setting against it
- name the widget badge condition, reminders included, so a title makes room for a badge the strip itself does not draw behind
- replace the fourteen focus variables, one per row height, with focusline and focuslinecenter, as the control now places the line
- reduce the codec and channel variables to map lookups, keeping the DSD sample rate rows
- name the watched state, the partially watched series and the per media kind setting gate as expressions, replacing the same test spelled out at forty-three sites across four files
- add movie sets to the video types the watched status setting covers, which every other list in the skin already included
- name the widget-editable condition the management dialog repeats, and the three Skin Shortcuts menu kinds
- keep file name detection for AURO-3D and DTS:X on DTS-HD HRA, which the stream cannot reveal
- add the Dolby Vision profile to the HDR media flag via HdrDetail
- name audio and subtitle streams by their stream name, falling back to the English language name and then the legacy code
- add extra title info, parental rating and, in multi client setups, the backend name to the PVR description variables
- add a plain elapsed time row for live playback
- separate genres, directors and writers with commas
- name the two widgets on screen setting as the TwoRowWidgets expression, which is what every two row test and layout condition reads
- add the channel label variables the fullscreen OSD and the guide dialog have called since 2023 without them existing, split per site as the dialog reads its channel from the guide container
- name the provider window's heading, breadcrumb and secondary column

Variables_Settings.xml:
- follow the renamed window property and the moved control ids in the dialog help texts
- remove the help texts for the always show settings link setting
- give the widget list's restore button its own help string; 31383 was written for it and 31385, describing the main menu, was used by mistake
- follow the merged heading label and the dropped SendClick proxy
- read the menu kind from the named expressions
- add the help text for the two widgets on screen setting

Variables_Skinshortcuts.xml:
- drop the five lookup variables that mapped a stored value back to its localized string, now that the script publishes a resolved label per property
- read the resolved label in the widget list, falling back to the script's own none string
- take over widgetBackground, which the generated file no longer defines, and add the two arrow variables the dialog's focusedlayout now shares
- rename the sort order label variable to match its property

VideoFullScreen.xml:
- hide end time, position, progress and cache bar during live playback
- name the audio and subtitle stream in the info line
- separate genres with commas
- call the channel label variable by the name it is defined under

VideoOSD.xml:
- rebuild the subtitle stream row as previous/name/next, using the new PreviousSubtitle action
- open the subtitle settings from the subtitle name and drop the settings icon
- remove the audio stream cycler, as audio has no backward action, and open the audio settings from the audio button
- name the button row so the rows around it move to whichever of its buttons is on screen, rather than to a play button that is not built when the player cannot pause
- send the option row, the subtitle stream row and the seek slider to it, as all three named that play button
- wrap left and right between the three buttons of the subtitle stream row, which stepped out to the record and skip back buttons at its ends

Windows that fill the screen:
- set a black background colour on all twenty-seven, so Kodi clears the screen rather than leaving each frame to draw over the one before

media/:
- add focusline.png and focuslinec.png, the three pixel focus line and its centred variant
- remove the eleven focus textures the layouts no longer name, six of which nothing had referenced for some time
- whiten the colour channels under every transparent pixel, so the packer can store a white-on-alpha texture in one channel instead of four; provably lossless, as no visible pixel is touched
- store the greyscale textures as grey plus alpha rather than RGBA, matching how Estuary keeps its own
- remove the drop shadows from the home menu icons and the PVR timer icon
- flatten the focus textures to white, which the 27c, 52c and 66c variants already were
- repack Textures.xbt with the Kodi v22 texture packer, which writes XBT 3 and picks a channel count per texture; 231 frames are now single channel and 194 dual, leaving 82 in full colour

addon.xml:
- require xbmc.gui 5.18.0
- require script.skinshortcuts 3.0.3, as the property overrides the configuration uses did not exist before 3.0.2
- bump version to 22.0.0
- update changelog

Changelog.md:
- update changelog
- remove the duplicate v16.9.3 heading

sync-translations.yml:
- fire on the development branch as well, as the trigger named only omega and translations therefore stopped propagating when work moved
- run only when language/ changes, which is all the sync copies
- pin actions/checkout to v4 and repo-file-sync-action to a commit, as both floated and the second is handed a token with write access across the sibling branches

validate.yml:
- check the skin on every pull request, as nothing ran on them before
- follow the live branches on push, dropping a branch that no longer exists and adding the aspect ratio siblings
- fail on dangling include and variable references, now that the last two are gone

validate_skin.py:
- report include and variable names that are referenced but never defined, names defined twice in one file, and files that do not parse, none of which Kodi reports usefully at runtime
- report each locale's msgid against en_gb and the Kodi markup tokens between msgid and msgstr, without failing on either, as translations come from Weblate and a hand-edit is overwritten on the next sync
- leave definitions that are never used unreported, as names reached through a param value or a quoted expression are invisible to a structural parse
- check a widget's sort against what it actually sorts by, across the bundled playlist's own order, the widget definition the picker copies from and the menu seed; nothing else keeps the three in step and a disagreement is invisible from the skin
