<!DOCTYPE html>
<!-- saved from url=(0045)https://replit.com/@l2darkness38/yvvy#main.py -->
<html lang="en" class=" " style=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style>.ͼ1.cm-editor.cm-focused {outline: 1px dotted #212121;}
.ͼ1.cm-editor {position: relative !important; box-sizing: border-box; display: flex !important; flex-direction: column;}
.ͼ1 .cm-scroller {display: flex !important; align-items: flex-start !important; font-family: monospace; line-height: 1.4; height: 100%; overflow-x: auto; position: relative; z-index: 0;}
.ͼ1 .cm-content[contenteditable=true] {-webkit-user-modify: read-write-plaintext-only;}
.ͼ1 .cm-content {margin: 0; flex-grow: 2; min-height: 100%; display: block; white-space: pre; word-wrap: normal; box-sizing: border-box; padding: 4px 0; outline: none;}
.ͼ1 .cm-lineWrapping {white-space: pre-wrap; white-space: break-spaces; word-break: break-word; overflow-wrap: anywhere;}
.ͼ2 .cm-content {caret-color: black;}
.ͼ3 .cm-content {caret-color: white;}
.ͼ1 .cm-line {display: block; padding: 0 2px 0 4px;}
.ͼ1 .cm-selectionLayer {z-index: -1; contain: size style;}
.ͼ1 .cm-selectionBackground {position: absolute;}
.ͼ2 .cm-selectionBackground {background: #d9d9d9;}
.ͼ3 .cm-selectionBackground {background: #222;}
.ͼ2.cm-focused .cm-selectionBackground {background: #d7d4f0;}
.ͼ3.cm-focused .cm-selectionBackground {background: #233;}
.ͼ1 .cm-cursorLayer {z-index: 100; contain: size style; pointer-events: none;}
.ͼ1.cm-focused .cm-cursorLayer {animation: steps(1) cm-blink 1.2s infinite;}
@keyframes cm-blink {50% {visibility: hidden;}}
@keyframes cm-blink2 {50% {visibility: hidden;}}
.ͼ1 .cm-cursor, .ͼ1 .cm-dropCursor {position: absolute; border-left: 1.2px solid black; margin-left: -0.6px; pointer-events: none;}
.ͼ1 .cm-cursor {display: none;}
.ͼ3 .cm-cursor {border-left-color: #444;}
.ͼ1.cm-focused .cm-cursor {display: block;}
.ͼ2 .cm-activeLine {background-color: #f3f9ff;}
.ͼ3 .cm-activeLine {background-color: #223039;}
.ͼ2 .cm-specialChar {color: red;}
.ͼ3 .cm-specialChar {color: #f78;}
.ͼ1 .cm-gutters {display: flex; height: 100%; box-sizing: border-box; left: 0; z-index: 200;}
.ͼ2 .cm-gutters {background-color: #f5f5f5; color: #6c6c6c; border-right: 1px solid #ddd;}
.ͼ3 .cm-gutters {background-color: #333338; color: #ccc;}
.ͼ1 .cm-gutter {display: flex !important; flex-direction: column; flex-shrink: 0; box-sizing: border-box; min-height: 100%; overflow: hidden;}
.ͼ1 .cm-gutterElement {box-sizing: border-box;}
.ͼ1 .cm-lineNumbers .cm-gutterElement {padding: 0 3px 0 5px; min-width: 20px; text-align: right; white-space: nowrap;}
.ͼ2 .cm-activeLineGutter {background-color: #e2f2ff;}
.ͼ3 .cm-activeLineGutter {background-color: #222227;}
.ͼ1 .cm-panels {box-sizing: border-box; position: sticky; left: 0; right: 0;}
.ͼ2 .cm-panels {background-color: #f5f5f5; color: black;}
.ͼ2 .cm-panels-top {border-bottom: 1px solid #ddd;}
.ͼ2 .cm-panels-bottom {border-top: 1px solid #ddd;}
.ͼ3 .cm-panels {background-color: #333338; color: white;}
.ͼ1 .cm-tab {display: inline-block; overflow: hidden; vertical-align: bottom;}
.ͼ1 .cm-widgetBuffer {vertical-align: text-top; height: 1em; display: inline;}
.ͼ1 .cm-placeholder {color: #888; display: inline-block; vertical-align: top;}
.ͼ1 .cm-button {vertical-align: middle; color: inherit; font-size: 70%; padding: .2em 1em; border-radius: 1px;}
.ͼ2 .cm-button:active {background-image: linear-gradient(#b4b4b4, #d0d3d6);}
.ͼ2 .cm-button {background-image: linear-gradient(#eff1f5, #d9d9df); border: 1px solid #888;}
.ͼ3 .cm-button:active {background-image: linear-gradient(#111, #333);}
.ͼ3 .cm-button {background-image: linear-gradient(#393939, #111); border: 1px solid #888;}
.ͼ1 .cm-textfield {vertical-align: middle; color: inherit; font-size: 70%; border: 1px solid silver; padding: .2em .5em;}
.ͼ2 .cm-textfield {background-color: white;}
.ͼ3 .cm-textfield {border: 1px solid #555; background-color: inherit;}
.ͼo {background-color: transparent !important;}
.ͼo .cm-content {padding-bottom: var(--space-4) !important;}
.ͼ28x.cm-focused {outline: 0 none;}
.ͼ28x {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ28x .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ28x .cm-line {line-height: var(--line-height-small);}
.ͼ28x .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ28x .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ28x .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ28x .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ28x.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ28x .cm-cursor, .ͼ28x .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ28x .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ28x .cm-activeLine {background-color: var(--background-higher);}
.ͼ28x .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ28x .cm-specialChar {color: var(--accent-negative-default);}
.ͼ28x .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ28x .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ28x .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ28x .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ28x .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ28x .cm-vim-panel input {color: var(--foreground-default);}
.ͼ28x .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ28x .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ28x .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ28x .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ28x .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ28x .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ28x .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ28x .cm-matchingBracket, .ͼ28x .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ28x .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ28x .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ28x .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ28x .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ28x .emmet-preview .cm-content {padding: 0 !important;}
.ͼ28x .emmet-preview .cm-scroller {z-index: 1;}
.ͼ28x .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ28x .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ28x .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ28x .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ28x .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ28x .cm-tooltip.multiplayer-tooltip, .ͼ28x .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ28x .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ28x .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ28x .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ28x .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ28x .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ28x .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ28x .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ28x .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ28p {color: var(--foreground-default);}
.ͼ28q {color: var(--outline-stronger);}
.ͼ28r {color: var(--accent-red-default);}
.ͼ28s {color: var(--accent-orange-stronger);}
.ͼ28t {color: var(--accent-yellow-stronger);}
.ͼ28u {color: var(--accent-lime-stronger);}
.ͼ28v {color: var(--accent-green-stronger);}
.ͼ28w {color: var(--accent-teal-stronger);}
.ͼ28h {color: var(--foreground-default);}
.ͼ28i {color: var(--accent-green-default);}
.ͼ28j {color: var(--accent-red-stronger);}
.ͼ28k {color: var(--accent-orange-strongest);}
.ͼ28l {color: var(--accent-yellow-strongest);}
.ͼ28m {color: var(--accent-lime-strongest);}
.ͼ28n {color: var(--accent-green-strongest);}
.ͼ28o {color: var(--accent-teal-strongest);}
.ͼ284 {text-decoration: underline;}
.ͼ285 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ286 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ287 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ288 {font-style: italic;}
.ͼ289 {font-weight: var(--font-weight-bold);}
.ͼ28a {text-decoration: line-through;}
.ͼ28b {font-family: var(--font-family-code);}
.ͼ28c {color: var(--foreground-dimmest);}
.ͼ28d {color: var(--accent-blue-strongest);}
.ͼ28e {color: var(--accent-blue-stronger);}
.ͼ28f {color: var(--accent-purple-stronger);}
.ͼ28g {color: var(--accent-pink-stronger);}
.ͼ282.cm-focused {outline: 0 none;}
.ͼ282 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ282 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ282 .cm-line {line-height: var(--line-height-small);}
.ͼ282 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ282 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ282 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ282 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ282.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ282 .cm-cursor, .ͼ282 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ282 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ282 .cm-activeLine {background-color: var(--background-higher);}
.ͼ282 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ282 .cm-specialChar {color: var(--accent-negative-default);}
.ͼ282 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ282 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ282 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ282 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ282 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ282 .cm-vim-panel input {color: var(--foreground-default);}
.ͼ282 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ282 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ282 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ282 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ282 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ282 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ282 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ282 .cm-matchingBracket, .ͼ282 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ282 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ282 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ282 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ282 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ282 .emmet-preview .cm-content {padding: 0 !important;}
.ͼ282 .emmet-preview .cm-scroller {z-index: 1;}
.ͼ282 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ282 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ282 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ282 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ282 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ282 .cm-tooltip.multiplayer-tooltip, .ͼ282 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ282 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ282 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ282 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ282 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ282 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ282 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ282 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ282 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ27u {color: var(--foreground-default);}
.ͼ27v {color: var(--outline-stronger);}
.ͼ27w {color: var(--accent-red-default);}
.ͼ27x {color: var(--accent-orange-stronger);}
.ͼ27y {color: var(--accent-yellow-stronger);}
.ͼ27z {color: var(--accent-lime-stronger);}
.ͼ280 {color: var(--accent-green-stronger);}
.ͼ281 {color: var(--accent-teal-stronger);}
.ͼ27m {color: var(--foreground-default);}
.ͼ27n {color: var(--accent-green-default);}
.ͼ27o {color: var(--accent-red-stronger);}
.ͼ27p {color: var(--accent-orange-strongest);}
.ͼ27q {color: var(--accent-yellow-strongest);}
.ͼ27r {color: var(--accent-lime-strongest);}
.ͼ27s {color: var(--accent-green-strongest);}
.ͼ27t {color: var(--accent-teal-strongest);}
.ͼ279 {text-decoration: underline;}
.ͼ27a {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ27b {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ27c {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ27d {font-style: italic;}
.ͼ27e {font-weight: var(--font-weight-bold);}
.ͼ27f {text-decoration: line-through;}
.ͼ27g {font-family: var(--font-family-code);}
.ͼ27h {color: var(--foreground-dimmest);}
.ͼ27i {color: var(--accent-blue-strongest);}
.ͼ27j {color: var(--accent-blue-stronger);}
.ͼ27k {color: var(--accent-purple-stronger);}
.ͼ27l {color: var(--accent-pink-stronger);}
.ͼ277.cm-focused {outline: 0 none;}
.ͼ277 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ277 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ277 .cm-line {line-height: var(--line-height-small);}
.ͼ277 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ277 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ277 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ277 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ277.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ277 .cm-cursor, .ͼ277 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ277 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ277 .cm-activeLine {background-color: var(--background-higher);}
.ͼ277 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ277 .cm-specialChar {color: var(--accent-negative-default);}
.ͼ277 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ277 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ277 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ277 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ277 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ277 .cm-vim-panel input {color: var(--foreground-default);}
.ͼ277 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ277 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ277 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ277 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ277 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ277 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ277 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ277 .cm-matchingBracket, .ͼ277 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ277 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ277 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ277 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ277 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ277 .emmet-preview .cm-content {padding: 0 !important;}
.ͼ277 .emmet-preview .cm-scroller {z-index: 1;}
.ͼ277 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ277 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ277 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ277 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ277 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ277 .cm-tooltip.multiplayer-tooltip, .ͼ277 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ277 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ277 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ277 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ277 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ277 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ277 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ277 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ277 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ26z {color: var(--foreground-default);}
.ͼ270 {color: var(--outline-stronger);}
.ͼ271 {color: var(--accent-red-default);}
.ͼ272 {color: var(--accent-orange-stronger);}
.ͼ273 {color: var(--accent-yellow-stronger);}
.ͼ274 {color: var(--accent-lime-stronger);}
.ͼ275 {color: var(--accent-green-stronger);}
.ͼ276 {color: var(--accent-teal-stronger);}
.ͼ26r {color: var(--foreground-default);}
.ͼ26s {color: var(--accent-green-default);}
.ͼ26t {color: var(--accent-red-stronger);}
.ͼ26u {color: var(--accent-orange-strongest);}
.ͼ26v {color: var(--accent-yellow-strongest);}
.ͼ26w {color: var(--accent-lime-strongest);}
.ͼ26x {color: var(--accent-green-strongest);}
.ͼ26y {color: var(--accent-teal-strongest);}
.ͼ26e {text-decoration: underline;}
.ͼ26f {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ26g {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ26h {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ26i {font-style: italic;}
.ͼ26j {font-weight: var(--font-weight-bold);}
.ͼ26k {text-decoration: line-through;}
.ͼ26l {font-family: var(--font-family-code);}
.ͼ26m {color: var(--foreground-dimmest);}
.ͼ26n {color: var(--accent-blue-strongest);}
.ͼ26o {color: var(--accent-blue-stronger);}
.ͼ26p {color: var(--accent-purple-stronger);}
.ͼ26q {color: var(--accent-pink-stronger);}
.ͼ26d.cm-focused {outline: 0 none;}
.ͼ26d {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ26d .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ26d .cm-line {line-height: var(--line-height-small);}
.ͼ26d .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ26d .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ26d .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ26d .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ26d.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ26d .cm-cursor, .ͼ26d .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ26d .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ26d .cm-activeLine {background-color: var(--background-higher);}
.ͼ26d .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ26d .cm-specialChar {color: var(--accent-negative-default);}
.ͼ26d .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ26d .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ26d .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ26d .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ26d .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ26d .cm-vim-panel input {color: var(--foreground-default);}
.ͼ26d .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ26d .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ26d .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ26d .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ26d .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ26d .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ26d .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ26d .cm-matchingBracket, .ͼ26d .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ26d .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ26d .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ26d .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ26d .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ26d .emmet-preview .cm-content {padding: 0 !important;}
.ͼ26d .emmet-preview .cm-scroller {z-index: 1;}
.ͼ26d .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ26d .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ26d .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ26d .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ26d .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ26d .cm-tooltip.multiplayer-tooltip, .ͼ26d .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ26d .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ26d .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ26d .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ26d .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ26d .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ26d .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ26d .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ26d .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ265 {color: var(--foreground-default);}
.ͼ266 {color: var(--outline-stronger);}
.ͼ267 {color: var(--accent-red-default);}
.ͼ268 {color: var(--accent-orange-stronger);}
.ͼ269 {color: var(--accent-yellow-stronger);}
.ͼ26a {color: var(--accent-lime-stronger);}
.ͼ26b {color: var(--accent-green-stronger);}
.ͼ26c {color: var(--accent-teal-stronger);}
.ͼ25x {color: var(--foreground-default);}
.ͼ25y {color: var(--accent-green-default);}
.ͼ25z {color: var(--accent-red-stronger);}
.ͼ260 {color: var(--accent-orange-strongest);}
.ͼ261 {color: var(--accent-yellow-strongest);}
.ͼ262 {color: var(--accent-lime-strongest);}
.ͼ263 {color: var(--accent-green-strongest);}
.ͼ264 {color: var(--accent-teal-strongest);}
.ͼ25k {text-decoration: underline;}
.ͼ25l {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ25m {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ25n {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ25o {font-style: italic;}
.ͼ25p {font-weight: var(--font-weight-bold);}
.ͼ25q {text-decoration: line-through;}
.ͼ25r {font-family: var(--font-family-code);}
.ͼ25s {color: var(--foreground-dimmest);}
.ͼ25t {color: var(--accent-blue-strongest);}
.ͼ25u {color: var(--accent-blue-stronger);}
.ͼ25v {color: var(--accent-purple-stronger);}
.ͼ25w {color: var(--accent-pink-stronger);}
.ͼ25j.cm-focused {outline: 0 none;}
.ͼ25j {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ25j .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ25j .cm-line {line-height: var(--line-height-small);}
.ͼ25j .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ25j .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ25j .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ25j .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ25j.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ25j .cm-cursor, .ͼ25j .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ25j .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ25j .cm-activeLine {background-color: var(--background-higher);}
.ͼ25j .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ25j .cm-specialChar {color: var(--accent-negative-default);}
.ͼ25j .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ25j .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ25j .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ25j .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ25j .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ25j .cm-vim-panel input {color: var(--foreground-default);}
.ͼ25j .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ25j .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ25j .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ25j .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ25j .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ25j .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ25j .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ25j .cm-matchingBracket, .ͼ25j .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ25j .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ25j .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ25j .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ25j .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ25j .emmet-preview .cm-content {padding: 0 !important;}
.ͼ25j .emmet-preview .cm-scroller {z-index: 1;}
.ͼ25j .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ25j .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ25j .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ25j .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ25j .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ25j .cm-tooltip.multiplayer-tooltip, .ͼ25j .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ25j .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ25j .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ25j .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ25j .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ25j .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ25j .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ25j .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ25j .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ25b {color: var(--foreground-default);}
.ͼ25c {color: var(--outline-stronger);}
.ͼ25d {color: var(--accent-red-default);}
.ͼ25e {color: var(--accent-orange-stronger);}
.ͼ25f {color: var(--accent-yellow-stronger);}
.ͼ25g {color: var(--accent-lime-stronger);}
.ͼ25h {color: var(--accent-green-stronger);}
.ͼ25i {color: var(--accent-teal-stronger);}
.ͼ253 {color: var(--foreground-default);}
.ͼ254 {color: var(--accent-green-default);}
.ͼ255 {color: var(--accent-red-stronger);}
.ͼ256 {color: var(--accent-orange-strongest);}
.ͼ257 {color: var(--accent-yellow-strongest);}
.ͼ258 {color: var(--accent-lime-strongest);}
.ͼ259 {color: var(--accent-green-strongest);}
.ͼ25a {color: var(--accent-teal-strongest);}
.ͼ24q {text-decoration: underline;}
.ͼ24r {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ24s {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ24t {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ24u {font-style: italic;}
.ͼ24v {font-weight: var(--font-weight-bold);}
.ͼ24w {text-decoration: line-through;}
.ͼ24x {font-family: var(--font-family-code);}
.ͼ24y {color: var(--foreground-dimmest);}
.ͼ24z {color: var(--accent-blue-strongest);}
.ͼ250 {color: var(--accent-blue-stronger);}
.ͼ251 {color: var(--accent-purple-stronger);}
.ͼ252 {color: var(--accent-pink-stronger);}
.ͼ24p.cm-focused {outline: 0 none;}
.ͼ24p {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ24p .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ24p .cm-line {line-height: var(--line-height-small);}
.ͼ24p .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ24p .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ24p .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ24p .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ24p.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ24p .cm-cursor, .ͼ24p .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ24p .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ24p .cm-activeLine {background-color: var(--background-higher);}
.ͼ24p .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ24p .cm-specialChar {color: var(--accent-negative-default);}
.ͼ24p .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ24p .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ24p .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ24p .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ24p .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ24p .cm-vim-panel input {color: var(--foreground-default);}
.ͼ24p .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ24p .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ24p .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ24p .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ24p .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ24p .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ24p .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ24p .cm-matchingBracket, .ͼ24p .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ24p .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ24p .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ24p .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ24p .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ24p .emmet-preview .cm-content {padding: 0 !important;}
.ͼ24p .emmet-preview .cm-scroller {z-index: 1;}
.ͼ24p .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ24p .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ24p .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ24p .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ24p .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ24p .cm-tooltip.multiplayer-tooltip, .ͼ24p .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ24p .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ24p .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ24p .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ24p .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ24p .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ24p .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ24p .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ24p .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ24h {color: var(--foreground-default);}
.ͼ24i {color: var(--outline-stronger);}
.ͼ24j {color: var(--accent-red-default);}
.ͼ24k {color: var(--accent-orange-stronger);}
.ͼ24l {color: var(--accent-yellow-stronger);}
.ͼ24m {color: var(--accent-lime-stronger);}
.ͼ24n {color: var(--accent-green-stronger);}
.ͼ24o {color: var(--accent-teal-stronger);}
.ͼ249 {color: var(--foreground-default);}
.ͼ24a {color: var(--accent-green-default);}
.ͼ24b {color: var(--accent-red-stronger);}
.ͼ24c {color: var(--accent-orange-strongest);}
.ͼ24d {color: var(--accent-yellow-strongest);}
.ͼ24e {color: var(--accent-lime-strongest);}
.ͼ24f {color: var(--accent-green-strongest);}
.ͼ24g {color: var(--accent-teal-strongest);}
.ͼ23w {text-decoration: underline;}
.ͼ23x {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ23y {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ23z {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ240 {font-style: italic;}
.ͼ241 {font-weight: var(--font-weight-bold);}
.ͼ242 {text-decoration: line-through;}
.ͼ243 {font-family: var(--font-family-code);}
.ͼ244 {color: var(--foreground-dimmest);}
.ͼ245 {color: var(--accent-blue-strongest);}
.ͼ246 {color: var(--accent-blue-stronger);}
.ͼ247 {color: var(--accent-purple-stronger);}
.ͼ248 {color: var(--accent-pink-stronger);}
.ͼ23u.cm-focused {outline: 0 none;}
.ͼ23u {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ23u .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ23u .cm-line {line-height: var(--line-height-small);}
.ͼ23u .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ23u .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ23u .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ23u .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ23u.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ23u .cm-cursor, .ͼ23u .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ23u .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ23u .cm-activeLine {background-color: var(--background-higher);}
.ͼ23u .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ23u .cm-specialChar {color: var(--accent-negative-default);}
.ͼ23u .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ23u .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ23u .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ23u .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ23u .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ23u .cm-vim-panel input {color: var(--foreground-default);}
.ͼ23u .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ23u .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ23u .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ23u .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ23u .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ23u .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ23u .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ23u .cm-matchingBracket, .ͼ23u .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ23u .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ23u .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ23u .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ23u .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ23u .emmet-preview .cm-content {padding: 0 !important;}
.ͼ23u .emmet-preview .cm-scroller {z-index: 1;}
.ͼ23u .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ23u .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ23u .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ23u .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ23u .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ23u .cm-tooltip.multiplayer-tooltip, .ͼ23u .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ23u .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ23u .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ23u .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ23u .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ23u .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ23u .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ23u .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ23u .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ23m {color: var(--foreground-default);}
.ͼ23n {color: var(--outline-stronger);}
.ͼ23o {color: var(--accent-red-default);}
.ͼ23p {color: var(--accent-orange-stronger);}
.ͼ23q {color: var(--accent-yellow-stronger);}
.ͼ23r {color: var(--accent-lime-stronger);}
.ͼ23s {color: var(--accent-green-stronger);}
.ͼ23t {color: var(--accent-teal-stronger);}
.ͼ23e {color: var(--foreground-default);}
.ͼ23f {color: var(--accent-green-default);}
.ͼ23g {color: var(--accent-red-stronger);}
.ͼ23h {color: var(--accent-orange-strongest);}
.ͼ23i {color: var(--accent-yellow-strongest);}
.ͼ23j {color: var(--accent-lime-strongest);}
.ͼ23k {color: var(--accent-green-strongest);}
.ͼ23l {color: var(--accent-teal-strongest);}
.ͼ231 {text-decoration: underline;}
.ͼ232 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ233 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ234 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ235 {font-style: italic;}
.ͼ236 {font-weight: var(--font-weight-bold);}
.ͼ237 {text-decoration: line-through;}
.ͼ238 {font-family: var(--font-family-code);}
.ͼ239 {color: var(--foreground-dimmest);}
.ͼ23a {color: var(--accent-blue-strongest);}
.ͼ23b {color: var(--accent-blue-stronger);}
.ͼ23c {color: var(--accent-purple-stronger);}
.ͼ23d {color: var(--accent-pink-stronger);}
.ͼ22z.cm-focused {outline: 0 none;}
.ͼ22z {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ22z .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ22z .cm-line {line-height: var(--line-height-small);}
.ͼ22z .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ22z .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ22z .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ22z .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ22z.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ22z .cm-cursor, .ͼ22z .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ22z .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ22z .cm-activeLine {background-color: var(--background-higher);}
.ͼ22z .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ22z .cm-specialChar {color: var(--accent-negative-default);}
.ͼ22z .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ22z .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ22z .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ22z .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ22z .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ22z .cm-vim-panel input {color: var(--foreground-default);}
.ͼ22z .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ22z .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ22z .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ22z .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ22z .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ22z .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ22z .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ22z .cm-matchingBracket, .ͼ22z .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ22z .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ22z .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ22z .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ22z .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ22z .emmet-preview .cm-content {padding: 0 !important;}
.ͼ22z .emmet-preview .cm-scroller {z-index: 1;}
.ͼ22z .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ22z .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ22z .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ22z .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ22z .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ22z .cm-tooltip.multiplayer-tooltip, .ͼ22z .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ22z .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ22z .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ22z .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ22z .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ22z .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ22z .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ22z .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ22z .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ22r {color: var(--foreground-default);}
.ͼ22s {color: var(--outline-stronger);}
.ͼ22t {color: var(--accent-red-default);}
.ͼ22u {color: var(--accent-orange-stronger);}
.ͼ22v {color: var(--accent-yellow-stronger);}
.ͼ22w {color: var(--accent-lime-stronger);}
.ͼ22x {color: var(--accent-green-stronger);}
.ͼ22y {color: var(--accent-teal-stronger);}
.ͼ22j {color: var(--foreground-default);}
.ͼ22k {color: var(--accent-green-default);}
.ͼ22l {color: var(--accent-red-stronger);}
.ͼ22m {color: var(--accent-orange-strongest);}
.ͼ22n {color: var(--accent-yellow-strongest);}
.ͼ22o {color: var(--accent-lime-strongest);}
.ͼ22p {color: var(--accent-green-strongest);}
.ͼ22q {color: var(--accent-teal-strongest);}
.ͼ226 {text-decoration: underline;}
.ͼ227 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ228 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ229 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ22a {font-style: italic;}
.ͼ22b {font-weight: var(--font-weight-bold);}
.ͼ22c {text-decoration: line-through;}
.ͼ22d {font-family: var(--font-family-code);}
.ͼ22e {color: var(--foreground-dimmest);}
.ͼ22f {color: var(--accent-blue-strongest);}
.ͼ22g {color: var(--accent-blue-stronger);}
.ͼ22h {color: var(--accent-purple-stronger);}
.ͼ22i {color: var(--accent-pink-stronger);}
.ͼ225.cm-focused {outline: 0 none;}
.ͼ225 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ225 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ225 .cm-line {line-height: var(--line-height-small);}
.ͼ225 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ225 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ225 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ225 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ225.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ225 .cm-cursor, .ͼ225 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ225 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ225 .cm-activeLine {background-color: var(--background-higher);}
.ͼ225 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ225 .cm-specialChar {color: var(--accent-negative-default);}
.ͼ225 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ225 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ225 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ225 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ225 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ225 .cm-vim-panel input {color: var(--foreground-default);}
.ͼ225 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ225 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ225 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ225 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ225 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ225 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ225 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ225 .cm-matchingBracket, .ͼ225 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ225 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ225 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ225 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ225 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ225 .emmet-preview .cm-content {padding: 0 !important;}
.ͼ225 .emmet-preview .cm-scroller {z-index: 1;}
.ͼ225 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ225 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ225 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ225 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ225 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ225 .cm-tooltip.multiplayer-tooltip, .ͼ225 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ225 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ225 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ225 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ225 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ225 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ225 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ225 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ225 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ21x {color: var(--foreground-default);}
.ͼ21y {color: var(--outline-stronger);}
.ͼ21z {color: var(--accent-red-default);}
.ͼ220 {color: var(--accent-orange-stronger);}
.ͼ221 {color: var(--accent-yellow-stronger);}
.ͼ222 {color: var(--accent-lime-stronger);}
.ͼ223 {color: var(--accent-green-stronger);}
.ͼ224 {color: var(--accent-teal-stronger);}
.ͼ21p {color: var(--foreground-default);}
.ͼ21q {color: var(--accent-green-default);}
.ͼ21r {color: var(--accent-red-stronger);}
.ͼ21s {color: var(--accent-orange-strongest);}
.ͼ21t {color: var(--accent-yellow-strongest);}
.ͼ21u {color: var(--accent-lime-strongest);}
.ͼ21v {color: var(--accent-green-strongest);}
.ͼ21w {color: var(--accent-teal-strongest);}
.ͼ21c {text-decoration: underline;}
.ͼ21d {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ21e {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ21f {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ21g {font-style: italic;}
.ͼ21h {font-weight: var(--font-weight-bold);}
.ͼ21i {text-decoration: line-through;}
.ͼ21j {font-family: var(--font-family-code);}
.ͼ21k {color: var(--foreground-dimmest);}
.ͼ21l {color: var(--accent-blue-strongest);}
.ͼ21m {color: var(--accent-blue-stronger);}
.ͼ21n {color: var(--accent-purple-stronger);}
.ͼ21o {color: var(--accent-pink-stronger);}
.ͼ21b.cm-focused {outline: 0 none;}
.ͼ21b {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ21b .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ21b .cm-line {line-height: var(--line-height-small);}
.ͼ21b .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ21b .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ21b .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ21b .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ21b.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ21b .cm-cursor, .ͼ21b .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ21b .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ21b .cm-activeLine {background-color: var(--background-higher);}
.ͼ21b .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ21b .cm-specialChar {color: var(--accent-negative-default);}
.ͼ21b .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ21b .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ21b .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ21b .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ21b .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ21b .cm-vim-panel input {color: var(--foreground-default);}
.ͼ21b .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ21b .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ21b .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ21b .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ21b .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ21b .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ21b .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ21b .cm-matchingBracket, .ͼ21b .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ21b .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ21b .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ21b .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ21b .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ21b .emmet-preview .cm-content {padding: 0 !important;}
.ͼ21b .emmet-preview .cm-scroller {z-index: 1;}
.ͼ21b .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ21b .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ21b .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ21b .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ21b .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ21b .cm-tooltip.multiplayer-tooltip, .ͼ21b .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ21b .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ21b .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ21b .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ21b .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ21b .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ21b .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ21b .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ21b .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ213 {color: var(--foreground-default);}
.ͼ214 {color: var(--outline-stronger);}
.ͼ215 {color: var(--accent-red-default);}
.ͼ216 {color: var(--accent-orange-stronger);}
.ͼ217 {color: var(--accent-yellow-stronger);}
.ͼ218 {color: var(--accent-lime-stronger);}
.ͼ219 {color: var(--accent-green-stronger);}
.ͼ21a {color: var(--accent-teal-stronger);}
.ͼ20v {color: var(--foreground-default);}
.ͼ20w {color: var(--accent-green-default);}
.ͼ20x {color: var(--accent-red-stronger);}
.ͼ20y {color: var(--accent-orange-strongest);}
.ͼ20z {color: var(--accent-yellow-strongest);}
.ͼ210 {color: var(--accent-lime-strongest);}
.ͼ211 {color: var(--accent-green-strongest);}
.ͼ212 {color: var(--accent-teal-strongest);}
.ͼ20i {text-decoration: underline;}
.ͼ20j {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ20k {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ20l {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ20m {font-style: italic;}
.ͼ20n {font-weight: var(--font-weight-bold);}
.ͼ20o {text-decoration: line-through;}
.ͼ20p {font-family: var(--font-family-code);}
.ͼ20q {color: var(--foreground-dimmest);}
.ͼ20r {color: var(--accent-blue-strongest);}
.ͼ20s {color: var(--accent-blue-stronger);}
.ͼ20t {color: var(--accent-purple-stronger);}
.ͼ20u {color: var(--accent-pink-stronger);}
.ͼ20h.cm-focused {outline: 0 none;}
.ͼ20h {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ20h .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ20h .cm-line {line-height: var(--line-height-small);}
.ͼ20h .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ20h .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ20h .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ20h .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ20h.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ20h .cm-cursor, .ͼ20h .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ20h .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ20h .cm-activeLine {background-color: var(--background-higher);}
.ͼ20h .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ20h .cm-specialChar {color: var(--accent-negative-default);}
.ͼ20h .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ20h .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ20h .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ20h .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ20h .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ20h .cm-vim-panel input {color: var(--foreground-default);}
.ͼ20h .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ20h .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ20h .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ20h .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ20h .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ20h .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ20h .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ20h .cm-matchingBracket, .ͼ20h .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ20h .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ20h .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ20h .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ20h .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ20h .emmet-preview .cm-content {padding: 0 !important;}
.ͼ20h .emmet-preview .cm-scroller {z-index: 1;}
.ͼ20h .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ20h .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ20h .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ20h .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ20h .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ20h .cm-tooltip.multiplayer-tooltip, .ͼ20h .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ20h .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ20h .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ20h .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ20h .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ20h .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ20h .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ20h .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ20h .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ209 {color: var(--foreground-default);}
.ͼ20a {color: var(--outline-stronger);}
.ͼ20b {color: var(--accent-red-default);}
.ͼ20c {color: var(--accent-orange-stronger);}
.ͼ20d {color: var(--accent-yellow-stronger);}
.ͼ20e {color: var(--accent-lime-stronger);}
.ͼ20f {color: var(--accent-green-stronger);}
.ͼ20g {color: var(--accent-teal-stronger);}
.ͼ201 {color: var(--foreground-default);}
.ͼ202 {color: var(--accent-green-default);}
.ͼ203 {color: var(--accent-red-stronger);}
.ͼ204 {color: var(--accent-orange-strongest);}
.ͼ205 {color: var(--accent-yellow-strongest);}
.ͼ206 {color: var(--accent-lime-strongest);}
.ͼ207 {color: var(--accent-green-strongest);}
.ͼ208 {color: var(--accent-teal-strongest);}
.ͼ1zo {text-decoration: underline;}
.ͼ1zp {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1zq {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1zr {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1zs {font-style: italic;}
.ͼ1zt {font-weight: var(--font-weight-bold);}
.ͼ1zu {text-decoration: line-through;}
.ͼ1zv {font-family: var(--font-family-code);}
.ͼ1zw {color: var(--foreground-dimmest);}
.ͼ1zx {color: var(--accent-blue-strongest);}
.ͼ1zy {color: var(--accent-blue-stronger);}
.ͼ1zz {color: var(--accent-purple-stronger);}
.ͼ200 {color: var(--accent-pink-stronger);}
.ͼ1zn.cm-focused {outline: 0 none;}
.ͼ1zn {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1zn .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1zn .cm-line {line-height: var(--line-height-small);}
.ͼ1zn .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1zn .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1zn .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1zn .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1zn.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1zn .cm-cursor, .ͼ1zn .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1zn .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1zn .cm-activeLine {background-color: var(--background-higher);}
.ͼ1zn .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1zn .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1zn .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1zn .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1zn .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1zn .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1zn .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1zn .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1zn .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1zn .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1zn .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1zn .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1zn .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1zn .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1zn .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1zn .cm-matchingBracket, .ͼ1zn .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1zn .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1zn .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1zn .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1zn .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1zn .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1zn .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1zn .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1zn .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1zn .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1zn .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1zn .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1zn .cm-tooltip.multiplayer-tooltip, .ͼ1zn .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1zn .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1zn .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1zn .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1zn .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1zn .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1zn .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1zn .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1zn .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1zf {color: var(--foreground-default);}
.ͼ1zg {color: var(--outline-stronger);}
.ͼ1zh {color: var(--accent-red-default);}
.ͼ1zi {color: var(--accent-orange-stronger);}
.ͼ1zj {color: var(--accent-yellow-stronger);}
.ͼ1zk {color: var(--accent-lime-stronger);}
.ͼ1zl {color: var(--accent-green-stronger);}
.ͼ1zm {color: var(--accent-teal-stronger);}
.ͼ1z7 {color: var(--foreground-default);}
.ͼ1z8 {color: var(--accent-green-default);}
.ͼ1z9 {color: var(--accent-red-stronger);}
.ͼ1za {color: var(--accent-orange-strongest);}
.ͼ1zb {color: var(--accent-yellow-strongest);}
.ͼ1zc {color: var(--accent-lime-strongest);}
.ͼ1zd {color: var(--accent-green-strongest);}
.ͼ1ze {color: var(--accent-teal-strongest);}
.ͼ1yu {text-decoration: underline;}
.ͼ1yv {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1yw {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1yx {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1yy {font-style: italic;}
.ͼ1yz {font-weight: var(--font-weight-bold);}
.ͼ1z0 {text-decoration: line-through;}
.ͼ1z1 {font-family: var(--font-family-code);}
.ͼ1z2 {color: var(--foreground-dimmest);}
.ͼ1z3 {color: var(--accent-blue-strongest);}
.ͼ1z4 {color: var(--accent-blue-stronger);}
.ͼ1z5 {color: var(--accent-purple-stronger);}
.ͼ1z6 {color: var(--accent-pink-stronger);}
.ͼ1yt.cm-focused {outline: 0 none;}
.ͼ1yt {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1yt .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1yt .cm-line {line-height: var(--line-height-small);}
.ͼ1yt .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1yt .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1yt .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1yt .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1yt.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1yt .cm-cursor, .ͼ1yt .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1yt .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1yt .cm-activeLine {background-color: var(--background-higher);}
.ͼ1yt .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1yt .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1yt .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1yt .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1yt .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1yt .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1yt .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1yt .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1yt .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1yt .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1yt .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1yt .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1yt .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1yt .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1yt .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1yt .cm-matchingBracket, .ͼ1yt .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1yt .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1yt .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1yt .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1yt .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1yt .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1yt .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1yt .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1yt .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1yt .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1yt .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1yt .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1yt .cm-tooltip.multiplayer-tooltip, .ͼ1yt .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1yt .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1yt .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1yt .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1yt .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1yt .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1yt .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1yt .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1yt .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1yl {color: var(--foreground-default);}
.ͼ1ym {color: var(--outline-stronger);}
.ͼ1yn {color: var(--accent-red-default);}
.ͼ1yo {color: var(--accent-orange-stronger);}
.ͼ1yp {color: var(--accent-yellow-stronger);}
.ͼ1yq {color: var(--accent-lime-stronger);}
.ͼ1yr {color: var(--accent-green-stronger);}
.ͼ1ys {color: var(--accent-teal-stronger);}
.ͼ1yd {color: var(--foreground-default);}
.ͼ1ye {color: var(--accent-green-default);}
.ͼ1yf {color: var(--accent-red-stronger);}
.ͼ1yg {color: var(--accent-orange-strongest);}
.ͼ1yh {color: var(--accent-yellow-strongest);}
.ͼ1yi {color: var(--accent-lime-strongest);}
.ͼ1yj {color: var(--accent-green-strongest);}
.ͼ1yk {color: var(--accent-teal-strongest);}
.ͼ1y0 {text-decoration: underline;}
.ͼ1y1 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1y2 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1y3 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1y4 {font-style: italic;}
.ͼ1y5 {font-weight: var(--font-weight-bold);}
.ͼ1y6 {text-decoration: line-through;}
.ͼ1y7 {font-family: var(--font-family-code);}
.ͼ1y8 {color: var(--foreground-dimmest);}
.ͼ1y9 {color: var(--accent-blue-strongest);}
.ͼ1ya {color: var(--accent-blue-stronger);}
.ͼ1yb {color: var(--accent-purple-stronger);}
.ͼ1yc {color: var(--accent-pink-stronger);}
.ͼ1xz.cm-focused {outline: 0 none;}
.ͼ1xz {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1xz .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1xz .cm-line {line-height: var(--line-height-small);}
.ͼ1xz .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1xz .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1xz .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1xz .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1xz.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1xz .cm-cursor, .ͼ1xz .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1xz .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1xz .cm-activeLine {background-color: var(--background-higher);}
.ͼ1xz .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1xz .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1xz .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1xz .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1xz .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1xz .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1xz .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1xz .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1xz .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1xz .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1xz .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1xz .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1xz .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1xz .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1xz .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1xz .cm-matchingBracket, .ͼ1xz .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1xz .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1xz .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1xz .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1xz .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1xz .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1xz .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1xz .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1xz .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1xz .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1xz .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1xz .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1xz .cm-tooltip.multiplayer-tooltip, .ͼ1xz .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1xz .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1xz .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1xz .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1xz .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1xz .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1xz .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1xz .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1xz .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1xr {color: var(--foreground-default);}
.ͼ1xs {color: var(--outline-stronger);}
.ͼ1xt {color: var(--accent-red-default);}
.ͼ1xu {color: var(--accent-orange-stronger);}
.ͼ1xv {color: var(--accent-yellow-stronger);}
.ͼ1xw {color: var(--accent-lime-stronger);}
.ͼ1xx {color: var(--accent-green-stronger);}
.ͼ1xy {color: var(--accent-teal-stronger);}
.ͼ1xj {color: var(--foreground-default);}
.ͼ1xk {color: var(--accent-green-default);}
.ͼ1xl {color: var(--accent-red-stronger);}
.ͼ1xm {color: var(--accent-orange-strongest);}
.ͼ1xn {color: var(--accent-yellow-strongest);}
.ͼ1xo {color: var(--accent-lime-strongest);}
.ͼ1xp {color: var(--accent-green-strongest);}
.ͼ1xq {color: var(--accent-teal-strongest);}
.ͼ1x6 {text-decoration: underline;}
.ͼ1x7 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1x8 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1x9 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1xa {font-style: italic;}
.ͼ1xb {font-weight: var(--font-weight-bold);}
.ͼ1xc {text-decoration: line-through;}
.ͼ1xd {font-family: var(--font-family-code);}
.ͼ1xe {color: var(--foreground-dimmest);}
.ͼ1xf {color: var(--accent-blue-strongest);}
.ͼ1xg {color: var(--accent-blue-stronger);}
.ͼ1xh {color: var(--accent-purple-stronger);}
.ͼ1xi {color: var(--accent-pink-stronger);}
.ͼ1x5.cm-focused {outline: 0 none;}
.ͼ1x5 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1x5 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1x5 .cm-line {line-height: var(--line-height-small);}
.ͼ1x5 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1x5 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1x5 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1x5 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1x5.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1x5 .cm-cursor, .ͼ1x5 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1x5 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1x5 .cm-activeLine {background-color: var(--background-higher);}
.ͼ1x5 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1x5 .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1x5 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1x5 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1x5 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1x5 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1x5 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1x5 .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1x5 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1x5 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1x5 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1x5 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1x5 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1x5 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1x5 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1x5 .cm-matchingBracket, .ͼ1x5 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1x5 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1x5 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1x5 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1x5 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1x5 .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1x5 .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1x5 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1x5 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1x5 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1x5 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1x5 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1x5 .cm-tooltip.multiplayer-tooltip, .ͼ1x5 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1x5 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1x5 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1x5 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1x5 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1x5 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1x5 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1x5 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1x5 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1wx {color: var(--foreground-default);}
.ͼ1wy {color: var(--outline-stronger);}
.ͼ1wz {color: var(--accent-red-default);}
.ͼ1x0 {color: var(--accent-orange-stronger);}
.ͼ1x1 {color: var(--accent-yellow-stronger);}
.ͼ1x2 {color: var(--accent-lime-stronger);}
.ͼ1x3 {color: var(--accent-green-stronger);}
.ͼ1x4 {color: var(--accent-teal-stronger);}
.ͼ1wp {color: var(--foreground-default);}
.ͼ1wq {color: var(--accent-green-default);}
.ͼ1wr {color: var(--accent-red-stronger);}
.ͼ1ws {color: var(--accent-orange-strongest);}
.ͼ1wt {color: var(--accent-yellow-strongest);}
.ͼ1wu {color: var(--accent-lime-strongest);}
.ͼ1wv {color: var(--accent-green-strongest);}
.ͼ1ww {color: var(--accent-teal-strongest);}
.ͼ1wc {text-decoration: underline;}
.ͼ1wd {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1we {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1wf {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1wg {font-style: italic;}
.ͼ1wh {font-weight: var(--font-weight-bold);}
.ͼ1wi {text-decoration: line-through;}
.ͼ1wj {font-family: var(--font-family-code);}
.ͼ1wk {color: var(--foreground-dimmest);}
.ͼ1wl {color: var(--accent-blue-strongest);}
.ͼ1wm {color: var(--accent-blue-stronger);}
.ͼ1wn {color: var(--accent-purple-stronger);}
.ͼ1wo {color: var(--accent-pink-stronger);}
.ͼ1wb.cm-focused {outline: 0 none;}
.ͼ1wb {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1wb .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1wb .cm-line {line-height: var(--line-height-small);}
.ͼ1wb .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1wb .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1wb .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1wb .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1wb.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1wb .cm-cursor, .ͼ1wb .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1wb .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1wb .cm-activeLine {background-color: var(--background-higher);}
.ͼ1wb .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1wb .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1wb .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1wb .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1wb .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1wb .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1wb .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1wb .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1wb .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1wb .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1wb .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1wb .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1wb .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1wb .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1wb .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1wb .cm-matchingBracket, .ͼ1wb .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1wb .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1wb .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1wb .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1wb .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1wb .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1wb .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1wb .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1wb .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1wb .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1wb .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1wb .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1wb .cm-tooltip.multiplayer-tooltip, .ͼ1wb .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1wb .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1wb .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1wb .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1wb .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1wb .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1wb .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1wb .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1wb .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1w3 {color: var(--foreground-default);}
.ͼ1w4 {color: var(--outline-stronger);}
.ͼ1w5 {color: var(--accent-red-default);}
.ͼ1w6 {color: var(--accent-orange-stronger);}
.ͼ1w7 {color: var(--accent-yellow-stronger);}
.ͼ1w8 {color: var(--accent-lime-stronger);}
.ͼ1w9 {color: var(--accent-green-stronger);}
.ͼ1wa {color: var(--accent-teal-stronger);}
.ͼ1vv {color: var(--foreground-default);}
.ͼ1vw {color: var(--accent-green-default);}
.ͼ1vx {color: var(--accent-red-stronger);}
.ͼ1vy {color: var(--accent-orange-strongest);}
.ͼ1vz {color: var(--accent-yellow-strongest);}
.ͼ1w0 {color: var(--accent-lime-strongest);}
.ͼ1w1 {color: var(--accent-green-strongest);}
.ͼ1w2 {color: var(--accent-teal-strongest);}
.ͼ1vi {text-decoration: underline;}
.ͼ1vj {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1vk {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1vl {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1vm {font-style: italic;}
.ͼ1vn {font-weight: var(--font-weight-bold);}
.ͼ1vo {text-decoration: line-through;}
.ͼ1vp {font-family: var(--font-family-code);}
.ͼ1vq {color: var(--foreground-dimmest);}
.ͼ1vr {color: var(--accent-blue-strongest);}
.ͼ1vs {color: var(--accent-blue-stronger);}
.ͼ1vt {color: var(--accent-purple-stronger);}
.ͼ1vu {color: var(--accent-pink-stronger);}
.ͼ1vh.cm-focused {outline: 0 none;}
.ͼ1vh {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1vh .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1vh .cm-line {line-height: var(--line-height-small);}
.ͼ1vh .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1vh .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1vh .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1vh .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1vh.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1vh .cm-cursor, .ͼ1vh .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1vh .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1vh .cm-activeLine {background-color: var(--background-higher);}
.ͼ1vh .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1vh .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1vh .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1vh .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1vh .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1vh .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1vh .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1vh .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1vh .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1vh .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1vh .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1vh .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1vh .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1vh .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1vh .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1vh .cm-matchingBracket, .ͼ1vh .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1vh .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1vh .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1vh .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1vh .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1vh .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1vh .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1vh .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1vh .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1vh .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1vh .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1vh .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1vh .cm-tooltip.multiplayer-tooltip, .ͼ1vh .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1vh .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1vh .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1vh .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1vh .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1vh .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1vh .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1vh .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1vh .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1v9 {color: var(--foreground-default);}
.ͼ1va {color: var(--outline-stronger);}
.ͼ1vb {color: var(--accent-red-default);}
.ͼ1vc {color: var(--accent-orange-stronger);}
.ͼ1vd {color: var(--accent-yellow-stronger);}
.ͼ1ve {color: var(--accent-lime-stronger);}
.ͼ1vf {color: var(--accent-green-stronger);}
.ͼ1vg {color: var(--accent-teal-stronger);}
.ͼ1v1 {color: var(--foreground-default);}
.ͼ1v2 {color: var(--accent-green-default);}
.ͼ1v3 {color: var(--accent-red-stronger);}
.ͼ1v4 {color: var(--accent-orange-strongest);}
.ͼ1v5 {color: var(--accent-yellow-strongest);}
.ͼ1v6 {color: var(--accent-lime-strongest);}
.ͼ1v7 {color: var(--accent-green-strongest);}
.ͼ1v8 {color: var(--accent-teal-strongest);}
.ͼ1uo {text-decoration: underline;}
.ͼ1up {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1uq {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1ur {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1us {font-style: italic;}
.ͼ1ut {font-weight: var(--font-weight-bold);}
.ͼ1uu {text-decoration: line-through;}
.ͼ1uv {font-family: var(--font-family-code);}
.ͼ1uw {color: var(--foreground-dimmest);}
.ͼ1ux {color: var(--accent-blue-strongest);}
.ͼ1uy {color: var(--accent-blue-stronger);}
.ͼ1uz {color: var(--accent-purple-stronger);}
.ͼ1v0 {color: var(--accent-pink-stronger);}
.ͼ1un.cm-focused {outline: 0 none;}
.ͼ1un {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1un .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1un .cm-line {line-height: var(--line-height-small);}
.ͼ1un .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1un .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1un .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1un .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1un.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1un .cm-cursor, .ͼ1un .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1un .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1un .cm-activeLine {background-color: var(--background-higher);}
.ͼ1un .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1un .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1un .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1un .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1un .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1un .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1un .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1un .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1un .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1un .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1un .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1un .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1un .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1un .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1un .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1un .cm-matchingBracket, .ͼ1un .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1un .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1un .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1un .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1un .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1un .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1un .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1un .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1un .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1un .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1un .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1un .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1un .cm-tooltip.multiplayer-tooltip, .ͼ1un .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1un .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1un .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1un .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1un .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1un .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1un .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1un .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1un .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1uf {color: var(--foreground-default);}
.ͼ1ug {color: var(--outline-stronger);}
.ͼ1uh {color: var(--accent-red-default);}
.ͼ1ui {color: var(--accent-orange-stronger);}
.ͼ1uj {color: var(--accent-yellow-stronger);}
.ͼ1uk {color: var(--accent-lime-stronger);}
.ͼ1ul {color: var(--accent-green-stronger);}
.ͼ1um {color: var(--accent-teal-stronger);}
.ͼ1u7 {color: var(--foreground-default);}
.ͼ1u8 {color: var(--accent-green-default);}
.ͼ1u9 {color: var(--accent-red-stronger);}
.ͼ1ua {color: var(--accent-orange-strongest);}
.ͼ1ub {color: var(--accent-yellow-strongest);}
.ͼ1uc {color: var(--accent-lime-strongest);}
.ͼ1ud {color: var(--accent-green-strongest);}
.ͼ1ue {color: var(--accent-teal-strongest);}
.ͼ1tu {text-decoration: underline;}
.ͼ1tv {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1tw {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1tx {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1ty {font-style: italic;}
.ͼ1tz {font-weight: var(--font-weight-bold);}
.ͼ1u0 {text-decoration: line-through;}
.ͼ1u1 {font-family: var(--font-family-code);}
.ͼ1u2 {color: var(--foreground-dimmest);}
.ͼ1u3 {color: var(--accent-blue-strongest);}
.ͼ1u4 {color: var(--accent-blue-stronger);}
.ͼ1u5 {color: var(--accent-purple-stronger);}
.ͼ1u6 {color: var(--accent-pink-stronger);}
.ͼ1tt.cm-focused {outline: 0 none;}
.ͼ1tt {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1tt .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1tt .cm-line {line-height: var(--line-height-small);}
.ͼ1tt .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1tt .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1tt .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1tt .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1tt.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1tt .cm-cursor, .ͼ1tt .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1tt .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1tt .cm-activeLine {background-color: var(--background-higher);}
.ͼ1tt .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1tt .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1tt .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1tt .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1tt .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1tt .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1tt .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1tt .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1tt .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1tt .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1tt .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1tt .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1tt .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1tt .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1tt .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1tt .cm-matchingBracket, .ͼ1tt .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1tt .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1tt .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1tt .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1tt .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1tt .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1tt .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1tt .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1tt .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1tt .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1tt .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1tt .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1tt .cm-tooltip.multiplayer-tooltip, .ͼ1tt .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1tt .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1tt .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1tt .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1tt .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1tt .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1tt .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1tt .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1tt .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1tl {color: var(--foreground-default);}
.ͼ1tm {color: var(--outline-stronger);}
.ͼ1tn {color: var(--accent-red-default);}
.ͼ1to {color: var(--accent-orange-stronger);}
.ͼ1tp {color: var(--accent-yellow-stronger);}
.ͼ1tq {color: var(--accent-lime-stronger);}
.ͼ1tr {color: var(--accent-green-stronger);}
.ͼ1ts {color: var(--accent-teal-stronger);}
.ͼ1td {color: var(--foreground-default);}
.ͼ1te {color: var(--accent-green-default);}
.ͼ1tf {color: var(--accent-red-stronger);}
.ͼ1tg {color: var(--accent-orange-strongest);}
.ͼ1th {color: var(--accent-yellow-strongest);}
.ͼ1ti {color: var(--accent-lime-strongest);}
.ͼ1tj {color: var(--accent-green-strongest);}
.ͼ1tk {color: var(--accent-teal-strongest);}
.ͼ1t0 {text-decoration: underline;}
.ͼ1t1 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1t2 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1t3 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1t4 {font-style: italic;}
.ͼ1t5 {font-weight: var(--font-weight-bold);}
.ͼ1t6 {text-decoration: line-through;}
.ͼ1t7 {font-family: var(--font-family-code);}
.ͼ1t8 {color: var(--foreground-dimmest);}
.ͼ1t9 {color: var(--accent-blue-strongest);}
.ͼ1ta {color: var(--accent-blue-stronger);}
.ͼ1tb {color: var(--accent-purple-stronger);}
.ͼ1tc {color: var(--accent-pink-stronger);}
.ͼ1sz.cm-focused {outline: 0 none;}
.ͼ1sz {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1sz .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1sz .cm-line {line-height: var(--line-height-small);}
.ͼ1sz .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1sz .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1sz .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1sz .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1sz.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1sz .cm-cursor, .ͼ1sz .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1sz .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1sz .cm-activeLine {background-color: var(--background-higher);}
.ͼ1sz .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1sz .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1sz .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1sz .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1sz .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1sz .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1sz .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1sz .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1sz .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1sz .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1sz .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1sz .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1sz .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1sz .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1sz .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1sz .cm-matchingBracket, .ͼ1sz .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1sz .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1sz .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1sz .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1sz .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1sz .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1sz .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1sz .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1sz .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1sz .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1sz .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1sz .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1sz .cm-tooltip.multiplayer-tooltip, .ͼ1sz .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1sz .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1sz .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1sz .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1sz .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1sz .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1sz .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1sz .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1sz .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1sr {color: var(--foreground-default);}
.ͼ1ss {color: var(--outline-stronger);}
.ͼ1st {color: var(--accent-red-default);}
.ͼ1su {color: var(--accent-orange-stronger);}
.ͼ1sv {color: var(--accent-yellow-stronger);}
.ͼ1sw {color: var(--accent-lime-stronger);}
.ͼ1sx {color: var(--accent-green-stronger);}
.ͼ1sy {color: var(--accent-teal-stronger);}
.ͼ1sj {color: var(--foreground-default);}
.ͼ1sk {color: var(--accent-green-default);}
.ͼ1sl {color: var(--accent-red-stronger);}
.ͼ1sm {color: var(--accent-orange-strongest);}
.ͼ1sn {color: var(--accent-yellow-strongest);}
.ͼ1so {color: var(--accent-lime-strongest);}
.ͼ1sp {color: var(--accent-green-strongest);}
.ͼ1sq {color: var(--accent-teal-strongest);}
.ͼ1s6 {text-decoration: underline;}
.ͼ1s7 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1s8 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1s9 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1sa {font-style: italic;}
.ͼ1sb {font-weight: var(--font-weight-bold);}
.ͼ1sc {text-decoration: line-through;}
.ͼ1sd {font-family: var(--font-family-code);}
.ͼ1se {color: var(--foreground-dimmest);}
.ͼ1sf {color: var(--accent-blue-strongest);}
.ͼ1sg {color: var(--accent-blue-stronger);}
.ͼ1sh {color: var(--accent-purple-stronger);}
.ͼ1si {color: var(--accent-pink-stronger);}
.ͼ1s5.cm-focused {outline: 0 none;}
.ͼ1s5 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1s5 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1s5 .cm-line {line-height: var(--line-height-small);}
.ͼ1s5 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1s5 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1s5 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1s5 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1s5.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1s5 .cm-cursor, .ͼ1s5 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1s5 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1s5 .cm-activeLine {background-color: var(--background-higher);}
.ͼ1s5 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1s5 .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1s5 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1s5 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1s5 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1s5 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1s5 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1s5 .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1s5 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1s5 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1s5 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1s5 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1s5 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1s5 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1s5 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1s5 .cm-matchingBracket, .ͼ1s5 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1s5 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1s5 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1s5 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1s5 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1s5 .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1s5 .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1s5 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1s5 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1s5 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1s5 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1s5 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1s5 .cm-tooltip.multiplayer-tooltip, .ͼ1s5 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1s5 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1s5 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1s5 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1s5 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1s5 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1s5 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1s5 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1s5 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1rx {color: var(--foreground-default);}
.ͼ1ry {color: var(--outline-stronger);}
.ͼ1rz {color: var(--accent-red-default);}
.ͼ1s0 {color: var(--accent-orange-stronger);}
.ͼ1s1 {color: var(--accent-yellow-stronger);}
.ͼ1s2 {color: var(--accent-lime-stronger);}
.ͼ1s3 {color: var(--accent-green-stronger);}
.ͼ1s4 {color: var(--accent-teal-stronger);}
.ͼ1rp {color: var(--foreground-default);}
.ͼ1rq {color: var(--accent-green-default);}
.ͼ1rr {color: var(--accent-red-stronger);}
.ͼ1rs {color: var(--accent-orange-strongest);}
.ͼ1rt {color: var(--accent-yellow-strongest);}
.ͼ1ru {color: var(--accent-lime-strongest);}
.ͼ1rv {color: var(--accent-green-strongest);}
.ͼ1rw {color: var(--accent-teal-strongest);}
.ͼ1rc {text-decoration: underline;}
.ͼ1rd {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1re {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1rf {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1rg {font-style: italic;}
.ͼ1rh {font-weight: var(--font-weight-bold);}
.ͼ1ri {text-decoration: line-through;}
.ͼ1rj {font-family: var(--font-family-code);}
.ͼ1rk {color: var(--foreground-dimmest);}
.ͼ1rl {color: var(--accent-blue-strongest);}
.ͼ1rm {color: var(--accent-blue-stronger);}
.ͼ1rn {color: var(--accent-purple-stronger);}
.ͼ1ro {color: var(--accent-pink-stronger);}
.ͼ1rb.cm-focused {outline: 0 none;}
.ͼ1rb {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1rb .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1rb .cm-line {line-height: var(--line-height-small);}
.ͼ1rb .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1rb .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1rb .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1rb .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1rb.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1rb .cm-cursor, .ͼ1rb .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1rb .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1rb .cm-activeLine {background-color: var(--background-higher);}
.ͼ1rb .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1rb .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1rb .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1rb .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1rb .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1rb .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1rb .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1rb .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1rb .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1rb .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1rb .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1rb .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1rb .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1rb .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1rb .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1rb .cm-matchingBracket, .ͼ1rb .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1rb .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1rb .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1rb .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1rb .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1rb .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1rb .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1rb .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1rb .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1rb .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1rb .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1rb .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1rb .cm-tooltip.multiplayer-tooltip, .ͼ1rb .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1rb .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1rb .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1rb .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1rb .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1rb .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1rb .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1rb .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1rb .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1r3 {color: var(--foreground-default);}
.ͼ1r4 {color: var(--outline-stronger);}
.ͼ1r5 {color: var(--accent-red-default);}
.ͼ1r6 {color: var(--accent-orange-stronger);}
.ͼ1r7 {color: var(--accent-yellow-stronger);}
.ͼ1r8 {color: var(--accent-lime-stronger);}
.ͼ1r9 {color: var(--accent-green-stronger);}
.ͼ1ra {color: var(--accent-teal-stronger);}
.ͼ1qv {color: var(--foreground-default);}
.ͼ1qw {color: var(--accent-green-default);}
.ͼ1qx {color: var(--accent-red-stronger);}
.ͼ1qy {color: var(--accent-orange-strongest);}
.ͼ1qz {color: var(--accent-yellow-strongest);}
.ͼ1r0 {color: var(--accent-lime-strongest);}
.ͼ1r1 {color: var(--accent-green-strongest);}
.ͼ1r2 {color: var(--accent-teal-strongest);}
.ͼ1qi {text-decoration: underline;}
.ͼ1qj {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1qk {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1ql {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1qm {font-style: italic;}
.ͼ1qn {font-weight: var(--font-weight-bold);}
.ͼ1qo {text-decoration: line-through;}
.ͼ1qp {font-family: var(--font-family-code);}
.ͼ1qq {color: var(--foreground-dimmest);}
.ͼ1qr {color: var(--accent-blue-strongest);}
.ͼ1qs {color: var(--accent-blue-stronger);}
.ͼ1qt {color: var(--accent-purple-stronger);}
.ͼ1qu {color: var(--accent-pink-stronger);}
.ͼ1qh.cm-focused {outline: 0 none;}
.ͼ1qh {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1qh .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1qh .cm-line {line-height: var(--line-height-small);}
.ͼ1qh .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1qh .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1qh .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1qh .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1qh.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1qh .cm-cursor, .ͼ1qh .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1qh .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1qh .cm-activeLine {background-color: var(--background-higher);}
.ͼ1qh .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1qh .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1qh .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1qh .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1qh .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1qh .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1qh .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1qh .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1qh .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1qh .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1qh .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1qh .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1qh .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1qh .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1qh .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1qh .cm-matchingBracket, .ͼ1qh .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1qh .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1qh .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1qh .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1qh .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1qh .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1qh .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1qh .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1qh .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1qh .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1qh .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1qh .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1qh .cm-tooltip.multiplayer-tooltip, .ͼ1qh .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1qh .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1qh .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1qh .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1qh .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1qh .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1qh .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1qh .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1qh .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1q9 {color: var(--foreground-default);}
.ͼ1qa {color: var(--outline-stronger);}
.ͼ1qb {color: var(--accent-red-default);}
.ͼ1qc {color: var(--accent-orange-stronger);}
.ͼ1qd {color: var(--accent-yellow-stronger);}
.ͼ1qe {color: var(--accent-lime-stronger);}
.ͼ1qf {color: var(--accent-green-stronger);}
.ͼ1qg {color: var(--accent-teal-stronger);}
.ͼ1q1 {color: var(--foreground-default);}
.ͼ1q2 {color: var(--accent-green-default);}
.ͼ1q3 {color: var(--accent-red-stronger);}
.ͼ1q4 {color: var(--accent-orange-strongest);}
.ͼ1q5 {color: var(--accent-yellow-strongest);}
.ͼ1q6 {color: var(--accent-lime-strongest);}
.ͼ1q7 {color: var(--accent-green-strongest);}
.ͼ1q8 {color: var(--accent-teal-strongest);}
.ͼ1po {text-decoration: underline;}
.ͼ1pp {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1pq {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1pr {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1ps {font-style: italic;}
.ͼ1pt {font-weight: var(--font-weight-bold);}
.ͼ1pu {text-decoration: line-through;}
.ͼ1pv {font-family: var(--font-family-code);}
.ͼ1pw {color: var(--foreground-dimmest);}
.ͼ1px {color: var(--accent-blue-strongest);}
.ͼ1py {color: var(--accent-blue-stronger);}
.ͼ1pz {color: var(--accent-purple-stronger);}
.ͼ1q0 {color: var(--accent-pink-stronger);}
.ͼ1pn.cm-focused {outline: 0 none;}
.ͼ1pn {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1pn .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1pn .cm-line {line-height: var(--line-height-small);}
.ͼ1pn .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1pn .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1pn .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1pn .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1pn.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1pn .cm-cursor, .ͼ1pn .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1pn .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1pn .cm-activeLine {background-color: var(--background-higher);}
.ͼ1pn .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1pn .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1pn .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1pn .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1pn .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1pn .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1pn .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1pn .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1pn .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1pn .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1pn .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1pn .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1pn .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1pn .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1pn .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1pn .cm-matchingBracket, .ͼ1pn .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1pn .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1pn .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1pn .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1pn .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1pn .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1pn .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1pn .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1pn .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1pn .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1pn .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1pn .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1pn .cm-tooltip.multiplayer-tooltip, .ͼ1pn .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1pn .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1pn .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1pn .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1pn .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1pn .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1pn .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1pn .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1pn .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1pf {color: var(--foreground-default);}
.ͼ1pg {color: var(--outline-stronger);}
.ͼ1ph {color: var(--accent-red-default);}
.ͼ1pi {color: var(--accent-orange-stronger);}
.ͼ1pj {color: var(--accent-yellow-stronger);}
.ͼ1pk {color: var(--accent-lime-stronger);}
.ͼ1pl {color: var(--accent-green-stronger);}
.ͼ1pm {color: var(--accent-teal-stronger);}
.ͼ1p7 {color: var(--foreground-default);}
.ͼ1p8 {color: var(--accent-green-default);}
.ͼ1p9 {color: var(--accent-red-stronger);}
.ͼ1pa {color: var(--accent-orange-strongest);}
.ͼ1pb {color: var(--accent-yellow-strongest);}
.ͼ1pc {color: var(--accent-lime-strongest);}
.ͼ1pd {color: var(--accent-green-strongest);}
.ͼ1pe {color: var(--accent-teal-strongest);}
.ͼ1ou {text-decoration: underline;}
.ͼ1ov {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1ow {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1ox {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1oy {font-style: italic;}
.ͼ1oz {font-weight: var(--font-weight-bold);}
.ͼ1p0 {text-decoration: line-through;}
.ͼ1p1 {font-family: var(--font-family-code);}
.ͼ1p2 {color: var(--foreground-dimmest);}
.ͼ1p3 {color: var(--accent-blue-strongest);}
.ͼ1p4 {color: var(--accent-blue-stronger);}
.ͼ1p5 {color: var(--accent-purple-stronger);}
.ͼ1p6 {color: var(--accent-pink-stronger);}
.ͼ1ot.cm-focused {outline: 0 none;}
.ͼ1ot {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1ot .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1ot .cm-line {line-height: var(--line-height-small);}
.ͼ1ot .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1ot .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1ot .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1ot .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1ot.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1ot .cm-cursor, .ͼ1ot .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1ot .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1ot .cm-activeLine {background-color: var(--background-higher);}
.ͼ1ot .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1ot .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1ot .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1ot .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1ot .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1ot .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1ot .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1ot .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1ot .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1ot .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1ot .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1ot .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1ot .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1ot .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1ot .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1ot .cm-matchingBracket, .ͼ1ot .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1ot .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1ot .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1ot .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1ot .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1ot .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1ot .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1ot .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1ot .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1ot .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1ot .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1ot .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1ot .cm-tooltip.multiplayer-tooltip, .ͼ1ot .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1ot .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1ot .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1ot .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1ot .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1ot .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1ot .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1ot .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1ot .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1ol {color: var(--foreground-default);}
.ͼ1om {color: var(--outline-stronger);}
.ͼ1on {color: var(--accent-red-default);}
.ͼ1oo {color: var(--accent-orange-stronger);}
.ͼ1op {color: var(--accent-yellow-stronger);}
.ͼ1oq {color: var(--accent-lime-stronger);}
.ͼ1or {color: var(--accent-green-stronger);}
.ͼ1os {color: var(--accent-teal-stronger);}
.ͼ1od {color: var(--foreground-default);}
.ͼ1oe {color: var(--accent-green-default);}
.ͼ1of {color: var(--accent-red-stronger);}
.ͼ1og {color: var(--accent-orange-strongest);}
.ͼ1oh {color: var(--accent-yellow-strongest);}
.ͼ1oi {color: var(--accent-lime-strongest);}
.ͼ1oj {color: var(--accent-green-strongest);}
.ͼ1ok {color: var(--accent-teal-strongest);}
.ͼ1o0 {text-decoration: underline;}
.ͼ1o1 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1o2 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1o3 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1o4 {font-style: italic;}
.ͼ1o5 {font-weight: var(--font-weight-bold);}
.ͼ1o6 {text-decoration: line-through;}
.ͼ1o7 {font-family: var(--font-family-code);}
.ͼ1o8 {color: var(--foreground-dimmest);}
.ͼ1o9 {color: var(--accent-blue-strongest);}
.ͼ1oa {color: var(--accent-blue-stronger);}
.ͼ1ob {color: var(--accent-purple-stronger);}
.ͼ1oc {color: var(--accent-pink-stronger);}
.ͼ1ny.cm-focused {outline: 0 none;}
.ͼ1ny {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1ny .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1ny .cm-line {line-height: var(--line-height-small);}
.ͼ1ny .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1ny .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1ny .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1ny .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1ny.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1ny .cm-cursor, .ͼ1ny .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1ny .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1ny .cm-activeLine {background-color: var(--background-higher);}
.ͼ1ny .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1ny .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1ny .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1ny .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1ny .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1ny .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1ny .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1ny .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1ny .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1ny .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1ny .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1ny .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1ny .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1ny .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1ny .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1ny .cm-matchingBracket, .ͼ1ny .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1ny .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1ny .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1ny .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1ny .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1ny .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1ny .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1ny .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1ny .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1ny .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1ny .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1ny .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1ny .cm-tooltip.multiplayer-tooltip, .ͼ1ny .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1ny .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1ny .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1ny .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1ny .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1ny .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1ny .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1ny .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1ny .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1nq {color: var(--foreground-default);}
.ͼ1nr {color: var(--outline-stronger);}
.ͼ1ns {color: var(--accent-red-default);}
.ͼ1nt {color: var(--accent-orange-stronger);}
.ͼ1nu {color: var(--accent-yellow-stronger);}
.ͼ1nv {color: var(--accent-lime-stronger);}
.ͼ1nw {color: var(--accent-green-stronger);}
.ͼ1nx {color: var(--accent-teal-stronger);}
.ͼ1ni {color: var(--foreground-default);}
.ͼ1nj {color: var(--accent-green-default);}
.ͼ1nk {color: var(--accent-red-stronger);}
.ͼ1nl {color: var(--accent-orange-strongest);}
.ͼ1nm {color: var(--accent-yellow-strongest);}
.ͼ1nn {color: var(--accent-lime-strongest);}
.ͼ1no {color: var(--accent-green-strongest);}
.ͼ1np {color: var(--accent-teal-strongest);}
.ͼ1n5 {text-decoration: underline;}
.ͼ1n6 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1n7 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1n8 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1n9 {font-style: italic;}
.ͼ1na {font-weight: var(--font-weight-bold);}
.ͼ1nb {text-decoration: line-through;}
.ͼ1nc {font-family: var(--font-family-code);}
.ͼ1nd {color: var(--foreground-dimmest);}
.ͼ1ne {color: var(--accent-blue-strongest);}
.ͼ1nf {color: var(--accent-blue-stronger);}
.ͼ1ng {color: var(--accent-purple-stronger);}
.ͼ1nh {color: var(--accent-pink-stronger);}
.ͼ1mz.cm-focused {outline: 0 none;}
.ͼ1mz {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1mz .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1mz .cm-line {line-height: var(--line-height-small);}
.ͼ1mz .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1mz .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1mz .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1mz .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1mz.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1mz .cm-cursor, .ͼ1mz .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1mz .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1mz .cm-activeLine {background-color: var(--background-higher);}
.ͼ1mz .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1mz .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1mz .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1mz .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1mz .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1mz .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1mz .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1mz .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1mz .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1mz .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1mz .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1mz .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1mz .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1mz .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1mz .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1mz .cm-matchingBracket, .ͼ1mz .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1mz .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1mz .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1mz .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1mz .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1mz .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1mz .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1mz .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1mz .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1mz .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1mz .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1mz .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1mz .cm-tooltip.multiplayer-tooltip, .ͼ1mz .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1mz .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1mz .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1mz .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1mz .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1mz .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1mz .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1mz .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1mz .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1mr {color: var(--foreground-default);}
.ͼ1ms {color: var(--outline-stronger);}
.ͼ1mt {color: var(--accent-red-default);}
.ͼ1mu {color: var(--accent-orange-stronger);}
.ͼ1mv {color: var(--accent-yellow-stronger);}
.ͼ1mw {color: var(--accent-lime-stronger);}
.ͼ1mx {color: var(--accent-green-stronger);}
.ͼ1my {color: var(--accent-teal-stronger);}
.ͼ1mj {color: var(--foreground-default);}
.ͼ1mk {color: var(--accent-green-default);}
.ͼ1ml {color: var(--accent-red-stronger);}
.ͼ1mm {color: var(--accent-orange-strongest);}
.ͼ1mn {color: var(--accent-yellow-strongest);}
.ͼ1mo {color: var(--accent-lime-strongest);}
.ͼ1mp {color: var(--accent-green-strongest);}
.ͼ1mq {color: var(--accent-teal-strongest);}
.ͼ1m6 {text-decoration: underline;}
.ͼ1m7 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1m8 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1m9 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1ma {font-style: italic;}
.ͼ1mb {font-weight: var(--font-weight-bold);}
.ͼ1mc {text-decoration: line-through;}
.ͼ1md {font-family: var(--font-family-code);}
.ͼ1me {color: var(--foreground-dimmest);}
.ͼ1mf {color: var(--accent-blue-strongest);}
.ͼ1mg {color: var(--accent-blue-stronger);}
.ͼ1mh {color: var(--accent-purple-stronger);}
.ͼ1mi {color: var(--accent-pink-stronger);}
.ͼ1m5.cm-focused {outline: 0 none;}
.ͼ1m5 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1m5 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1m5 .cm-line {line-height: var(--line-height-small);}
.ͼ1m5 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1m5 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1m5 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1m5 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1m5.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1m5 .cm-cursor, .ͼ1m5 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1m5 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1m5 .cm-activeLine {background-color: var(--background-higher);}
.ͼ1m5 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1m5 .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1m5 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1m5 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1m5 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1m5 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1m5 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1m5 .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1m5 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1m5 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1m5 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1m5 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1m5 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1m5 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1m5 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1m5 .cm-matchingBracket, .ͼ1m5 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1m5 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1m5 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1m5 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1m5 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1m5 .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1m5 .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1m5 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1m5 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1m5 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1m5 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1m5 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1m5 .cm-tooltip.multiplayer-tooltip, .ͼ1m5 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1m5 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1m5 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1m5 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1m5 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1m5 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1m5 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1m5 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1m5 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1lx {color: var(--foreground-default);}
.ͼ1ly {color: var(--outline-stronger);}
.ͼ1lz {color: var(--accent-red-default);}
.ͼ1m0 {color: var(--accent-orange-stronger);}
.ͼ1m1 {color: var(--accent-yellow-stronger);}
.ͼ1m2 {color: var(--accent-lime-stronger);}
.ͼ1m3 {color: var(--accent-green-stronger);}
.ͼ1m4 {color: var(--accent-teal-stronger);}
.ͼ1lp {color: var(--foreground-default);}
.ͼ1lq {color: var(--accent-green-default);}
.ͼ1lr {color: var(--accent-red-stronger);}
.ͼ1ls {color: var(--accent-orange-strongest);}
.ͼ1lt {color: var(--accent-yellow-strongest);}
.ͼ1lu {color: var(--accent-lime-strongest);}
.ͼ1lv {color: var(--accent-green-strongest);}
.ͼ1lw {color: var(--accent-teal-strongest);}
.ͼ1lc {text-decoration: underline;}
.ͼ1ld {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1le {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1lf {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1lg {font-style: italic;}
.ͼ1lh {font-weight: var(--font-weight-bold);}
.ͼ1li {text-decoration: line-through;}
.ͼ1lj {font-family: var(--font-family-code);}
.ͼ1lk {color: var(--foreground-dimmest);}
.ͼ1ll {color: var(--accent-blue-strongest);}
.ͼ1lm {color: var(--accent-blue-stronger);}
.ͼ1ln {color: var(--accent-purple-stronger);}
.ͼ1lo {color: var(--accent-pink-stronger);}
.ͼ1la.cm-focused {outline: 0 none;}
.ͼ1la {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1la .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1la .cm-line {line-height: var(--line-height-small);}
.ͼ1la .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1la .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1la .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1la .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1la.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1la .cm-cursor, .ͼ1la .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1la .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1la .cm-activeLine {background-color: var(--background-higher);}
.ͼ1la .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1la .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1la .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1la .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1la .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1la .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1la .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1la .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1la .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1la .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1la .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1la .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1la .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1la .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1la .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1la .cm-matchingBracket, .ͼ1la .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1la .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1la .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1la .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1la .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1la .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1la .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1la .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1la .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1la .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1la .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1la .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1la .cm-tooltip.multiplayer-tooltip, .ͼ1la .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1la .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1la .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1la .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1la .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1la .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1la .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1la .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1la .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1l2 {color: var(--foreground-default);}
.ͼ1l3 {color: var(--outline-stronger);}
.ͼ1l4 {color: var(--accent-red-default);}
.ͼ1l5 {color: var(--accent-orange-stronger);}
.ͼ1l6 {color: var(--accent-yellow-stronger);}
.ͼ1l7 {color: var(--accent-lime-stronger);}
.ͼ1l8 {color: var(--accent-green-stronger);}
.ͼ1l9 {color: var(--accent-teal-stronger);}
.ͼ1ku {color: var(--foreground-default);}
.ͼ1kv {color: var(--accent-green-default);}
.ͼ1kw {color: var(--accent-red-stronger);}
.ͼ1kx {color: var(--accent-orange-strongest);}
.ͼ1ky {color: var(--accent-yellow-strongest);}
.ͼ1kz {color: var(--accent-lime-strongest);}
.ͼ1l0 {color: var(--accent-green-strongest);}
.ͼ1l1 {color: var(--accent-teal-strongest);}
.ͼ1kh {text-decoration: underline;}
.ͼ1ki {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1kj {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1kk {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1kl {font-style: italic;}
.ͼ1km {font-weight: var(--font-weight-bold);}
.ͼ1kn {text-decoration: line-through;}
.ͼ1ko {font-family: var(--font-family-code);}
.ͼ1kp {color: var(--foreground-dimmest);}
.ͼ1kq {color: var(--accent-blue-strongest);}
.ͼ1kr {color: var(--accent-blue-stronger);}
.ͼ1ks {color: var(--accent-purple-stronger);}
.ͼ1kt {color: var(--accent-pink-stronger);}
.ͼ1ke.cm-focused {outline: 0 none;}
.ͼ1ke {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1ke .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1ke .cm-line {line-height: var(--line-height-small);}
.ͼ1ke .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1ke .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1ke .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1ke .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1ke.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1ke .cm-cursor, .ͼ1ke .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1ke .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1ke .cm-activeLine {background-color: var(--background-higher);}
.ͼ1ke .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1ke .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1ke .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1ke .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1ke .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1ke .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1ke .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1ke .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1ke .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1ke .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1ke .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1ke .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1ke .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1ke .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1ke .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1ke .cm-matchingBracket, .ͼ1ke .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1ke .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1ke .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1ke .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1ke .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1ke .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1ke .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1ke .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1ke .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1ke .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1ke .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1ke .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1ke .cm-tooltip.multiplayer-tooltip, .ͼ1ke .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1ke .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1ke .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1ke .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1ke .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1ke .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1ke .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1ke .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1ke .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1k6 {color: var(--foreground-default);}
.ͼ1k7 {color: var(--outline-stronger);}
.ͼ1k8 {color: var(--accent-red-default);}
.ͼ1k9 {color: var(--accent-orange-stronger);}
.ͼ1ka {color: var(--accent-yellow-stronger);}
.ͼ1kb {color: var(--accent-lime-stronger);}
.ͼ1kc {color: var(--accent-green-stronger);}
.ͼ1kd {color: var(--accent-teal-stronger);}
.ͼ1jy {color: var(--foreground-default);}
.ͼ1jz {color: var(--accent-green-default);}
.ͼ1k0 {color: var(--accent-red-stronger);}
.ͼ1k1 {color: var(--accent-orange-strongest);}
.ͼ1k2 {color: var(--accent-yellow-strongest);}
.ͼ1k3 {color: var(--accent-lime-strongest);}
.ͼ1k4 {color: var(--accent-green-strongest);}
.ͼ1k5 {color: var(--accent-teal-strongest);}
.ͼ1jl {text-decoration: underline;}
.ͼ1jm {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1jn {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1jo {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1jp {font-style: italic;}
.ͼ1jq {font-weight: var(--font-weight-bold);}
.ͼ1jr {text-decoration: line-through;}
.ͼ1js {font-family: var(--font-family-code);}
.ͼ1jt {color: var(--foreground-dimmest);}
.ͼ1ju {color: var(--accent-blue-strongest);}
.ͼ1jv {color: var(--accent-blue-stronger);}
.ͼ1jw {color: var(--accent-purple-stronger);}
.ͼ1jx {color: var(--accent-pink-stronger);}
.ͼ1jj.cm-focused {outline: 0 none;}
.ͼ1jj {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1jj .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1jj .cm-line {line-height: var(--line-height-small);}
.ͼ1jj .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1jj .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1jj .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1jj .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1jj.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1jj .cm-cursor, .ͼ1jj .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1jj .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1jj .cm-activeLine {background-color: var(--background-higher);}
.ͼ1jj .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1jj .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1jj .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1jj .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1jj .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1jj .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1jj .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1jj .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1jj .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1jj .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1jj .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1jj .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1jj .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1jj .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1jj .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1jj .cm-matchingBracket, .ͼ1jj .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1jj .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1jj .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1jj .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1jj .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1jj .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1jj .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1jj .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1jj .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1jj .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1jj .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1jj .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1jj .cm-tooltip.multiplayer-tooltip, .ͼ1jj .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1jj .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1jj .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1jj .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1jj .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1jj .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1jj .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1jj .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1jj .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1jb {color: var(--foreground-default);}
.ͼ1jc {color: var(--outline-stronger);}
.ͼ1jd {color: var(--accent-red-default);}
.ͼ1je {color: var(--accent-orange-stronger);}
.ͼ1jf {color: var(--accent-yellow-stronger);}
.ͼ1jg {color: var(--accent-lime-stronger);}
.ͼ1jh {color: var(--accent-green-stronger);}
.ͼ1ji {color: var(--accent-teal-stronger);}
.ͼ1j3 {color: var(--foreground-default);}
.ͼ1j4 {color: var(--accent-green-default);}
.ͼ1j5 {color: var(--accent-red-stronger);}
.ͼ1j6 {color: var(--accent-orange-strongest);}
.ͼ1j7 {color: var(--accent-yellow-strongest);}
.ͼ1j8 {color: var(--accent-lime-strongest);}
.ͼ1j9 {color: var(--accent-green-strongest);}
.ͼ1ja {color: var(--accent-teal-strongest);}
.ͼ1iq {text-decoration: underline;}
.ͼ1ir {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1is {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1it {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1iu {font-style: italic;}
.ͼ1iv {font-weight: var(--font-weight-bold);}
.ͼ1iw {text-decoration: line-through;}
.ͼ1ix {font-family: var(--font-family-code);}
.ͼ1iy {color: var(--foreground-dimmest);}
.ͼ1iz {color: var(--accent-blue-strongest);}
.ͼ1j0 {color: var(--accent-blue-stronger);}
.ͼ1j1 {color: var(--accent-purple-stronger);}
.ͼ1j2 {color: var(--accent-pink-stronger);}
.ͼ1io.cm-focused {outline: 0 none;}
.ͼ1io {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1io .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1io .cm-line {line-height: var(--line-height-small);}
.ͼ1io .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1io .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1io .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1io .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1io.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1io .cm-cursor, .ͼ1io .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1io .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1io .cm-activeLine {background-color: var(--background-higher);}
.ͼ1io .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1io .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1io .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1io .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1io .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1io .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1io .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1io .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1io .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1io .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1io .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1io .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1io .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1io .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1io .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1io .cm-matchingBracket, .ͼ1io .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1io .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1io .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1io .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1io .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1io .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1io .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1io .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1io .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1io .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1io .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1io .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1io .cm-tooltip.multiplayer-tooltip, .ͼ1io .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1io .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1io .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1io .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1io .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1io .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1io .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1io .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1io .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1ig {color: var(--foreground-default);}
.ͼ1ih {color: var(--outline-stronger);}
.ͼ1ii {color: var(--accent-red-default);}
.ͼ1ij {color: var(--accent-orange-stronger);}
.ͼ1ik {color: var(--accent-yellow-stronger);}
.ͼ1il {color: var(--accent-lime-stronger);}
.ͼ1im {color: var(--accent-green-stronger);}
.ͼ1in {color: var(--accent-teal-stronger);}
.ͼ1i8 {color: var(--foreground-default);}
.ͼ1i9 {color: var(--accent-green-default);}
.ͼ1ia {color: var(--accent-red-stronger);}
.ͼ1ib {color: var(--accent-orange-strongest);}
.ͼ1ic {color: var(--accent-yellow-strongest);}
.ͼ1id {color: var(--accent-lime-strongest);}
.ͼ1ie {color: var(--accent-green-strongest);}
.ͼ1if {color: var(--accent-teal-strongest);}
.ͼ1hv {text-decoration: underline;}
.ͼ1hw {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1hx {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1hy {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1hz {font-style: italic;}
.ͼ1i0 {font-weight: var(--font-weight-bold);}
.ͼ1i1 {text-decoration: line-through;}
.ͼ1i2 {font-family: var(--font-family-code);}
.ͼ1i3 {color: var(--foreground-dimmest);}
.ͼ1i4 {color: var(--accent-blue-strongest);}
.ͼ1i5 {color: var(--accent-blue-stronger);}
.ͼ1i6 {color: var(--accent-purple-stronger);}
.ͼ1i7 {color: var(--accent-pink-stronger);}
.ͼ1hu.cm-focused {outline: 0 none;}
.ͼ1hu {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1hu .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1hu .cm-line {line-height: var(--line-height-small);}
.ͼ1hu .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1hu .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1hu .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1hu .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1hu.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1hu .cm-cursor, .ͼ1hu .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1hu .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1hu .cm-activeLine {background-color: var(--background-higher);}
.ͼ1hu .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1hu .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1hu .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1hu .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1hu .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1hu .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1hu .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1hu .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1hu .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1hu .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1hu .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1hu .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1hu .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1hu .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1hu .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1hu .cm-matchingBracket, .ͼ1hu .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1hu .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1hu .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1hu .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1hu .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1hu .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1hu .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1hu .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1hu .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1hu .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1hu .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1hu .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1hu .cm-tooltip.multiplayer-tooltip, .ͼ1hu .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1hu .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1hu .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1hu .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1hu .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1hu .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1hu .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1hu .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1hu .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1hm {color: var(--foreground-default);}
.ͼ1hn {color: var(--outline-stronger);}
.ͼ1ho {color: var(--accent-red-default);}
.ͼ1hp {color: var(--accent-orange-stronger);}
.ͼ1hq {color: var(--accent-yellow-stronger);}
.ͼ1hr {color: var(--accent-lime-stronger);}
.ͼ1hs {color: var(--accent-green-stronger);}
.ͼ1ht {color: var(--accent-teal-stronger);}
.ͼ1he {color: var(--foreground-default);}
.ͼ1hf {color: var(--accent-green-default);}
.ͼ1hg {color: var(--accent-red-stronger);}
.ͼ1hh {color: var(--accent-orange-strongest);}
.ͼ1hi {color: var(--accent-yellow-strongest);}
.ͼ1hj {color: var(--accent-lime-strongest);}
.ͼ1hk {color: var(--accent-green-strongest);}
.ͼ1hl {color: var(--accent-teal-strongest);}
.ͼ1h1 {text-decoration: underline;}
.ͼ1h2 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1h3 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1h4 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1h5 {font-style: italic;}
.ͼ1h6 {font-weight: var(--font-weight-bold);}
.ͼ1h7 {text-decoration: line-through;}
.ͼ1h8 {font-family: var(--font-family-code);}
.ͼ1h9 {color: var(--foreground-dimmest);}
.ͼ1ha {color: var(--accent-blue-strongest);}
.ͼ1hb {color: var(--accent-blue-stronger);}
.ͼ1hc {color: var(--accent-purple-stronger);}
.ͼ1hd {color: var(--accent-pink-stronger);}
.ͼ1h0.cm-focused {outline: 0 none;}
.ͼ1h0 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1h0 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1h0 .cm-line {line-height: var(--line-height-small);}
.ͼ1h0 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1h0 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1h0 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1h0 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1h0.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1h0 .cm-cursor, .ͼ1h0 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1h0 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1h0 .cm-activeLine {background-color: var(--background-higher);}
.ͼ1h0 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1h0 .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1h0 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1h0 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1h0 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1h0 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1h0 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1h0 .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1h0 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1h0 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1h0 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1h0 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1h0 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1h0 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1h0 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1h0 .cm-matchingBracket, .ͼ1h0 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1h0 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1h0 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1h0 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1h0 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1h0 .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1h0 .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1h0 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1h0 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1h0 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1h0 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1h0 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1h0 .cm-tooltip.multiplayer-tooltip, .ͼ1h0 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1h0 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1h0 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1h0 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1h0 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1h0 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1h0 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1h0 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1h0 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1gs {color: var(--foreground-default);}
.ͼ1gt {color: var(--outline-stronger);}
.ͼ1gu {color: var(--accent-red-default);}
.ͼ1gv {color: var(--accent-orange-stronger);}
.ͼ1gw {color: var(--accent-yellow-stronger);}
.ͼ1gx {color: var(--accent-lime-stronger);}
.ͼ1gy {color: var(--accent-green-stronger);}
.ͼ1gz {color: var(--accent-teal-stronger);}
.ͼ1gk {color: var(--foreground-default);}
.ͼ1gl {color: var(--accent-green-default);}
.ͼ1gm {color: var(--accent-red-stronger);}
.ͼ1gn {color: var(--accent-orange-strongest);}
.ͼ1go {color: var(--accent-yellow-strongest);}
.ͼ1gp {color: var(--accent-lime-strongest);}
.ͼ1gq {color: var(--accent-green-strongest);}
.ͼ1gr {color: var(--accent-teal-strongest);}
.ͼ1g7 {text-decoration: underline;}
.ͼ1g8 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1g9 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1ga {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1gb {font-style: italic;}
.ͼ1gc {font-weight: var(--font-weight-bold);}
.ͼ1gd {text-decoration: line-through;}
.ͼ1ge {font-family: var(--font-family-code);}
.ͼ1gf {color: var(--foreground-dimmest);}
.ͼ1gg {color: var(--accent-blue-strongest);}
.ͼ1gh {color: var(--accent-blue-stronger);}
.ͼ1gi {color: var(--accent-purple-stronger);}
.ͼ1gj {color: var(--accent-pink-stronger);}
.ͼ1g6.cm-focused {outline: 0 none;}
.ͼ1g6 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1g6 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1g6 .cm-line {line-height: var(--line-height-small);}
.ͼ1g6 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1g6 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1g6 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1g6 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1g6.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1g6 .cm-cursor, .ͼ1g6 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1g6 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1g6 .cm-activeLine {background-color: var(--background-higher);}
.ͼ1g6 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1g6 .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1g6 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1g6 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1g6 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1g6 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1g6 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1g6 .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1g6 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1g6 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1g6 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1g6 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1g6 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1g6 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1g6 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1g6 .cm-matchingBracket, .ͼ1g6 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1g6 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1g6 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1g6 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1g6 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1g6 .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1g6 .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1g6 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1g6 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1g6 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1g6 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1g6 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1g6 .cm-tooltip.multiplayer-tooltip, .ͼ1g6 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1g6 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1g6 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1g6 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1g6 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1g6 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1g6 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1g6 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1g6 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1fy {color: var(--foreground-default);}
.ͼ1fz {color: var(--outline-stronger);}
.ͼ1g0 {color: var(--accent-red-default);}
.ͼ1g1 {color: var(--accent-orange-stronger);}
.ͼ1g2 {color: var(--accent-yellow-stronger);}
.ͼ1g3 {color: var(--accent-lime-stronger);}
.ͼ1g4 {color: var(--accent-green-stronger);}
.ͼ1g5 {color: var(--accent-teal-stronger);}
.ͼ1fq {color: var(--foreground-default);}
.ͼ1fr {color: var(--accent-green-default);}
.ͼ1fs {color: var(--accent-red-stronger);}
.ͼ1ft {color: var(--accent-orange-strongest);}
.ͼ1fu {color: var(--accent-yellow-strongest);}
.ͼ1fv {color: var(--accent-lime-strongest);}
.ͼ1fw {color: var(--accent-green-strongest);}
.ͼ1fx {color: var(--accent-teal-strongest);}
.ͼ1fd {text-decoration: underline;}
.ͼ1fe {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1ff {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1fg {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1fh {font-style: italic;}
.ͼ1fi {font-weight: var(--font-weight-bold);}
.ͼ1fj {text-decoration: line-through;}
.ͼ1fk {font-family: var(--font-family-code);}
.ͼ1fl {color: var(--foreground-dimmest);}
.ͼ1fm {color: var(--accent-blue-strongest);}
.ͼ1fn {color: var(--accent-blue-stronger);}
.ͼ1fo {color: var(--accent-purple-stronger);}
.ͼ1fp {color: var(--accent-pink-stronger);}
.ͼ1fc.cm-focused {outline: 0 none;}
.ͼ1fc {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1fc .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1fc .cm-line {line-height: var(--line-height-small);}
.ͼ1fc .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1fc .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1fc .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1fc .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1fc.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1fc .cm-cursor, .ͼ1fc .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1fc .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1fc .cm-activeLine {background-color: var(--background-higher);}
.ͼ1fc .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1fc .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1fc .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1fc .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1fc .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1fc .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1fc .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1fc .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1fc .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1fc .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1fc .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1fc .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1fc .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1fc .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1fc .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1fc .cm-matchingBracket, .ͼ1fc .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1fc .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1fc .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1fc .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1fc .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1fc .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1fc .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1fc .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1fc .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1fc .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1fc .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1fc .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1fc .cm-tooltip.multiplayer-tooltip, .ͼ1fc .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1fc .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1fc .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1fc .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1fc .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1fc .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1fc .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1fc .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1fc .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1f4 {color: var(--foreground-default);}
.ͼ1f5 {color: var(--outline-stronger);}
.ͼ1f6 {color: var(--accent-red-default);}
.ͼ1f7 {color: var(--accent-orange-stronger);}
.ͼ1f8 {color: var(--accent-yellow-stronger);}
.ͼ1f9 {color: var(--accent-lime-stronger);}
.ͼ1fa {color: var(--accent-green-stronger);}
.ͼ1fb {color: var(--accent-teal-stronger);}
.ͼ1ew {color: var(--foreground-default);}
.ͼ1ex {color: var(--accent-green-default);}
.ͼ1ey {color: var(--accent-red-stronger);}
.ͼ1ez {color: var(--accent-orange-strongest);}
.ͼ1f0 {color: var(--accent-yellow-strongest);}
.ͼ1f1 {color: var(--accent-lime-strongest);}
.ͼ1f2 {color: var(--accent-green-strongest);}
.ͼ1f3 {color: var(--accent-teal-strongest);}
.ͼ1ej {text-decoration: underline;}
.ͼ1ek {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1el {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1em {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1en {font-style: italic;}
.ͼ1eo {font-weight: var(--font-weight-bold);}
.ͼ1ep {text-decoration: line-through;}
.ͼ1eq {font-family: var(--font-family-code);}
.ͼ1er {color: var(--foreground-dimmest);}
.ͼ1es {color: var(--accent-blue-strongest);}
.ͼ1et {color: var(--accent-blue-stronger);}
.ͼ1eu {color: var(--accent-purple-stronger);}
.ͼ1ev {color: var(--accent-pink-stronger);}
.ͼ1ei.cm-focused {outline: 0 none;}
.ͼ1ei {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1ei .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1ei .cm-line {line-height: var(--line-height-small);}
.ͼ1ei .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1ei .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1ei .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1ei .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1ei.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1ei .cm-cursor, .ͼ1ei .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1ei .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1ei .cm-activeLine {background-color: var(--background-higher);}
.ͼ1ei .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1ei .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1ei .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1ei .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1ei .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1ei .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1ei .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1ei .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1ei .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1ei .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1ei .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1ei .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1ei .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1ei .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1ei .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1ei .cm-matchingBracket, .ͼ1ei .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1ei .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1ei .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1ei .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1ei .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1ei .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1ei .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1ei .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1ei .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1ei .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1ei .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1ei .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1ei .cm-tooltip.multiplayer-tooltip, .ͼ1ei .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1ei .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1ei .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1ei .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1ei .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1ei .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1ei .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1ei .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1ei .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1ea {color: var(--foreground-default);}
.ͼ1eb {color: var(--outline-stronger);}
.ͼ1ec {color: var(--accent-red-default);}
.ͼ1ed {color: var(--accent-orange-stronger);}
.ͼ1ee {color: var(--accent-yellow-stronger);}
.ͼ1ef {color: var(--accent-lime-stronger);}
.ͼ1eg {color: var(--accent-green-stronger);}
.ͼ1eh {color: var(--accent-teal-stronger);}
.ͼ1e2 {color: var(--foreground-default);}
.ͼ1e3 {color: var(--accent-green-default);}
.ͼ1e4 {color: var(--accent-red-stronger);}
.ͼ1e5 {color: var(--accent-orange-strongest);}
.ͼ1e6 {color: var(--accent-yellow-strongest);}
.ͼ1e7 {color: var(--accent-lime-strongest);}
.ͼ1e8 {color: var(--accent-green-strongest);}
.ͼ1e9 {color: var(--accent-teal-strongest);}
.ͼ1dp {text-decoration: underline;}
.ͼ1dq {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1dr {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1ds {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1dt {font-style: italic;}
.ͼ1du {font-weight: var(--font-weight-bold);}
.ͼ1dv {text-decoration: line-through;}
.ͼ1dw {font-family: var(--font-family-code);}
.ͼ1dx {color: var(--foreground-dimmest);}
.ͼ1dy {color: var(--accent-blue-strongest);}
.ͼ1dz {color: var(--accent-blue-stronger);}
.ͼ1e0 {color: var(--accent-purple-stronger);}
.ͼ1e1 {color: var(--accent-pink-stronger);}
.ͼ1do.cm-focused {outline: 0 none;}
.ͼ1do {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1do .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1do .cm-line {line-height: var(--line-height-small);}
.ͼ1do .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1do .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1do .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1do .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1do.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1do .cm-cursor, .ͼ1do .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1do .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1do .cm-activeLine {background-color: var(--background-higher);}
.ͼ1do .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1do .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1do .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1do .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1do .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1do .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1do .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1do .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1do .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1do .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1do .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1do .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1do .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1do .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1do .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1do .cm-matchingBracket, .ͼ1do .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1do .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1do .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1do .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1do .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1do .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1do .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1do .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1do .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1do .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1do .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1do .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1do .cm-tooltip.multiplayer-tooltip, .ͼ1do .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1do .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1do .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1do .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1do .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1do .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1do .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1do .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1do .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1dg {color: var(--foreground-default);}
.ͼ1dh {color: var(--outline-stronger);}
.ͼ1di {color: var(--accent-red-default);}
.ͼ1dj {color: var(--accent-orange-stronger);}
.ͼ1dk {color: var(--accent-yellow-stronger);}
.ͼ1dl {color: var(--accent-lime-stronger);}
.ͼ1dm {color: var(--accent-green-stronger);}
.ͼ1dn {color: var(--accent-teal-stronger);}
.ͼ1d8 {color: var(--foreground-default);}
.ͼ1d9 {color: var(--accent-green-default);}
.ͼ1da {color: var(--accent-red-stronger);}
.ͼ1db {color: var(--accent-orange-strongest);}
.ͼ1dc {color: var(--accent-yellow-strongest);}
.ͼ1dd {color: var(--accent-lime-strongest);}
.ͼ1de {color: var(--accent-green-strongest);}
.ͼ1df {color: var(--accent-teal-strongest);}
.ͼ1cv {text-decoration: underline;}
.ͼ1cw {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1cx {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1cy {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1cz {font-style: italic;}
.ͼ1d0 {font-weight: var(--font-weight-bold);}
.ͼ1d1 {text-decoration: line-through;}
.ͼ1d2 {font-family: var(--font-family-code);}
.ͼ1d3 {color: var(--foreground-dimmest);}
.ͼ1d4 {color: var(--accent-blue-strongest);}
.ͼ1d5 {color: var(--accent-blue-stronger);}
.ͼ1d6 {color: var(--accent-purple-stronger);}
.ͼ1d7 {color: var(--accent-pink-stronger);}
.ͼ1cu.cm-focused {outline: 0 none;}
.ͼ1cu {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1cu .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1cu .cm-line {line-height: var(--line-height-small);}
.ͼ1cu .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1cu .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1cu .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1cu .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1cu.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1cu .cm-cursor, .ͼ1cu .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1cu .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1cu .cm-activeLine {background-color: var(--background-higher);}
.ͼ1cu .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1cu .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1cu .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1cu .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1cu .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1cu .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1cu .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1cu .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1cu .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1cu .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1cu .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1cu .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1cu .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1cu .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1cu .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1cu .cm-matchingBracket, .ͼ1cu .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1cu .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1cu .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1cu .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1cu .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1cu .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1cu .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1cu .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1cu .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1cu .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1cu .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1cu .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1cu .cm-tooltip.multiplayer-tooltip, .ͼ1cu .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1cu .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1cu .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1cu .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1cu .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1cu .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1cu .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1cu .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1cu .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1cm {color: var(--foreground-default);}
.ͼ1cn {color: var(--outline-stronger);}
.ͼ1co {color: var(--accent-red-default);}
.ͼ1cp {color: var(--accent-orange-stronger);}
.ͼ1cq {color: var(--accent-yellow-stronger);}
.ͼ1cr {color: var(--accent-lime-stronger);}
.ͼ1cs {color: var(--accent-green-stronger);}
.ͼ1ct {color: var(--accent-teal-stronger);}
.ͼ1ce {color: var(--foreground-default);}
.ͼ1cf {color: var(--accent-green-default);}
.ͼ1cg {color: var(--accent-red-stronger);}
.ͼ1ch {color: var(--accent-orange-strongest);}
.ͼ1ci {color: var(--accent-yellow-strongest);}
.ͼ1cj {color: var(--accent-lime-strongest);}
.ͼ1ck {color: var(--accent-green-strongest);}
.ͼ1cl {color: var(--accent-teal-strongest);}
.ͼ1c1 {text-decoration: underline;}
.ͼ1c2 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1c3 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1c4 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1c5 {font-style: italic;}
.ͼ1c6 {font-weight: var(--font-weight-bold);}
.ͼ1c7 {text-decoration: line-through;}
.ͼ1c8 {font-family: var(--font-family-code);}
.ͼ1c9 {color: var(--foreground-dimmest);}
.ͼ1ca {color: var(--accent-blue-strongest);}
.ͼ1cb {color: var(--accent-blue-stronger);}
.ͼ1cc {color: var(--accent-purple-stronger);}
.ͼ1cd {color: var(--accent-pink-stronger);}
.ͼ1c0.cm-focused {outline: 0 none;}
.ͼ1c0 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1c0 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1c0 .cm-line {line-height: var(--line-height-small);}
.ͼ1c0 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1c0 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1c0 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1c0 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1c0.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1c0 .cm-cursor, .ͼ1c0 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1c0 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1c0 .cm-activeLine {background-color: var(--background-higher);}
.ͼ1c0 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1c0 .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1c0 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1c0 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1c0 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1c0 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1c0 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1c0 .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1c0 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1c0 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1c0 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1c0 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1c0 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1c0 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1c0 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1c0 .cm-matchingBracket, .ͼ1c0 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1c0 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1c0 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1c0 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1c0 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1c0 .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1c0 .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1c0 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1c0 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1c0 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1c0 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1c0 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1c0 .cm-tooltip.multiplayer-tooltip, .ͼ1c0 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1c0 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1c0 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1c0 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1c0 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1c0 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1c0 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1c0 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1c0 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1bs {color: var(--foreground-default);}
.ͼ1bt {color: var(--outline-stronger);}
.ͼ1bu {color: var(--accent-red-default);}
.ͼ1bv {color: var(--accent-orange-stronger);}
.ͼ1bw {color: var(--accent-yellow-stronger);}
.ͼ1bx {color: var(--accent-lime-stronger);}
.ͼ1by {color: var(--accent-green-stronger);}
.ͼ1bz {color: var(--accent-teal-stronger);}
.ͼ1bk {color: var(--foreground-default);}
.ͼ1bl {color: var(--accent-green-default);}
.ͼ1bm {color: var(--accent-red-stronger);}
.ͼ1bn {color: var(--accent-orange-strongest);}
.ͼ1bo {color: var(--accent-yellow-strongest);}
.ͼ1bp {color: var(--accent-lime-strongest);}
.ͼ1bq {color: var(--accent-green-strongest);}
.ͼ1br {color: var(--accent-teal-strongest);}
.ͼ1b7 {text-decoration: underline;}
.ͼ1b8 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1b9 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1ba {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1bb {font-style: italic;}
.ͼ1bc {font-weight: var(--font-weight-bold);}
.ͼ1bd {text-decoration: line-through;}
.ͼ1be {font-family: var(--font-family-code);}
.ͼ1bf {color: var(--foreground-dimmest);}
.ͼ1bg {color: var(--accent-blue-strongest);}
.ͼ1bh {color: var(--accent-blue-stronger);}
.ͼ1bi {color: var(--accent-purple-stronger);}
.ͼ1bj {color: var(--accent-pink-stronger);}
.ͼ1b6.cm-focused {outline: 0 none;}
.ͼ1b6 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1b6 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1b6 .cm-line {line-height: var(--line-height-small);}
.ͼ1b6 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1b6 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1b6 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1b6 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1b6.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1b6 .cm-cursor, .ͼ1b6 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1b6 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1b6 .cm-activeLine {background-color: var(--background-higher);}
.ͼ1b6 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1b6 .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1b6 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1b6 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1b6 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1b6 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1b6 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1b6 .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1b6 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1b6 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1b6 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1b6 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1b6 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1b6 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1b6 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1b6 .cm-matchingBracket, .ͼ1b6 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1b6 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1b6 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1b6 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1b6 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1b6 .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1b6 .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1b6 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1b6 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1b6 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1b6 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1b6 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1b6 .cm-tooltip.multiplayer-tooltip, .ͼ1b6 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1b6 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1b6 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1b6 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1b6 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1b6 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1b6 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1b6 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1b6 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1ay {color: var(--foreground-default);}
.ͼ1az {color: var(--outline-stronger);}
.ͼ1b0 {color: var(--accent-red-default);}
.ͼ1b1 {color: var(--accent-orange-stronger);}
.ͼ1b2 {color: var(--accent-yellow-stronger);}
.ͼ1b3 {color: var(--accent-lime-stronger);}
.ͼ1b4 {color: var(--accent-green-stronger);}
.ͼ1b5 {color: var(--accent-teal-stronger);}
.ͼ1aq {color: var(--foreground-default);}
.ͼ1ar {color: var(--accent-green-default);}
.ͼ1as {color: var(--accent-red-stronger);}
.ͼ1at {color: var(--accent-orange-strongest);}
.ͼ1au {color: var(--accent-yellow-strongest);}
.ͼ1av {color: var(--accent-lime-strongest);}
.ͼ1aw {color: var(--accent-green-strongest);}
.ͼ1ax {color: var(--accent-teal-strongest);}
.ͼ1ad {text-decoration: underline;}
.ͼ1ae {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1af {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1ag {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1ah {font-style: italic;}
.ͼ1ai {font-weight: var(--font-weight-bold);}
.ͼ1aj {text-decoration: line-through;}
.ͼ1ak {font-family: var(--font-family-code);}
.ͼ1al {color: var(--foreground-dimmest);}
.ͼ1am {color: var(--accent-blue-strongest);}
.ͼ1an {color: var(--accent-blue-stronger);}
.ͼ1ao {color: var(--accent-purple-stronger);}
.ͼ1ap {color: var(--accent-pink-stronger);}
.ͼ1ac.cm-focused {outline: 0 none;}
.ͼ1ac {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1ac .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ1ac .cm-line {line-height: var(--line-height-small);}
.ͼ1ac .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1ac .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1ac .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1ac .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1ac.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1ac .cm-cursor, .ͼ1ac .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1ac .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1ac .cm-activeLine {background-color: var(--background-higher);}
.ͼ1ac .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1ac .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1ac .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1ac .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1ac .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1ac .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1ac .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1ac .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1ac .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1ac .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1ac .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1ac .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1ac .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1ac .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1ac .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1ac .cm-matchingBracket, .ͼ1ac .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1ac .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1ac .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1ac .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1ac .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1ac .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1ac .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1ac .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1ac .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1ac .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1ac .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1ac .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1ac .cm-tooltip.multiplayer-tooltip, .ͼ1ac .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1ac .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1ac .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1ac .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1ac .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1ac .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1ac .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1ac .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1ac .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1a4 {color: var(--foreground-default);}
.ͼ1a5 {color: var(--outline-stronger);}
.ͼ1a6 {color: var(--accent-red-default);}
.ͼ1a7 {color: var(--accent-orange-stronger);}
.ͼ1a8 {color: var(--accent-yellow-stronger);}
.ͼ1a9 {color: var(--accent-lime-stronger);}
.ͼ1aa {color: var(--accent-green-stronger);}
.ͼ1ab {color: var(--accent-teal-stronger);}
.ͼ19w {color: var(--foreground-default);}
.ͼ19x {color: var(--accent-green-default);}
.ͼ19y {color: var(--accent-red-stronger);}
.ͼ19z {color: var(--accent-orange-strongest);}
.ͼ1a0 {color: var(--accent-yellow-strongest);}
.ͼ1a1 {color: var(--accent-lime-strongest);}
.ͼ1a2 {color: var(--accent-green-strongest);}
.ͼ1a3 {color: var(--accent-teal-strongest);}
.ͼ19j {text-decoration: underline;}
.ͼ19k {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ19l {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ19m {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ19n {font-style: italic;}
.ͼ19o {font-weight: var(--font-weight-bold);}
.ͼ19p {text-decoration: line-through;}
.ͼ19q {font-family: var(--font-family-code);}
.ͼ19r {color: var(--foreground-dimmest);}
.ͼ19s {color: var(--accent-blue-strongest);}
.ͼ19t {color: var(--accent-blue-stronger);}
.ͼ19u {color: var(--accent-purple-stronger);}
.ͼ19v {color: var(--accent-pink-stronger);}
.ͼ19i.cm-focused {outline: 0 none;}
.ͼ19i {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ19i .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ19i .cm-line {line-height: var(--line-height-small);}
.ͼ19i .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ19i .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ19i .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ19i .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ19i.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ19i .cm-cursor, .ͼ19i .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ19i .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ19i .cm-activeLine {background-color: var(--background-higher);}
.ͼ19i .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ19i .cm-specialChar {color: var(--accent-negative-default);}
.ͼ19i .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ19i .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ19i .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ19i .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ19i .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ19i .cm-vim-panel input {color: var(--foreground-default);}
.ͼ19i .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ19i .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ19i .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ19i .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ19i .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ19i .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ19i .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ19i .cm-matchingBracket, .ͼ19i .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ19i .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ19i .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ19i .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ19i .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ19i .emmet-preview .cm-content {padding: 0 !important;}
.ͼ19i .emmet-preview .cm-scroller {z-index: 1;}
.ͼ19i .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ19i .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ19i .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ19i .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ19i .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ19i .cm-tooltip.multiplayer-tooltip, .ͼ19i .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ19i .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ19i .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ19i .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ19i .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ19i .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ19i .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ19i .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ19i .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ19a {color: var(--foreground-default);}
.ͼ19b {color: var(--outline-stronger);}
.ͼ19c {color: var(--accent-red-default);}
.ͼ19d {color: var(--accent-orange-stronger);}
.ͼ19e {color: var(--accent-yellow-stronger);}
.ͼ19f {color: var(--accent-lime-stronger);}
.ͼ19g {color: var(--accent-green-stronger);}
.ͼ19h {color: var(--accent-teal-stronger);}
.ͼ192 {color: var(--foreground-default);}
.ͼ193 {color: var(--accent-green-default);}
.ͼ194 {color: var(--accent-red-stronger);}
.ͼ195 {color: var(--accent-orange-strongest);}
.ͼ196 {color: var(--accent-yellow-strongest);}
.ͼ197 {color: var(--accent-lime-strongest);}
.ͼ198 {color: var(--accent-green-strongest);}
.ͼ199 {color: var(--accent-teal-strongest);}
.ͼ18p {text-decoration: underline;}
.ͼ18q {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ18r {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ18s {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ18t {font-style: italic;}
.ͼ18u {font-weight: var(--font-weight-bold);}
.ͼ18v {text-decoration: line-through;}
.ͼ18w {font-family: var(--font-family-code);}
.ͼ18x {color: var(--foreground-dimmest);}
.ͼ18y {color: var(--accent-blue-strongest);}
.ͼ18z {color: var(--accent-blue-stronger);}
.ͼ190 {color: var(--accent-purple-stronger);}
.ͼ191 {color: var(--accent-pink-stronger);}
.ͼ18o.cm-focused {outline: 0 none;}
.ͼ18o {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ18o .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ18o .cm-line {line-height: var(--line-height-small);}
.ͼ18o .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ18o .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ18o .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ18o .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ18o.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ18o .cm-cursor, .ͼ18o .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ18o .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ18o .cm-activeLine {background-color: var(--background-higher);}
.ͼ18o .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ18o .cm-specialChar {color: var(--accent-negative-default);}
.ͼ18o .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ18o .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ18o .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ18o .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ18o .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ18o .cm-vim-panel input {color: var(--foreground-default);}
.ͼ18o .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ18o .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ18o .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ18o .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ18o .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ18o .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ18o .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ18o .cm-matchingBracket, .ͼ18o .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ18o .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ18o .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ18o .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ18o .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ18o .emmet-preview .cm-content {padding: 0 !important;}
.ͼ18o .emmet-preview .cm-scroller {z-index: 1;}
.ͼ18o .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ18o .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ18o .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ18o .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ18o .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ18o .cm-tooltip.multiplayer-tooltip, .ͼ18o .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ18o .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ18o .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ18o .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ18o .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ18o .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ18o .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ18o .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ18o .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ18g {color: var(--foreground-default);}
.ͼ18h {color: var(--outline-stronger);}
.ͼ18i {color: var(--accent-red-default);}
.ͼ18j {color: var(--accent-orange-stronger);}
.ͼ18k {color: var(--accent-yellow-stronger);}
.ͼ18l {color: var(--accent-lime-stronger);}
.ͼ18m {color: var(--accent-green-stronger);}
.ͼ18n {color: var(--accent-teal-stronger);}
.ͼ188 {color: var(--foreground-default);}
.ͼ189 {color: var(--accent-green-default);}
.ͼ18a {color: var(--accent-red-stronger);}
.ͼ18b {color: var(--accent-orange-strongest);}
.ͼ18c {color: var(--accent-yellow-strongest);}
.ͼ18d {color: var(--accent-lime-strongest);}
.ͼ18e {color: var(--accent-green-strongest);}
.ͼ18f {color: var(--accent-teal-strongest);}
.ͼ17v {text-decoration: underline;}
.ͼ17w {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ17x {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ17y {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ17z {font-style: italic;}
.ͼ180 {font-weight: var(--font-weight-bold);}
.ͼ181 {text-decoration: line-through;}
.ͼ182 {font-family: var(--font-family-code);}
.ͼ183 {color: var(--foreground-dimmest);}
.ͼ184 {color: var(--accent-blue-strongest);}
.ͼ185 {color: var(--accent-blue-stronger);}
.ͼ186 {color: var(--accent-purple-stronger);}
.ͼ187 {color: var(--accent-pink-stronger);}
.ͼ17u.cm-focused {outline: 0 none;}
.ͼ17u {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ17u .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ17u .cm-line {line-height: var(--line-height-small);}
.ͼ17u .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ17u .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ17u .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ17u .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ17u.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ17u .cm-cursor, .ͼ17u .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ17u .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ17u .cm-activeLine {background-color: var(--background-higher);}
.ͼ17u .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ17u .cm-specialChar {color: var(--accent-negative-default);}
.ͼ17u .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ17u .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ17u .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ17u .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ17u .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ17u .cm-vim-panel input {color: var(--foreground-default);}
.ͼ17u .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ17u .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ17u .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ17u .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ17u .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ17u .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ17u .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ17u .cm-matchingBracket, .ͼ17u .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ17u .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ17u .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ17u .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ17u .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ17u .emmet-preview .cm-content {padding: 0 !important;}
.ͼ17u .emmet-preview .cm-scroller {z-index: 1;}
.ͼ17u .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ17u .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ17u .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ17u .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ17u .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ17u .cm-tooltip.multiplayer-tooltip, .ͼ17u .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ17u .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ17u .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ17u .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ17u .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ17u .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ17u .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ17u .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ17u .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ17m {color: var(--foreground-default);}
.ͼ17n {color: var(--outline-stronger);}
.ͼ17o {color: var(--accent-red-default);}
.ͼ17p {color: var(--accent-orange-stronger);}
.ͼ17q {color: var(--accent-yellow-stronger);}
.ͼ17r {color: var(--accent-lime-stronger);}
.ͼ17s {color: var(--accent-green-stronger);}
.ͼ17t {color: var(--accent-teal-stronger);}
.ͼ17e {color: var(--foreground-default);}
.ͼ17f {color: var(--accent-green-default);}
.ͼ17g {color: var(--accent-red-stronger);}
.ͼ17h {color: var(--accent-orange-strongest);}
.ͼ17i {color: var(--accent-yellow-strongest);}
.ͼ17j {color: var(--accent-lime-strongest);}
.ͼ17k {color: var(--accent-green-strongest);}
.ͼ17l {color: var(--accent-teal-strongest);}
.ͼ171 {text-decoration: underline;}
.ͼ172 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ173 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ174 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ175 {font-style: italic;}
.ͼ176 {font-weight: var(--font-weight-bold);}
.ͼ177 {text-decoration: line-through;}
.ͼ178 {font-family: var(--font-family-code);}
.ͼ179 {color: var(--foreground-dimmest);}
.ͼ17a {color: var(--accent-blue-strongest);}
.ͼ17b {color: var(--accent-blue-stronger);}
.ͼ17c {color: var(--accent-purple-stronger);}
.ͼ17d {color: var(--accent-pink-stronger);}
.ͼ170.cm-focused {outline: 0 none;}
.ͼ170 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ170 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ170 .cm-line {line-height: var(--line-height-small);}
.ͼ170 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ170 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ170 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ170 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ170.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ170 .cm-cursor, .ͼ170 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ170 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ170 .cm-activeLine {background-color: var(--background-higher);}
.ͼ170 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ170 .cm-specialChar {color: var(--accent-negative-default);}
.ͼ170 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ170 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ170 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ170 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ170 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ170 .cm-vim-panel input {color: var(--foreground-default);}
.ͼ170 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ170 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ170 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ170 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ170 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ170 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ170 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ170 .cm-matchingBracket, .ͼ170 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ170 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ170 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ170 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ170 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ170 .emmet-preview .cm-content {padding: 0 !important;}
.ͼ170 .emmet-preview .cm-scroller {z-index: 1;}
.ͼ170 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ170 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ170 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ170 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ170 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ170 .cm-tooltip.multiplayer-tooltip, .ͼ170 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ170 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ170 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ170 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ170 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ170 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ170 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ170 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ170 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ16s {color: var(--foreground-default);}
.ͼ16t {color: var(--outline-stronger);}
.ͼ16u {color: var(--accent-red-default);}
.ͼ16v {color: var(--accent-orange-stronger);}
.ͼ16w {color: var(--accent-yellow-stronger);}
.ͼ16x {color: var(--accent-lime-stronger);}
.ͼ16y {color: var(--accent-green-stronger);}
.ͼ16z {color: var(--accent-teal-stronger);}
.ͼ16k {color: var(--foreground-default);}
.ͼ16l {color: var(--accent-green-default);}
.ͼ16m {color: var(--accent-red-stronger);}
.ͼ16n {color: var(--accent-orange-strongest);}
.ͼ16o {color: var(--accent-yellow-strongest);}
.ͼ16p {color: var(--accent-lime-strongest);}
.ͼ16q {color: var(--accent-green-strongest);}
.ͼ16r {color: var(--accent-teal-strongest);}
.ͼ167 {text-decoration: underline;}
.ͼ168 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ169 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ16a {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ16b {font-style: italic;}
.ͼ16c {font-weight: var(--font-weight-bold);}
.ͼ16d {text-decoration: line-through;}
.ͼ16e {font-family: var(--font-family-code);}
.ͼ16f {color: var(--foreground-dimmest);}
.ͼ16g {color: var(--accent-blue-strongest);}
.ͼ16h {color: var(--accent-blue-stronger);}
.ͼ16i {color: var(--accent-purple-stronger);}
.ͼ16j {color: var(--accent-pink-stronger);}
.ͼ166.cm-focused {outline: 0 none;}
.ͼ166 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ166 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ166 .cm-line {line-height: var(--line-height-small);}
.ͼ166 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ166 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ166 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ166 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ166.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ166 .cm-cursor, .ͼ166 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ166 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ166 .cm-activeLine {background-color: var(--background-higher);}
.ͼ166 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ166 .cm-specialChar {color: var(--accent-negative-default);}
.ͼ166 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ166 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ166 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ166 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ166 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ166 .cm-vim-panel input {color: var(--foreground-default);}
.ͼ166 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ166 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ166 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ166 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ166 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ166 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ166 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ166 .cm-matchingBracket, .ͼ166 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ166 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ166 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ166 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ166 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ166 .emmet-preview .cm-content {padding: 0 !important;}
.ͼ166 .emmet-preview .cm-scroller {z-index: 1;}
.ͼ166 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ166 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ166 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ166 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ166 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ166 .cm-tooltip.multiplayer-tooltip, .ͼ166 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ166 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ166 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ166 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ166 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ166 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ166 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ166 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ166 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ15y {color: var(--foreground-default);}
.ͼ15z {color: var(--outline-stronger);}
.ͼ160 {color: var(--accent-red-default);}
.ͼ161 {color: var(--accent-orange-stronger);}
.ͼ162 {color: var(--accent-yellow-stronger);}
.ͼ163 {color: var(--accent-lime-stronger);}
.ͼ164 {color: var(--accent-green-stronger);}
.ͼ165 {color: var(--accent-teal-stronger);}
.ͼ15q {color: var(--foreground-default);}
.ͼ15r {color: var(--accent-green-default);}
.ͼ15s {color: var(--accent-red-stronger);}
.ͼ15t {color: var(--accent-orange-strongest);}
.ͼ15u {color: var(--accent-yellow-strongest);}
.ͼ15v {color: var(--accent-lime-strongest);}
.ͼ15w {color: var(--accent-green-strongest);}
.ͼ15x {color: var(--accent-teal-strongest);}
.ͼ15d {text-decoration: underline;}
.ͼ15e {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ15f {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ15g {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ15h {font-style: italic;}
.ͼ15i {font-weight: var(--font-weight-bold);}
.ͼ15j {text-decoration: line-through;}
.ͼ15k {font-family: var(--font-family-code);}
.ͼ15l {color: var(--foreground-dimmest);}
.ͼ15m {color: var(--accent-blue-strongest);}
.ͼ15n {color: var(--accent-blue-stronger);}
.ͼ15o {color: var(--accent-purple-stronger);}
.ͼ15p {color: var(--accent-pink-stronger);}
.ͼ15c.cm-focused {outline: 0 none;}
.ͼ15c {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ15c .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ15c .cm-line {line-height: var(--line-height-small);}
.ͼ15c .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ15c .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ15c .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ15c .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ15c.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ15c .cm-cursor, .ͼ15c .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ15c .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ15c .cm-activeLine {background-color: var(--background-higher);}
.ͼ15c .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ15c .cm-specialChar {color: var(--accent-negative-default);}
.ͼ15c .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ15c .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ15c .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ15c .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ15c .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ15c .cm-vim-panel input {color: var(--foreground-default);}
.ͼ15c .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ15c .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ15c .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ15c .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ15c .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ15c .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ15c .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ15c .cm-matchingBracket, .ͼ15c .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ15c .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ15c .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ15c .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ15c .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ15c .emmet-preview .cm-content {padding: 0 !important;}
.ͼ15c .emmet-preview .cm-scroller {z-index: 1;}
.ͼ15c .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ15c .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ15c .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ15c .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ15c .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ15c .cm-tooltip.multiplayer-tooltip, .ͼ15c .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ15c .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ15c .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ15c .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ15c .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ15c .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ15c .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ15c .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ15c .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ154 {color: var(--foreground-default);}
.ͼ155 {color: var(--outline-stronger);}
.ͼ156 {color: var(--accent-red-default);}
.ͼ157 {color: var(--accent-orange-stronger);}
.ͼ158 {color: var(--accent-yellow-stronger);}
.ͼ159 {color: var(--accent-lime-stronger);}
.ͼ15a {color: var(--accent-green-stronger);}
.ͼ15b {color: var(--accent-teal-stronger);}
.ͼ14w {color: var(--foreground-default);}
.ͼ14x {color: var(--accent-green-default);}
.ͼ14y {color: var(--accent-red-stronger);}
.ͼ14z {color: var(--accent-orange-strongest);}
.ͼ150 {color: var(--accent-yellow-strongest);}
.ͼ151 {color: var(--accent-lime-strongest);}
.ͼ152 {color: var(--accent-green-strongest);}
.ͼ153 {color: var(--accent-teal-strongest);}
.ͼ14j {text-decoration: underline;}
.ͼ14k {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ14l {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ14m {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ14n {font-style: italic;}
.ͼ14o {font-weight: var(--font-weight-bold);}
.ͼ14p {text-decoration: line-through;}
.ͼ14q {font-family: var(--font-family-code);}
.ͼ14r {color: var(--foreground-dimmest);}
.ͼ14s {color: var(--accent-blue-strongest);}
.ͼ14t {color: var(--accent-blue-stronger);}
.ͼ14u {color: var(--accent-purple-stronger);}
.ͼ14v {color: var(--accent-pink-stronger);}
.ͼ14i.cm-focused {outline: 0 none;}
.ͼ14i {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ14i .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ14i .cm-line {line-height: var(--line-height-small);}
.ͼ14i .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ14i .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ14i .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ14i .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ14i.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ14i .cm-cursor, .ͼ14i .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ14i .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ14i .cm-activeLine {background-color: var(--background-higher);}
.ͼ14i .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ14i .cm-specialChar {color: var(--accent-negative-default);}
.ͼ14i .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ14i .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ14i .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ14i .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ14i .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ14i .cm-vim-panel input {color: var(--foreground-default);}
.ͼ14i .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ14i .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ14i .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ14i .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ14i .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ14i .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ14i .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ14i .cm-matchingBracket, .ͼ14i .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ14i .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ14i .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ14i .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ14i .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ14i .emmet-preview .cm-content {padding: 0 !important;}
.ͼ14i .emmet-preview .cm-scroller {z-index: 1;}
.ͼ14i .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ14i .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ14i .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ14i .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ14i .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ14i .cm-tooltip.multiplayer-tooltip, .ͼ14i .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ14i .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ14i .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ14i .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ14i .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ14i .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ14i .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ14i .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ14i .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ14a {color: var(--foreground-default);}
.ͼ14b {color: var(--outline-stronger);}
.ͼ14c {color: var(--accent-red-default);}
.ͼ14d {color: var(--accent-orange-stronger);}
.ͼ14e {color: var(--accent-yellow-stronger);}
.ͼ14f {color: var(--accent-lime-stronger);}
.ͼ14g {color: var(--accent-green-stronger);}
.ͼ14h {color: var(--accent-teal-stronger);}
.ͼ142 {color: var(--foreground-default);}
.ͼ143 {color: var(--accent-green-default);}
.ͼ144 {color: var(--accent-red-stronger);}
.ͼ145 {color: var(--accent-orange-strongest);}
.ͼ146 {color: var(--accent-yellow-strongest);}
.ͼ147 {color: var(--accent-lime-strongest);}
.ͼ148 {color: var(--accent-green-strongest);}
.ͼ149 {color: var(--accent-teal-strongest);}
.ͼ13p {text-decoration: underline;}
.ͼ13q {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ13r {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ13s {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ13t {font-style: italic;}
.ͼ13u {font-weight: var(--font-weight-bold);}
.ͼ13v {text-decoration: line-through;}
.ͼ13w {font-family: var(--font-family-code);}
.ͼ13x {color: var(--foreground-dimmest);}
.ͼ13y {color: var(--accent-blue-strongest);}
.ͼ13z {color: var(--accent-blue-stronger);}
.ͼ140 {color: var(--accent-purple-stronger);}
.ͼ141 {color: var(--accent-pink-stronger);}
.ͼ13o.cm-focused {outline: 0 none;}
.ͼ13o {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ13o .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ13o .cm-line {line-height: var(--line-height-small);}
.ͼ13o .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ13o .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ13o .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ13o .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ13o.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ13o .cm-cursor, .ͼ13o .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ13o .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ13o .cm-activeLine {background-color: var(--background-higher);}
.ͼ13o .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ13o .cm-specialChar {color: var(--accent-negative-default);}
.ͼ13o .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ13o .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ13o .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ13o .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ13o .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ13o .cm-vim-panel input {color: var(--foreground-default);}
.ͼ13o .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ13o .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ13o .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ13o .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ13o .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ13o .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ13o .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ13o .cm-matchingBracket, .ͼ13o .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ13o .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ13o .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ13o .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ13o .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ13o .emmet-preview .cm-content {padding: 0 !important;}
.ͼ13o .emmet-preview .cm-scroller {z-index: 1;}
.ͼ13o .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ13o .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ13o .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ13o .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ13o .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ13o .cm-tooltip.multiplayer-tooltip, .ͼ13o .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ13o .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ13o .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ13o .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ13o .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ13o .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ13o .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ13o .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ13o .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ13g {color: var(--foreground-default);}
.ͼ13h {color: var(--outline-stronger);}
.ͼ13i {color: var(--accent-red-default);}
.ͼ13j {color: var(--accent-orange-stronger);}
.ͼ13k {color: var(--accent-yellow-stronger);}
.ͼ13l {color: var(--accent-lime-stronger);}
.ͼ13m {color: var(--accent-green-stronger);}
.ͼ13n {color: var(--accent-teal-stronger);}
.ͼ138 {color: var(--foreground-default);}
.ͼ139 {color: var(--accent-green-default);}
.ͼ13a {color: var(--accent-red-stronger);}
.ͼ13b {color: var(--accent-orange-strongest);}
.ͼ13c {color: var(--accent-yellow-strongest);}
.ͼ13d {color: var(--accent-lime-strongest);}
.ͼ13e {color: var(--accent-green-strongest);}
.ͼ13f {color: var(--accent-teal-strongest);}
.ͼ12v {text-decoration: underline;}
.ͼ12w {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ12x {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ12y {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ12z {font-style: italic;}
.ͼ130 {font-weight: var(--font-weight-bold);}
.ͼ131 {text-decoration: line-through;}
.ͼ132 {font-family: var(--font-family-code);}
.ͼ133 {color: var(--foreground-dimmest);}
.ͼ134 {color: var(--accent-blue-strongest);}
.ͼ135 {color: var(--accent-blue-stronger);}
.ͼ136 {color: var(--accent-purple-stronger);}
.ͼ137 {color: var(--accent-pink-stronger);}
.ͼ12u.cm-focused {outline: 0 none;}
.ͼ12u {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ12u .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ12u .cm-line {line-height: var(--line-height-small);}
.ͼ12u .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ12u .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ12u .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ12u .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ12u.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ12u .cm-cursor, .ͼ12u .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ12u .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ12u .cm-activeLine {background-color: var(--background-higher);}
.ͼ12u .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ12u .cm-specialChar {color: var(--accent-negative-default);}
.ͼ12u .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ12u .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ12u .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ12u .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ12u .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ12u .cm-vim-panel input {color: var(--foreground-default);}
.ͼ12u .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ12u .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ12u .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ12u .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ12u .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ12u .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ12u .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ12u .cm-matchingBracket, .ͼ12u .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ12u .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ12u .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ12u .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ12u .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ12u .emmet-preview .cm-content {padding: 0 !important;}
.ͼ12u .emmet-preview .cm-scroller {z-index: 1;}
.ͼ12u .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ12u .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ12u .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ12u .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ12u .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ12u .cm-tooltip.multiplayer-tooltip, .ͼ12u .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ12u .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ12u .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ12u .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ12u .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ12u .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ12u .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ12u .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ12u .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ12m {color: var(--foreground-default);}
.ͼ12n {color: var(--outline-stronger);}
.ͼ12o {color: var(--accent-red-default);}
.ͼ12p {color: var(--accent-orange-stronger);}
.ͼ12q {color: var(--accent-yellow-stronger);}
.ͼ12r {color: var(--accent-lime-stronger);}
.ͼ12s {color: var(--accent-green-stronger);}
.ͼ12t {color: var(--accent-teal-stronger);}
.ͼ12e {color: var(--foreground-default);}
.ͼ12f {color: var(--accent-green-default);}
.ͼ12g {color: var(--accent-red-stronger);}
.ͼ12h {color: var(--accent-orange-strongest);}
.ͼ12i {color: var(--accent-yellow-strongest);}
.ͼ12j {color: var(--accent-lime-strongest);}
.ͼ12k {color: var(--accent-green-strongest);}
.ͼ12l {color: var(--accent-teal-strongest);}
.ͼ121 {text-decoration: underline;}
.ͼ122 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ123 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ124 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ125 {font-style: italic;}
.ͼ126 {font-weight: var(--font-weight-bold);}
.ͼ127 {text-decoration: line-through;}
.ͼ128 {font-family: var(--font-family-code);}
.ͼ129 {color: var(--foreground-dimmest);}
.ͼ12a {color: var(--accent-blue-strongest);}
.ͼ12b {color: var(--accent-blue-stronger);}
.ͼ12c {color: var(--accent-purple-stronger);}
.ͼ12d {color: var(--accent-pink-stronger);}
.ͼ120.cm-focused {outline: 0 none;}
.ͼ120 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ120 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ120 .cm-line {line-height: var(--line-height-small);}
.ͼ120 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ120 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ120 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ120 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ120.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ120 .cm-cursor, .ͼ120 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ120 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ120 .cm-activeLine {background-color: var(--background-higher);}
.ͼ120 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ120 .cm-specialChar {color: var(--accent-negative-default);}
.ͼ120 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ120 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ120 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ120 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ120 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ120 .cm-vim-panel input {color: var(--foreground-default);}
.ͼ120 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ120 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ120 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ120 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ120 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ120 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ120 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ120 .cm-matchingBracket, .ͼ120 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ120 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ120 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ120 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ120 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ120 .emmet-preview .cm-content {padding: 0 !important;}
.ͼ120 .emmet-preview .cm-scroller {z-index: 1;}
.ͼ120 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ120 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ120 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ120 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ120 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ120 .cm-tooltip.multiplayer-tooltip, .ͼ120 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ120 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ120 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ120 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ120 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ120 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ120 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ120 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ120 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ11s {color: var(--foreground-default);}
.ͼ11t {color: var(--outline-stronger);}
.ͼ11u {color: var(--accent-red-default);}
.ͼ11v {color: var(--accent-orange-stronger);}
.ͼ11w {color: var(--accent-yellow-stronger);}
.ͼ11x {color: var(--accent-lime-stronger);}
.ͼ11y {color: var(--accent-green-stronger);}
.ͼ11z {color: var(--accent-teal-stronger);}
.ͼ11k {color: var(--foreground-default);}
.ͼ11l {color: var(--accent-green-default);}
.ͼ11m {color: var(--accent-red-stronger);}
.ͼ11n {color: var(--accent-orange-strongest);}
.ͼ11o {color: var(--accent-yellow-strongest);}
.ͼ11p {color: var(--accent-lime-strongest);}
.ͼ11q {color: var(--accent-green-strongest);}
.ͼ11r {color: var(--accent-teal-strongest);}
.ͼ117 {text-decoration: underline;}
.ͼ118 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ119 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ11a {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ11b {font-style: italic;}
.ͼ11c {font-weight: var(--font-weight-bold);}
.ͼ11d {text-decoration: line-through;}
.ͼ11e {font-family: var(--font-family-code);}
.ͼ11f {color: var(--foreground-dimmest);}
.ͼ11g {color: var(--accent-blue-strongest);}
.ͼ11h {color: var(--accent-blue-stronger);}
.ͼ11i {color: var(--accent-purple-stronger);}
.ͼ11j {color: var(--accent-pink-stronger);}
.ͼ116.cm-focused {outline: 0 none;}
.ͼ116 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ116 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ116 .cm-line {line-height: var(--line-height-small);}
.ͼ116 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ116 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ116 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ116 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ116.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ116 .cm-cursor, .ͼ116 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ116 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ116 .cm-activeLine {background-color: var(--background-higher);}
.ͼ116 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ116 .cm-specialChar {color: var(--accent-negative-default);}
.ͼ116 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ116 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ116 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ116 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ116 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ116 .cm-vim-panel input {color: var(--foreground-default);}
.ͼ116 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ116 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ116 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ116 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ116 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ116 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ116 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ116 .cm-matchingBracket, .ͼ116 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ116 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ116 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ116 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ116 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ116 .emmet-preview .cm-content {padding: 0 !important;}
.ͼ116 .emmet-preview .cm-scroller {z-index: 1;}
.ͼ116 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ116 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ116 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ116 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ116 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ116 .cm-tooltip.multiplayer-tooltip, .ͼ116 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ116 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ116 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ116 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ116 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ116 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ116 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ116 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ116 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ10y {color: var(--foreground-default);}
.ͼ10z {color: var(--outline-stronger);}
.ͼ110 {color: var(--accent-red-default);}
.ͼ111 {color: var(--accent-orange-stronger);}
.ͼ112 {color: var(--accent-yellow-stronger);}
.ͼ113 {color: var(--accent-lime-stronger);}
.ͼ114 {color: var(--accent-green-stronger);}
.ͼ115 {color: var(--accent-teal-stronger);}
.ͼ10q {color: var(--foreground-default);}
.ͼ10r {color: var(--accent-green-default);}
.ͼ10s {color: var(--accent-red-stronger);}
.ͼ10t {color: var(--accent-orange-strongest);}
.ͼ10u {color: var(--accent-yellow-strongest);}
.ͼ10v {color: var(--accent-lime-strongest);}
.ͼ10w {color: var(--accent-green-strongest);}
.ͼ10x {color: var(--accent-teal-strongest);}
.ͼ10d {text-decoration: underline;}
.ͼ10e {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ10f {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ10g {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ10h {font-style: italic;}
.ͼ10i {font-weight: var(--font-weight-bold);}
.ͼ10j {text-decoration: line-through;}
.ͼ10k {font-family: var(--font-family-code);}
.ͼ10l {color: var(--foreground-dimmest);}
.ͼ10m {color: var(--accent-blue-strongest);}
.ͼ10n {color: var(--accent-blue-stronger);}
.ͼ10o {color: var(--accent-purple-stronger);}
.ͼ10p {color: var(--accent-pink-stronger);}
.ͼ10c.cm-focused {outline: 0 none;}
.ͼ10c {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ10c .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ10c .cm-line {line-height: var(--line-height-small);}
.ͼ10c .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ10c .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ10c .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ10c .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ10c.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ10c .cm-cursor, .ͼ10c .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ10c .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ10c .cm-activeLine {background-color: var(--background-higher);}
.ͼ10c .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ10c .cm-specialChar {color: var(--accent-negative-default);}
.ͼ10c .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ10c .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ10c .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ10c .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ10c .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ10c .cm-vim-panel input {color: var(--foreground-default);}
.ͼ10c .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ10c .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ10c .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ10c .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ10c .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ10c .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ10c .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ10c .cm-matchingBracket, .ͼ10c .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ10c .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ10c .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ10c .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ10c .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ10c .emmet-preview .cm-content {padding: 0 !important;}
.ͼ10c .emmet-preview .cm-scroller {z-index: 1;}
.ͼ10c .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ10c .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ10c .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ10c .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ10c .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ10c .cm-tooltip.multiplayer-tooltip, .ͼ10c .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ10c .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ10c .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ10c .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ10c .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ10c .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ10c .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ10c .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ10c .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ104 {color: var(--foreground-default);}
.ͼ105 {color: var(--outline-stronger);}
.ͼ106 {color: var(--accent-red-default);}
.ͼ107 {color: var(--accent-orange-stronger);}
.ͼ108 {color: var(--accent-yellow-stronger);}
.ͼ109 {color: var(--accent-lime-stronger);}
.ͼ10a {color: var(--accent-green-stronger);}
.ͼ10b {color: var(--accent-teal-stronger);}
.ͼzw {color: var(--foreground-default);}
.ͼzx {color: var(--accent-green-default);}
.ͼzy {color: var(--accent-red-stronger);}
.ͼzz {color: var(--accent-orange-strongest);}
.ͼ100 {color: var(--accent-yellow-strongest);}
.ͼ101 {color: var(--accent-lime-strongest);}
.ͼ102 {color: var(--accent-green-strongest);}
.ͼ103 {color: var(--accent-teal-strongest);}
.ͼzj {text-decoration: underline;}
.ͼzk {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼzl {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼzm {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼzn {font-style: italic;}
.ͼzo {font-weight: var(--font-weight-bold);}
.ͼzp {text-decoration: line-through;}
.ͼzq {font-family: var(--font-family-code);}
.ͼzr {color: var(--foreground-dimmest);}
.ͼzs {color: var(--accent-blue-strongest);}
.ͼzt {color: var(--accent-blue-stronger);}
.ͼzu {color: var(--accent-purple-stronger);}
.ͼzv {color: var(--accent-pink-stronger);}
.ͼzi.cm-focused {outline: 0 none;}
.ͼzi {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼzi .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼzi .cm-line {line-height: var(--line-height-small);}
.ͼzi .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼzi .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼzi .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼzi .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼzi.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼzi .cm-cursor, .ͼzi .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼzi .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼzi .cm-activeLine {background-color: var(--background-higher);}
.ͼzi .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼzi .cm-specialChar {color: var(--accent-negative-default);}
.ͼzi .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼzi .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼzi .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼzi .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼzi .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼzi .cm-vim-panel input {color: var(--foreground-default);}
.ͼzi .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼzi .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼzi .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼzi .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼzi .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼzi .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼzi .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼzi .cm-matchingBracket, .ͼzi .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼzi .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼzi .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼzi .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼzi .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼzi .emmet-preview .cm-content {padding: 0 !important;}
.ͼzi .emmet-preview .cm-scroller {z-index: 1;}
.ͼzi .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼzi .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼzi .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼzi .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼzi .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼzi .cm-tooltip.multiplayer-tooltip, .ͼzi .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼzi .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼzi .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼzi .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼzi .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼzi .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼzi .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼzi .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼzi .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼza {color: var(--foreground-default);}
.ͼzb {color: var(--outline-stronger);}
.ͼzc {color: var(--accent-red-default);}
.ͼzd {color: var(--accent-orange-stronger);}
.ͼze {color: var(--accent-yellow-stronger);}
.ͼzf {color: var(--accent-lime-stronger);}
.ͼzg {color: var(--accent-green-stronger);}
.ͼzh {color: var(--accent-teal-stronger);}
.ͼz2 {color: var(--foreground-default);}
.ͼz3 {color: var(--accent-green-default);}
.ͼz4 {color: var(--accent-red-stronger);}
.ͼz5 {color: var(--accent-orange-strongest);}
.ͼz6 {color: var(--accent-yellow-strongest);}
.ͼz7 {color: var(--accent-lime-strongest);}
.ͼz8 {color: var(--accent-green-strongest);}
.ͼz9 {color: var(--accent-teal-strongest);}
.ͼyp {text-decoration: underline;}
.ͼyq {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼyr {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼys {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼyt {font-style: italic;}
.ͼyu {font-weight: var(--font-weight-bold);}
.ͼyv {text-decoration: line-through;}
.ͼyw {font-family: var(--font-family-code);}
.ͼyx {color: var(--foreground-dimmest);}
.ͼyy {color: var(--accent-blue-strongest);}
.ͼyz {color: var(--accent-blue-stronger);}
.ͼz0 {color: var(--accent-purple-stronger);}
.ͼz1 {color: var(--accent-pink-stronger);}
.ͼyo.cm-focused {outline: 0 none;}
.ͼyo {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼyo .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼyo .cm-line {line-height: var(--line-height-small);}
.ͼyo .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼyo .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼyo .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼyo .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼyo.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼyo .cm-cursor, .ͼyo .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼyo .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼyo .cm-activeLine {background-color: var(--background-higher);}
.ͼyo .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼyo .cm-specialChar {color: var(--accent-negative-default);}
.ͼyo .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼyo .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼyo .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼyo .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼyo .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼyo .cm-vim-panel input {color: var(--foreground-default);}
.ͼyo .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼyo .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼyo .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼyo .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼyo .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼyo .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼyo .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼyo .cm-matchingBracket, .ͼyo .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼyo .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼyo .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼyo .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼyo .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼyo .emmet-preview .cm-content {padding: 0 !important;}
.ͼyo .emmet-preview .cm-scroller {z-index: 1;}
.ͼyo .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼyo .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼyo .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼyo .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼyo .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼyo .cm-tooltip.multiplayer-tooltip, .ͼyo .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼyo .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼyo .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼyo .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼyo .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼyo .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼyo .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼyo .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼyo .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼyg {color: var(--foreground-default);}
.ͼyh {color: var(--outline-stronger);}
.ͼyi {color: var(--accent-red-default);}
.ͼyj {color: var(--accent-orange-stronger);}
.ͼyk {color: var(--accent-yellow-stronger);}
.ͼyl {color: var(--accent-lime-stronger);}
.ͼym {color: var(--accent-green-stronger);}
.ͼyn {color: var(--accent-teal-stronger);}
.ͼy8 {color: var(--foreground-default);}
.ͼy9 {color: var(--accent-green-default);}
.ͼya {color: var(--accent-red-stronger);}
.ͼyb {color: var(--accent-orange-strongest);}
.ͼyc {color: var(--accent-yellow-strongest);}
.ͼyd {color: var(--accent-lime-strongest);}
.ͼye {color: var(--accent-green-strongest);}
.ͼyf {color: var(--accent-teal-strongest);}
.ͼxv {text-decoration: underline;}
.ͼxw {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼxx {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼxy {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼxz {font-style: italic;}
.ͼy0 {font-weight: var(--font-weight-bold);}
.ͼy1 {text-decoration: line-through;}
.ͼy2 {font-family: var(--font-family-code);}
.ͼy3 {color: var(--foreground-dimmest);}
.ͼy4 {color: var(--accent-blue-strongest);}
.ͼy5 {color: var(--accent-blue-stronger);}
.ͼy6 {color: var(--accent-purple-stronger);}
.ͼy7 {color: var(--accent-pink-stronger);}
.ͼxu.cm-focused {outline: 0 none;}
.ͼxu {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼxu .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼxu .cm-line {line-height: var(--line-height-small);}
.ͼxu .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼxu .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼxu .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼxu .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼxu.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼxu .cm-cursor, .ͼxu .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼxu .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼxu .cm-activeLine {background-color: var(--background-higher);}
.ͼxu .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼxu .cm-specialChar {color: var(--accent-negative-default);}
.ͼxu .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼxu .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼxu .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼxu .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼxu .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼxu .cm-vim-panel input {color: var(--foreground-default);}
.ͼxu .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼxu .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼxu .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼxu .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼxu .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼxu .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼxu .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼxu .cm-matchingBracket, .ͼxu .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼxu .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼxu .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼxu .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼxu .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼxu .emmet-preview .cm-content {padding: 0 !important;}
.ͼxu .emmet-preview .cm-scroller {z-index: 1;}
.ͼxu .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼxu .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼxu .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼxu .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼxu .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼxu .cm-tooltip.multiplayer-tooltip, .ͼxu .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼxu .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼxu .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼxu .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼxu .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼxu .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼxu .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼxu .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼxu .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼxm {color: var(--foreground-default);}
.ͼxn {color: var(--outline-stronger);}
.ͼxo {color: var(--accent-red-default);}
.ͼxp {color: var(--accent-orange-stronger);}
.ͼxq {color: var(--accent-yellow-stronger);}
.ͼxr {color: var(--accent-lime-stronger);}
.ͼxs {color: var(--accent-green-stronger);}
.ͼxt {color: var(--accent-teal-stronger);}
.ͼxe {color: var(--foreground-default);}
.ͼxf {color: var(--accent-green-default);}
.ͼxg {color: var(--accent-red-stronger);}
.ͼxh {color: var(--accent-orange-strongest);}
.ͼxi {color: var(--accent-yellow-strongest);}
.ͼxj {color: var(--accent-lime-strongest);}
.ͼxk {color: var(--accent-green-strongest);}
.ͼxl {color: var(--accent-teal-strongest);}
.ͼx1 {text-decoration: underline;}
.ͼx2 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼx3 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼx4 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼx5 {font-style: italic;}
.ͼx6 {font-weight: var(--font-weight-bold);}
.ͼx7 {text-decoration: line-through;}
.ͼx8 {font-family: var(--font-family-code);}
.ͼx9 {color: var(--foreground-dimmest);}
.ͼxa {color: var(--accent-blue-strongest);}
.ͼxb {color: var(--accent-blue-stronger);}
.ͼxc {color: var(--accent-purple-stronger);}
.ͼxd {color: var(--accent-pink-stronger);}
.ͼx0.cm-focused {outline: 0 none;}
.ͼx0 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼx0 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼx0 .cm-line {line-height: var(--line-height-small);}
.ͼx0 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼx0 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼx0 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼx0 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼx0.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼx0 .cm-cursor, .ͼx0 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼx0 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼx0 .cm-activeLine {background-color: var(--background-higher);}
.ͼx0 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼx0 .cm-specialChar {color: var(--accent-negative-default);}
.ͼx0 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼx0 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼx0 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼx0 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼx0 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼx0 .cm-vim-panel input {color: var(--foreground-default);}
.ͼx0 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼx0 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼx0 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼx0 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼx0 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼx0 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼx0 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼx0 .cm-matchingBracket, .ͼx0 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼx0 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼx0 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼx0 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼx0 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼx0 .emmet-preview .cm-content {padding: 0 !important;}
.ͼx0 .emmet-preview .cm-scroller {z-index: 1;}
.ͼx0 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼx0 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼx0 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼx0 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼx0 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼx0 .cm-tooltip.multiplayer-tooltip, .ͼx0 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼx0 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼx0 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼx0 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼx0 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼx0 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼx0 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼx0 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼx0 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼws {color: var(--foreground-default);}
.ͼwt {color: var(--outline-stronger);}
.ͼwu {color: var(--accent-red-default);}
.ͼwv {color: var(--accent-orange-stronger);}
.ͼww {color: var(--accent-yellow-stronger);}
.ͼwx {color: var(--accent-lime-stronger);}
.ͼwy {color: var(--accent-green-stronger);}
.ͼwz {color: var(--accent-teal-stronger);}
.ͼwk {color: var(--foreground-default);}
.ͼwl {color: var(--accent-green-default);}
.ͼwm {color: var(--accent-red-stronger);}
.ͼwn {color: var(--accent-orange-strongest);}
.ͼwo {color: var(--accent-yellow-strongest);}
.ͼwp {color: var(--accent-lime-strongest);}
.ͼwq {color: var(--accent-green-strongest);}
.ͼwr {color: var(--accent-teal-strongest);}
.ͼw7 {text-decoration: underline;}
.ͼw8 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼw9 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼwa {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼwb {font-style: italic;}
.ͼwc {font-weight: var(--font-weight-bold);}
.ͼwd {text-decoration: line-through;}
.ͼwe {font-family: var(--font-family-code);}
.ͼwf {color: var(--foreground-dimmest);}
.ͼwg {color: var(--accent-blue-strongest);}
.ͼwh {color: var(--accent-blue-stronger);}
.ͼwi {color: var(--accent-purple-stronger);}
.ͼwj {color: var(--accent-pink-stronger);}
.ͼw6.cm-focused {outline: 0 none;}
.ͼw6 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼw6 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼw6 .cm-line {line-height: var(--line-height-small);}
.ͼw6 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼw6 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼw6 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼw6 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼw6.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼw6 .cm-cursor, .ͼw6 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼw6 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼw6 .cm-activeLine {background-color: var(--background-higher);}
.ͼw6 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼw6 .cm-specialChar {color: var(--accent-negative-default);}
.ͼw6 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼw6 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼw6 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼw6 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼw6 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼw6 .cm-vim-panel input {color: var(--foreground-default);}
.ͼw6 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼw6 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼw6 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼw6 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼw6 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼw6 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼw6 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼw6 .cm-matchingBracket, .ͼw6 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼw6 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼw6 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼw6 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼw6 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼw6 .emmet-preview .cm-content {padding: 0 !important;}
.ͼw6 .emmet-preview .cm-scroller {z-index: 1;}
.ͼw6 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼw6 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼw6 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼw6 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼw6 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼw6 .cm-tooltip.multiplayer-tooltip, .ͼw6 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼw6 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼw6 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼw6 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼw6 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼw6 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼw6 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼw6 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼw6 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼvy {color: var(--foreground-default);}
.ͼvz {color: var(--outline-stronger);}
.ͼw0 {color: var(--accent-red-default);}
.ͼw1 {color: var(--accent-orange-stronger);}
.ͼw2 {color: var(--accent-yellow-stronger);}
.ͼw3 {color: var(--accent-lime-stronger);}
.ͼw4 {color: var(--accent-green-stronger);}
.ͼw5 {color: var(--accent-teal-stronger);}
.ͼvq {color: var(--foreground-default);}
.ͼvr {color: var(--accent-green-default);}
.ͼvs {color: var(--accent-red-stronger);}
.ͼvt {color: var(--accent-orange-strongest);}
.ͼvu {color: var(--accent-yellow-strongest);}
.ͼvv {color: var(--accent-lime-strongest);}
.ͼvw {color: var(--accent-green-strongest);}
.ͼvx {color: var(--accent-teal-strongest);}
.ͼvd {text-decoration: underline;}
.ͼve {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼvf {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼvg {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼvh {font-style: italic;}
.ͼvi {font-weight: var(--font-weight-bold);}
.ͼvj {text-decoration: line-through;}
.ͼvk {font-family: var(--font-family-code);}
.ͼvl {color: var(--foreground-dimmest);}
.ͼvm {color: var(--accent-blue-strongest);}
.ͼvn {color: var(--accent-blue-stronger);}
.ͼvo {color: var(--accent-purple-stronger);}
.ͼvp {color: var(--accent-pink-stronger);}
.ͼvc.cm-focused {outline: 0 none;}
.ͼvc {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼvc .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼvc .cm-line {line-height: var(--line-height-small);}
.ͼvc .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼvc .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼvc .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼvc .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼvc.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼvc .cm-cursor, .ͼvc .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼvc .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼvc .cm-activeLine {background-color: var(--background-higher);}
.ͼvc .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼvc .cm-specialChar {color: var(--accent-negative-default);}
.ͼvc .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼvc .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼvc .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼvc .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼvc .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼvc .cm-vim-panel input {color: var(--foreground-default);}
.ͼvc .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼvc .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼvc .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼvc .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼvc .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼvc .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼvc .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼvc .cm-matchingBracket, .ͼvc .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼvc .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼvc .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼvc .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼvc .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼvc .emmet-preview .cm-content {padding: 0 !important;}
.ͼvc .emmet-preview .cm-scroller {z-index: 1;}
.ͼvc .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼvc .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼvc .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼvc .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼvc .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼvc .cm-tooltip.multiplayer-tooltip, .ͼvc .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼvc .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼvc .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼvc .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼvc .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼvc .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼvc .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼvc .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼvc .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼv4 {color: var(--foreground-default);}
.ͼv5 {color: var(--outline-stronger);}
.ͼv6 {color: var(--accent-red-default);}
.ͼv7 {color: var(--accent-orange-stronger);}
.ͼv8 {color: var(--accent-yellow-stronger);}
.ͼv9 {color: var(--accent-lime-stronger);}
.ͼva {color: var(--accent-green-stronger);}
.ͼvb {color: var(--accent-teal-stronger);}
.ͼuw {color: var(--foreground-default);}
.ͼux {color: var(--accent-green-default);}
.ͼuy {color: var(--accent-red-stronger);}
.ͼuz {color: var(--accent-orange-strongest);}
.ͼv0 {color: var(--accent-yellow-strongest);}
.ͼv1 {color: var(--accent-lime-strongest);}
.ͼv2 {color: var(--accent-green-strongest);}
.ͼv3 {color: var(--accent-teal-strongest);}
.ͼuj {text-decoration: underline;}
.ͼuk {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼul {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼum {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼun {font-style: italic;}
.ͼuo {font-weight: var(--font-weight-bold);}
.ͼup {text-decoration: line-through;}
.ͼuq {font-family: var(--font-family-code);}
.ͼur {color: var(--foreground-dimmest);}
.ͼus {color: var(--accent-blue-strongest);}
.ͼut {color: var(--accent-blue-stronger);}
.ͼuu {color: var(--accent-purple-stronger);}
.ͼuv {color: var(--accent-pink-stronger);}
.ͼui.cm-focused {outline: 0 none;}
.ͼui {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼui .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼui .cm-line {line-height: var(--line-height-small);}
.ͼui .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼui .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼui .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼui .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼui.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼui .cm-cursor, .ͼui .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼui .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼui .cm-activeLine {background-color: var(--background-higher);}
.ͼui .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼui .cm-specialChar {color: var(--accent-negative-default);}
.ͼui .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼui .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼui .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼui .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼui .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼui .cm-vim-panel input {color: var(--foreground-default);}
.ͼui .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼui .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼui .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼui .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼui .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼui .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼui .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼui .cm-matchingBracket, .ͼui .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼui .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼui .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼui .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼui .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼui .emmet-preview .cm-content {padding: 0 !important;}
.ͼui .emmet-preview .cm-scroller {z-index: 1;}
.ͼui .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼui .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼui .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼui .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼui .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼui .cm-tooltip.multiplayer-tooltip, .ͼui .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼui .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼui .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼui .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼui .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼui .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼui .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼui .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼui .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼua {color: var(--foreground-default);}
.ͼub {color: var(--outline-stronger);}
.ͼuc {color: var(--accent-red-default);}
.ͼud {color: var(--accent-orange-stronger);}
.ͼue {color: var(--accent-yellow-stronger);}
.ͼuf {color: var(--accent-lime-stronger);}
.ͼug {color: var(--accent-green-stronger);}
.ͼuh {color: var(--accent-teal-stronger);}
.ͼu2 {color: var(--foreground-default);}
.ͼu3 {color: var(--accent-green-default);}
.ͼu4 {color: var(--accent-red-stronger);}
.ͼu5 {color: var(--accent-orange-strongest);}
.ͼu6 {color: var(--accent-yellow-strongest);}
.ͼu7 {color: var(--accent-lime-strongest);}
.ͼu8 {color: var(--accent-green-strongest);}
.ͼu9 {color: var(--accent-teal-strongest);}
.ͼtp {text-decoration: underline;}
.ͼtq {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼtr {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼts {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼtt {font-style: italic;}
.ͼtu {font-weight: var(--font-weight-bold);}
.ͼtv {text-decoration: line-through;}
.ͼtw {font-family: var(--font-family-code);}
.ͼtx {color: var(--foreground-dimmest);}
.ͼty {color: var(--accent-blue-strongest);}
.ͼtz {color: var(--accent-blue-stronger);}
.ͼu0 {color: var(--accent-purple-stronger);}
.ͼu1 {color: var(--accent-pink-stronger);}
.ͼto.cm-focused {outline: 0 none;}
.ͼto {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼto .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼto .cm-line {line-height: var(--line-height-small);}
.ͼto .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼto .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼto .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼto .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼto.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼto .cm-cursor, .ͼto .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼto .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼto .cm-activeLine {background-color: var(--background-higher);}
.ͼto .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼto .cm-specialChar {color: var(--accent-negative-default);}
.ͼto .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼto .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼto .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼto .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼto .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼto .cm-vim-panel input {color: var(--foreground-default);}
.ͼto .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼto .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼto .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼto .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼto .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼto .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼto .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼto .cm-matchingBracket, .ͼto .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼto .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼto .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼto .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼto .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼto .emmet-preview .cm-content {padding: 0 !important;}
.ͼto .emmet-preview .cm-scroller {z-index: 1;}
.ͼto .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼto .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼto .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼto .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼto .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼto .cm-tooltip.multiplayer-tooltip, .ͼto .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼto .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼto .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼto .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼto .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼto .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼto .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼto .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼto .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼtg {color: var(--foreground-default);}
.ͼth {color: var(--outline-stronger);}
.ͼti {color: var(--accent-red-default);}
.ͼtj {color: var(--accent-orange-stronger);}
.ͼtk {color: var(--accent-yellow-stronger);}
.ͼtl {color: var(--accent-lime-stronger);}
.ͼtm {color: var(--accent-green-stronger);}
.ͼtn {color: var(--accent-teal-stronger);}
.ͼt8 {color: var(--foreground-default);}
.ͼt9 {color: var(--accent-green-default);}
.ͼta {color: var(--accent-red-stronger);}
.ͼtb {color: var(--accent-orange-strongest);}
.ͼtc {color: var(--accent-yellow-strongest);}
.ͼtd {color: var(--accent-lime-strongest);}
.ͼte {color: var(--accent-green-strongest);}
.ͼtf {color: var(--accent-teal-strongest);}
.ͼsv {text-decoration: underline;}
.ͼsw {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼsx {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼsy {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼsz {font-style: italic;}
.ͼt0 {font-weight: var(--font-weight-bold);}
.ͼt1 {text-decoration: line-through;}
.ͼt2 {font-family: var(--font-family-code);}
.ͼt3 {color: var(--foreground-dimmest);}
.ͼt4 {color: var(--accent-blue-strongest);}
.ͼt5 {color: var(--accent-blue-stronger);}
.ͼt6 {color: var(--accent-purple-stronger);}
.ͼt7 {color: var(--accent-pink-stronger);}
.ͼsu.cm-focused {outline: 0 none;}
.ͼsu {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼsu .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼsu .cm-line {line-height: var(--line-height-small);}
.ͼsu .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼsu .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼsu .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼsu .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼsu.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼsu .cm-cursor, .ͼsu .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼsu .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼsu .cm-activeLine {background-color: var(--background-higher);}
.ͼsu .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼsu .cm-specialChar {color: var(--accent-negative-default);}
.ͼsu .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼsu .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼsu .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼsu .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼsu .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼsu .cm-vim-panel input {color: var(--foreground-default);}
.ͼsu .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼsu .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼsu .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼsu .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼsu .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼsu .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼsu .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼsu .cm-matchingBracket, .ͼsu .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼsu .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼsu .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼsu .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼsu .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼsu .emmet-preview .cm-content {padding: 0 !important;}
.ͼsu .emmet-preview .cm-scroller {z-index: 1;}
.ͼsu .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼsu .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼsu .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼsu .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼsu .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼsu .cm-tooltip.multiplayer-tooltip, .ͼsu .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼsu .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼsu .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼsu .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼsu .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼsu .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼsu .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼsu .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼsu .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼsm {color: var(--foreground-default);}
.ͼsn {color: var(--outline-stronger);}
.ͼso {color: var(--accent-red-default);}
.ͼsp {color: var(--accent-orange-stronger);}
.ͼsq {color: var(--accent-yellow-stronger);}
.ͼsr {color: var(--accent-lime-stronger);}
.ͼss {color: var(--accent-green-stronger);}
.ͼst {color: var(--accent-teal-stronger);}
.ͼse {color: var(--foreground-default);}
.ͼsf {color: var(--accent-green-default);}
.ͼsg {color: var(--accent-red-stronger);}
.ͼsh {color: var(--accent-orange-strongest);}
.ͼsi {color: var(--accent-yellow-strongest);}
.ͼsj {color: var(--accent-lime-strongest);}
.ͼsk {color: var(--accent-green-strongest);}
.ͼsl {color: var(--accent-teal-strongest);}
.ͼs1 {text-decoration: underline;}
.ͼs2 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼs3 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼs4 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼs5 {font-style: italic;}
.ͼs6 {font-weight: var(--font-weight-bold);}
.ͼs7 {text-decoration: line-through;}
.ͼs8 {font-family: var(--font-family-code);}
.ͼs9 {color: var(--foreground-dimmest);}
.ͼsa {color: var(--accent-blue-strongest);}
.ͼsb {color: var(--accent-blue-stronger);}
.ͼsc {color: var(--accent-purple-stronger);}
.ͼsd {color: var(--accent-pink-stronger);}
.ͼs0.cm-focused {outline: 0 none;}
.ͼs0 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼs0 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼs0 .cm-line {line-height: var(--line-height-small);}
.ͼs0 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼs0 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼs0 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼs0 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼs0.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼs0 .cm-cursor, .ͼs0 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼs0 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼs0 .cm-activeLine {background-color: var(--background-higher);}
.ͼs0 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼs0 .cm-specialChar {color: var(--accent-negative-default);}
.ͼs0 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼs0 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼs0 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼs0 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼs0 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼs0 .cm-vim-panel input {color: var(--foreground-default);}
.ͼs0 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼs0 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼs0 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼs0 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼs0 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼs0 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼs0 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼs0 .cm-matchingBracket, .ͼs0 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼs0 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼs0 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼs0 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼs0 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼs0 .emmet-preview .cm-content {padding: 0 !important;}
.ͼs0 .emmet-preview .cm-scroller {z-index: 1;}
.ͼs0 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼs0 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼs0 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼs0 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼs0 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼs0 .cm-tooltip.multiplayer-tooltip, .ͼs0 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼs0 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼs0 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼs0 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼs0 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼs0 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼs0 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼs0 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼs0 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼrs {color: var(--foreground-default);}
.ͼrt {color: var(--outline-stronger);}
.ͼru {color: var(--accent-red-default);}
.ͼrv {color: var(--accent-orange-stronger);}
.ͼrw {color: var(--accent-yellow-stronger);}
.ͼrx {color: var(--accent-lime-stronger);}
.ͼry {color: var(--accent-green-stronger);}
.ͼrz {color: var(--accent-teal-stronger);}
.ͼrk {color: var(--foreground-default);}
.ͼrl {color: var(--accent-green-default);}
.ͼrm {color: var(--accent-red-stronger);}
.ͼrn {color: var(--accent-orange-strongest);}
.ͼro {color: var(--accent-yellow-strongest);}
.ͼrp {color: var(--accent-lime-strongest);}
.ͼrq {color: var(--accent-green-strongest);}
.ͼrr {color: var(--accent-teal-strongest);}
.ͼr7 {text-decoration: underline;}
.ͼr8 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼr9 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼra {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼrb {font-style: italic;}
.ͼrc {font-weight: var(--font-weight-bold);}
.ͼrd {text-decoration: line-through;}
.ͼre {font-family: var(--font-family-code);}
.ͼrf {color: var(--foreground-dimmest);}
.ͼrg {color: var(--accent-blue-strongest);}
.ͼrh {color: var(--accent-blue-stronger);}
.ͼri {color: var(--accent-purple-stronger);}
.ͼrj {color: var(--accent-pink-stronger);}
.ͼr2.cm-focused {outline: 0 none;}
.ͼr2 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼr2 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼr2 .cm-line {line-height: var(--line-height-small);}
.ͼr2 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼr2 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼr2 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼr2 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼr2.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼr2 .cm-cursor, .ͼr2 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼr2 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼr2 .cm-activeLine {background-color: var(--background-higher);}
.ͼr2 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼr2 .cm-specialChar {color: var(--accent-negative-default);}
.ͼr2 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼr2 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼr2 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼr2 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼr2 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼr2 .cm-vim-panel input {color: var(--foreground-default);}
.ͼr2 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼr2 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼr2 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼr2 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼr2 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼr2 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼr2 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼr2 .cm-matchingBracket, .ͼr2 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼr2 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼr2 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼr2 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼr2 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼr2 .emmet-preview .cm-content {padding: 0 !important;}
.ͼr2 .emmet-preview .cm-scroller {z-index: 1;}
.ͼr2 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼr2 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼr2 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼr2 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼr2 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼr2 .cm-tooltip.multiplayer-tooltip, .ͼr2 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼr2 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼr2 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼr2 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼr2 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼr2 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼr2 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼr2 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼr2 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼqu {color: var(--foreground-default);}
.ͼqv {color: var(--outline-stronger);}
.ͼqw {color: var(--accent-red-default);}
.ͼqx {color: var(--accent-orange-stronger);}
.ͼqy {color: var(--accent-yellow-stronger);}
.ͼqz {color: var(--accent-lime-stronger);}
.ͼr0 {color: var(--accent-green-stronger);}
.ͼr1 {color: var(--accent-teal-stronger);}
.ͼqm {color: var(--foreground-default);}
.ͼqn {color: var(--accent-green-default);}
.ͼqo {color: var(--accent-red-stronger);}
.ͼqp {color: var(--accent-orange-strongest);}
.ͼqq {color: var(--accent-yellow-strongest);}
.ͼqr {color: var(--accent-lime-strongest);}
.ͼqs {color: var(--accent-green-strongest);}
.ͼqt {color: var(--accent-teal-strongest);}
.ͼq9 {text-decoration: underline;}
.ͼqa {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼqb {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼqc {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼqd {font-style: italic;}
.ͼqe {font-weight: var(--font-weight-bold);}
.ͼqf {text-decoration: line-through;}
.ͼqg {font-family: var(--font-family-code);}
.ͼqh {color: var(--foreground-dimmest);}
.ͼqi {color: var(--accent-blue-strongest);}
.ͼqj {color: var(--accent-blue-stronger);}
.ͼqk {color: var(--accent-purple-stronger);}
.ͼql {color: var(--accent-pink-stronger);}
.ͼq8.cm-focused {outline: 0 none;}
.ͼq8 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼq8 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼq8 .cm-line {line-height: var(--line-height-small);}
.ͼq8 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼq8 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼq8 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼq8 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼq8.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼq8 .cm-cursor, .ͼq8 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼq8 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼq8 .cm-activeLine {background-color: var(--background-higher);}
.ͼq8 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼq8 .cm-specialChar {color: var(--accent-negative-default);}
.ͼq8 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼq8 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼq8 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼq8 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼq8 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼq8 .cm-vim-panel input {color: var(--foreground-default);}
.ͼq8 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼq8 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼq8 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼq8 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼq8 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼq8 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼq8 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼq8 .cm-matchingBracket, .ͼq8 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼq8 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼq8 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼq8 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼq8 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼq8 .emmet-preview .cm-content {padding: 0 !important;}
.ͼq8 .emmet-preview .cm-scroller {z-index: 1;}
.ͼq8 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼq8 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼq8 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼq8 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼq8 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼq8 .cm-tooltip.multiplayer-tooltip, .ͼq8 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼq8 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼq8 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼq8 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼq8 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼq8 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼq8 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼq8 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼq8 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼq0 {color: var(--foreground-default);}
.ͼq1 {color: var(--outline-stronger);}
.ͼq2 {color: var(--accent-red-default);}
.ͼq3 {color: var(--accent-orange-stronger);}
.ͼq4 {color: var(--accent-yellow-stronger);}
.ͼq5 {color: var(--accent-lime-stronger);}
.ͼq6 {color: var(--accent-green-stronger);}
.ͼq7 {color: var(--accent-teal-stronger);}
.ͼps {color: var(--foreground-default);}
.ͼpt {color: var(--accent-green-default);}
.ͼpu {color: var(--accent-red-stronger);}
.ͼpv {color: var(--accent-orange-strongest);}
.ͼpw {color: var(--accent-yellow-strongest);}
.ͼpx {color: var(--accent-lime-strongest);}
.ͼpy {color: var(--accent-green-strongest);}
.ͼpz {color: var(--accent-teal-strongest);}
.ͼpf {text-decoration: underline;}
.ͼpg {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼph {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼpi {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼpj {font-style: italic;}
.ͼpk {font-weight: var(--font-weight-bold);}
.ͼpl {text-decoration: line-through;}
.ͼpm {font-family: var(--font-family-code);}
.ͼpn {color: var(--foreground-dimmest);}
.ͼpo {color: var(--accent-blue-strongest);}
.ͼpp {color: var(--accent-blue-stronger);}
.ͼpq {color: var(--accent-purple-stronger);}
.ͼpr {color: var(--accent-pink-stronger);}
.ͼpa.cm-focused {outline: 0 none;}
.ͼpa {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼpa .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼpa .cm-line {line-height: var(--line-height-small);}
.ͼpa .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼpa .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼpa .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼpa .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼpa.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼpa .cm-cursor, .ͼpa .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼpa .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼpa .cm-activeLine {background-color: var(--background-higher);}
.ͼpa .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼpa .cm-specialChar {color: var(--accent-negative-default);}
.ͼpa .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼpa .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼpa .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼpa .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼpa .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼpa .cm-vim-panel input {color: var(--foreground-default);}
.ͼpa .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼpa .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼpa .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼpa .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼpa .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼpa .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼpa .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼpa .cm-matchingBracket, .ͼpa .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼpa .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼpa .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼpa .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼpa .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼpa .emmet-preview .cm-content {padding: 0 !important;}
.ͼpa .emmet-preview .cm-scroller {z-index: 1;}
.ͼpa .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼpa .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼpa .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼpa .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼpa .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼpa .cm-tooltip.multiplayer-tooltip, .ͼpa .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼpa .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼpa .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼpa .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼpa .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼpa .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼpa .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼpa .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼpa .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼp2 {color: var(--foreground-default);}
.ͼp3 {color: var(--outline-stronger);}
.ͼp4 {color: var(--accent-red-default);}
.ͼp5 {color: var(--accent-orange-stronger);}
.ͼp6 {color: var(--accent-yellow-stronger);}
.ͼp7 {color: var(--accent-lime-stronger);}
.ͼp8 {color: var(--accent-green-stronger);}
.ͼp9 {color: var(--accent-teal-stronger);}
.ͼou {color: var(--foreground-default);}
.ͼov {color: var(--accent-green-default);}
.ͼow {color: var(--accent-red-stronger);}
.ͼox {color: var(--accent-orange-strongest);}
.ͼoy {color: var(--accent-yellow-strongest);}
.ͼoz {color: var(--accent-lime-strongest);}
.ͼp0 {color: var(--accent-green-strongest);}
.ͼp1 {color: var(--accent-teal-strongest);}
.ͼoh {text-decoration: underline;}
.ͼoi {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼoj {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼok {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼol {font-style: italic;}
.ͼom {font-weight: var(--font-weight-bold);}
.ͼon {text-decoration: line-through;}
.ͼoo {font-family: var(--font-family-code);}
.ͼop {color: var(--foreground-dimmest);}
.ͼoq {color: var(--accent-blue-strongest);}
.ͼor {color: var(--accent-blue-stronger);}
.ͼos {color: var(--accent-purple-stronger);}
.ͼot {color: var(--accent-pink-stronger);}
.ͼog.cm-focused {outline: 0 none;}
.ͼog {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼog .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼog .cm-line {line-height: var(--line-height-small);}
.ͼog .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼog .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼog .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼog .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼog.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼog .cm-cursor, .ͼog .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼog .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼog .cm-activeLine {background-color: var(--background-higher);}
.ͼog .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼog .cm-specialChar {color: var(--accent-negative-default);}
.ͼog .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼog .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼog .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼog .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼog .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼog .cm-vim-panel input {color: var(--foreground-default);}
.ͼog .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼog .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼog .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼog .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼog .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼog .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼog .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼog .cm-matchingBracket, .ͼog .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼog .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼog .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼog .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼog .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼog .emmet-preview .cm-content {padding: 0 !important;}
.ͼog .emmet-preview .cm-scroller {z-index: 1;}
.ͼog .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼog .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼog .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼog .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼog .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼog .cm-tooltip.multiplayer-tooltip, .ͼog .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼog .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼog .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼog .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼog .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼog .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼog .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼog .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼog .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼo8 {color: var(--foreground-default);}
.ͼo9 {color: var(--outline-stronger);}
.ͼoa {color: var(--accent-red-default);}
.ͼob {color: var(--accent-orange-stronger);}
.ͼoc {color: var(--accent-yellow-stronger);}
.ͼod {color: var(--accent-lime-stronger);}
.ͼoe {color: var(--accent-green-stronger);}
.ͼof {color: var(--accent-teal-stronger);}
.ͼo0 {color: var(--foreground-default);}
.ͼo1 {color: var(--accent-green-default);}
.ͼo2 {color: var(--accent-red-stronger);}
.ͼo3 {color: var(--accent-orange-strongest);}
.ͼo4 {color: var(--accent-yellow-strongest);}
.ͼo5 {color: var(--accent-lime-strongest);}
.ͼo6 {color: var(--accent-green-strongest);}
.ͼo7 {color: var(--accent-teal-strongest);}
.ͼnn {text-decoration: underline;}
.ͼno {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼnp {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼnq {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼnr {font-style: italic;}
.ͼns {font-weight: var(--font-weight-bold);}
.ͼnt {text-decoration: line-through;}
.ͼnu {font-family: var(--font-family-code);}
.ͼnv {color: var(--foreground-dimmest);}
.ͼnw {color: var(--accent-blue-strongest);}
.ͼnx {color: var(--accent-blue-stronger);}
.ͼny {color: var(--accent-purple-stronger);}
.ͼnz {color: var(--accent-pink-stronger);}
.ͼnl.cm-focused {outline: 0 none;}
.ͼnl {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼnl .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼnl .cm-line {line-height: var(--line-height-small);}
.ͼnl .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼnl .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼnl .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼnl .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼnl.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼnl .cm-cursor, .ͼnl .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼnl .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼnl .cm-activeLine {background-color: var(--background-higher);}
.ͼnl .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼnl .cm-specialChar {color: var(--accent-negative-default);}
.ͼnl .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼnl .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼnl .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼnl .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼnl .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼnl .cm-vim-panel input {color: var(--foreground-default);}
.ͼnl .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼnl .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼnl .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼnl .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼnl .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼnl .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼnl .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼnl .cm-matchingBracket, .ͼnl .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼnl .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼnl .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼnl .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼnl .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼnl .emmet-preview .cm-content {padding: 0 !important;}
.ͼnl .emmet-preview .cm-scroller {z-index: 1;}
.ͼnl .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼnl .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼnl .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼnl .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼnl .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼnl .cm-tooltip.multiplayer-tooltip, .ͼnl .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼnl .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼnl .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼnl .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼnl .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼnl .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼnl .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼnl .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼnl .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼnd {color: var(--foreground-default);}
.ͼne {color: var(--outline-stronger);}
.ͼnf {color: var(--accent-red-default);}
.ͼng {color: var(--accent-orange-stronger);}
.ͼnh {color: var(--accent-yellow-stronger);}
.ͼni {color: var(--accent-lime-stronger);}
.ͼnj {color: var(--accent-green-stronger);}
.ͼnk {color: var(--accent-teal-stronger);}
.ͼn5 {color: var(--foreground-default);}
.ͼn6 {color: var(--accent-green-default);}
.ͼn7 {color: var(--accent-red-stronger);}
.ͼn8 {color: var(--accent-orange-strongest);}
.ͼn9 {color: var(--accent-yellow-strongest);}
.ͼna {color: var(--accent-lime-strongest);}
.ͼnb {color: var(--accent-green-strongest);}
.ͼnc {color: var(--accent-teal-strongest);}
.ͼms {text-decoration: underline;}
.ͼmt {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼmu {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼmv {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼmw {font-style: italic;}
.ͼmx {font-weight: var(--font-weight-bold);}
.ͼmy {text-decoration: line-through;}
.ͼmz {font-family: var(--font-family-code);}
.ͼn0 {color: var(--foreground-dimmest);}
.ͼn1 {color: var(--accent-blue-strongest);}
.ͼn2 {color: var(--accent-blue-stronger);}
.ͼn3 {color: var(--accent-purple-stronger);}
.ͼn4 {color: var(--accent-pink-stronger);}
.ͼmr.cm-focused {outline: 0 none;}
.ͼmr {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼmr .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼmr .cm-line {line-height: var(--line-height-small);}
.ͼmr .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼmr .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼmr .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼmr .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼmr.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼmr .cm-cursor, .ͼmr .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼmr .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼmr .cm-activeLine {background-color: var(--background-higher);}
.ͼmr .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼmr .cm-specialChar {color: var(--accent-negative-default);}
.ͼmr .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼmr .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼmr .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼmr .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼmr .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼmr .cm-vim-panel input {color: var(--foreground-default);}
.ͼmr .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼmr .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼmr .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼmr .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼmr .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼmr .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼmr .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼmr .cm-matchingBracket, .ͼmr .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼmr .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼmr .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼmr .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼmr .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼmr .emmet-preview .cm-content {padding: 0 !important;}
.ͼmr .emmet-preview .cm-scroller {z-index: 1;}
.ͼmr .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼmr .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼmr .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼmr .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼmr .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼmr .cm-tooltip.multiplayer-tooltip, .ͼmr .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼmr .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼmr .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼmr .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼmr .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼmr .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼmr .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼmr .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼmr .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼmj {color: var(--foreground-default);}
.ͼmk {color: var(--outline-stronger);}
.ͼml {color: var(--accent-red-default);}
.ͼmm {color: var(--accent-orange-stronger);}
.ͼmn {color: var(--accent-yellow-stronger);}
.ͼmo {color: var(--accent-lime-stronger);}
.ͼmp {color: var(--accent-green-stronger);}
.ͼmq {color: var(--accent-teal-stronger);}
.ͼmb {color: var(--foreground-default);}
.ͼmc {color: var(--accent-green-default);}
.ͼmd {color: var(--accent-red-stronger);}
.ͼme {color: var(--accent-orange-strongest);}
.ͼmf {color: var(--accent-yellow-strongest);}
.ͼmg {color: var(--accent-lime-strongest);}
.ͼmh {color: var(--accent-green-strongest);}
.ͼmi {color: var(--accent-teal-strongest);}
.ͼly {text-decoration: underline;}
.ͼlz {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼm0 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼm1 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼm2 {font-style: italic;}
.ͼm3 {font-weight: var(--font-weight-bold);}
.ͼm4 {text-decoration: line-through;}
.ͼm5 {font-family: var(--font-family-code);}
.ͼm6 {color: var(--foreground-dimmest);}
.ͼm7 {color: var(--accent-blue-strongest);}
.ͼm8 {color: var(--accent-blue-stronger);}
.ͼm9 {color: var(--accent-purple-stronger);}
.ͼma {color: var(--accent-pink-stronger);}
.ͼlx.cm-focused {outline: 0 none;}
.ͼlx {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼlx .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼlx .cm-line {line-height: var(--line-height-small);}
.ͼlx .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼlx .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼlx .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼlx .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼlx.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼlx .cm-cursor, .ͼlx .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼlx .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼlx .cm-activeLine {background-color: var(--background-higher);}
.ͼlx .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼlx .cm-specialChar {color: var(--accent-negative-default);}
.ͼlx .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼlx .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼlx .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼlx .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼlx .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼlx .cm-vim-panel input {color: var(--foreground-default);}
.ͼlx .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼlx .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼlx .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼlx .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼlx .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼlx .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼlx .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼlx .cm-matchingBracket, .ͼlx .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼlx .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼlx .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼlx .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼlx .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼlx .emmet-preview .cm-content {padding: 0 !important;}
.ͼlx .emmet-preview .cm-scroller {z-index: 1;}
.ͼlx .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼlx .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼlx .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼlx .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼlx .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼlx .cm-tooltip.multiplayer-tooltip, .ͼlx .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼlx .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼlx .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼlx .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼlx .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼlx .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼlx .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼlx .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼlx .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼlp {color: var(--foreground-default);}
.ͼlq {color: var(--outline-stronger);}
.ͼlr {color: var(--accent-red-default);}
.ͼls {color: var(--accent-orange-stronger);}
.ͼlt {color: var(--accent-yellow-stronger);}
.ͼlu {color: var(--accent-lime-stronger);}
.ͼlv {color: var(--accent-green-stronger);}
.ͼlw {color: var(--accent-teal-stronger);}
.ͼlh {color: var(--foreground-default);}
.ͼli {color: var(--accent-green-default);}
.ͼlj {color: var(--accent-red-stronger);}
.ͼlk {color: var(--accent-orange-strongest);}
.ͼll {color: var(--accent-yellow-strongest);}
.ͼlm {color: var(--accent-lime-strongest);}
.ͼln {color: var(--accent-green-strongest);}
.ͼlo {color: var(--accent-teal-strongest);}
.ͼl4 {text-decoration: underline;}
.ͼl5 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼl6 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼl7 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼl8 {font-style: italic;}
.ͼl9 {font-weight: var(--font-weight-bold);}
.ͼla {text-decoration: line-through;}
.ͼlb {font-family: var(--font-family-code);}
.ͼlc {color: var(--foreground-dimmest);}
.ͼld {color: var(--accent-blue-strongest);}
.ͼle {color: var(--accent-blue-stronger);}
.ͼlf {color: var(--accent-purple-stronger);}
.ͼlg {color: var(--accent-pink-stronger);}
.ͼl3.cm-focused {outline: 0 none;}
.ͼl3 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼl3 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼl3 .cm-line {line-height: var(--line-height-small);}
.ͼl3 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼl3 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼl3 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼl3 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼl3.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼl3 .cm-cursor, .ͼl3 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼl3 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼl3 .cm-activeLine {background-color: var(--background-higher);}
.ͼl3 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼl3 .cm-specialChar {color: var(--accent-negative-default);}
.ͼl3 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼl3 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼl3 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼl3 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼl3 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼl3 .cm-vim-panel input {color: var(--foreground-default);}
.ͼl3 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼl3 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼl3 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼl3 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼl3 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼl3 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼl3 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼl3 .cm-matchingBracket, .ͼl3 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼl3 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼl3 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼl3 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼl3 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼl3 .emmet-preview .cm-content {padding: 0 !important;}
.ͼl3 .emmet-preview .cm-scroller {z-index: 1;}
.ͼl3 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼl3 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼl3 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼl3 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼl3 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼl3 .cm-tooltip.multiplayer-tooltip, .ͼl3 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼl3 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼl3 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼl3 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼl3 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼl3 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼl3 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼl3 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼl3 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼkv {color: var(--foreground-default);}
.ͼkw {color: var(--outline-stronger);}
.ͼkx {color: var(--accent-red-default);}
.ͼky {color: var(--accent-orange-stronger);}
.ͼkz {color: var(--accent-yellow-stronger);}
.ͼl0 {color: var(--accent-lime-stronger);}
.ͼl1 {color: var(--accent-green-stronger);}
.ͼl2 {color: var(--accent-teal-stronger);}
.ͼkn {color: var(--foreground-default);}
.ͼko {color: var(--accent-green-default);}
.ͼkp {color: var(--accent-red-stronger);}
.ͼkq {color: var(--accent-orange-strongest);}
.ͼkr {color: var(--accent-yellow-strongest);}
.ͼks {color: var(--accent-lime-strongest);}
.ͼkt {color: var(--accent-green-strongest);}
.ͼku {color: var(--accent-teal-strongest);}
.ͼka {text-decoration: underline;}
.ͼkb {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼkc {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼkd {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼke {font-style: italic;}
.ͼkf {font-weight: var(--font-weight-bold);}
.ͼkg {text-decoration: line-through;}
.ͼkh {font-family: var(--font-family-code);}
.ͼki {color: var(--foreground-dimmest);}
.ͼkj {color: var(--accent-blue-strongest);}
.ͼkk {color: var(--accent-blue-stronger);}
.ͼkl {color: var(--accent-purple-stronger);}
.ͼkm {color: var(--accent-pink-stronger);}
.ͼk0.cm-focused {outline: 0 none;}
.ͼk0 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼk0 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼk0 .cm-line {line-height: var(--line-height-small);}
.ͼk0 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼk0 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼk0 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼk0 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼk0.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼk0 .cm-cursor, .ͼk0 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼk0 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼk0 .cm-activeLine {background-color: var(--background-higher);}
.ͼk0 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼk0 .cm-specialChar {color: var(--accent-negative-default);}
.ͼk0 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼk0 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼk0 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼk0 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼk0 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼk0 .cm-vim-panel input {color: var(--foreground-default);}
.ͼk0 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼk0 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼk0 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼk0 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼk0 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼk0 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼk0 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼk0 .cm-matchingBracket, .ͼk0 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼk0 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼk0 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼk0 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼk0 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼk0 .emmet-preview .cm-content {padding: 0 !important;}
.ͼk0 .emmet-preview .cm-scroller {z-index: 1;}
.ͼk0 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼk0 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼk0 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼk0 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼk0 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼk0 .cm-tooltip.multiplayer-tooltip, .ͼk0 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼk0 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼk0 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼk0 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼk0 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼk0 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼk0 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼk0 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼk0 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼjs {color: var(--foreground-default);}
.ͼjt {color: var(--outline-stronger);}
.ͼju {color: var(--accent-red-default);}
.ͼjv {color: var(--accent-orange-stronger);}
.ͼjw {color: var(--accent-yellow-stronger);}
.ͼjx {color: var(--accent-lime-stronger);}
.ͼjy {color: var(--accent-green-stronger);}
.ͼjz {color: var(--accent-teal-stronger);}
.ͼjk {color: var(--foreground-default);}
.ͼjl {color: var(--accent-green-default);}
.ͼjm {color: var(--accent-red-stronger);}
.ͼjn {color: var(--accent-orange-strongest);}
.ͼjo {color: var(--accent-yellow-strongest);}
.ͼjp {color: var(--accent-lime-strongest);}
.ͼjq {color: var(--accent-green-strongest);}
.ͼjr {color: var(--accent-teal-strongest);}
.ͼj7 {text-decoration: underline;}
.ͼj8 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼj9 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼja {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼjb {font-style: italic;}
.ͼjc {font-weight: var(--font-weight-bold);}
.ͼjd {text-decoration: line-through;}
.ͼje {font-family: var(--font-family-code);}
.ͼjf {color: var(--foreground-dimmest);}
.ͼjg {color: var(--accent-blue-strongest);}
.ͼjh {color: var(--accent-blue-stronger);}
.ͼji {color: var(--accent-purple-stronger);}
.ͼjj {color: var(--accent-pink-stronger);}
.ͼj2.cm-focused {outline: 0 none;}
.ͼj2 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼj2 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼj2 .cm-line {line-height: var(--line-height-small);}
.ͼj2 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼj2 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼj2 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼj2 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼj2.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼj2 .cm-cursor, .ͼj2 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼj2 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼj2 .cm-activeLine {background-color: var(--background-higher);}
.ͼj2 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼj2 .cm-specialChar {color: var(--accent-negative-default);}
.ͼj2 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼj2 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼj2 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼj2 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼj2 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼj2 .cm-vim-panel input {color: var(--foreground-default);}
.ͼj2 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼj2 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼj2 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼj2 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼj2 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼj2 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼj2 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼj2 .cm-matchingBracket, .ͼj2 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼj2 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼj2 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼj2 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼj2 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼj2 .emmet-preview .cm-content {padding: 0 !important;}
.ͼj2 .emmet-preview .cm-scroller {z-index: 1;}
.ͼj2 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼj2 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼj2 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼj2 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼj2 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼj2 .cm-tooltip.multiplayer-tooltip, .ͼj2 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼj2 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼj2 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼj2 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼj2 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼj2 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼj2 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼj2 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼj2 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼiu {color: var(--foreground-default);}
.ͼiv {color: var(--outline-stronger);}
.ͼiw {color: var(--accent-red-default);}
.ͼix {color: var(--accent-orange-stronger);}
.ͼiy {color: var(--accent-yellow-stronger);}
.ͼiz {color: var(--accent-lime-stronger);}
.ͼj0 {color: var(--accent-green-stronger);}
.ͼj1 {color: var(--accent-teal-stronger);}
.ͼim {color: var(--foreground-default);}
.ͼin {color: var(--accent-green-default);}
.ͼio {color: var(--accent-red-stronger);}
.ͼip {color: var(--accent-orange-strongest);}
.ͼiq {color: var(--accent-yellow-strongest);}
.ͼir {color: var(--accent-lime-strongest);}
.ͼis {color: var(--accent-green-strongest);}
.ͼit {color: var(--accent-teal-strongest);}
.ͼi9 {text-decoration: underline;}
.ͼia {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼib {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼic {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼid {font-style: italic;}
.ͼie {font-weight: var(--font-weight-bold);}
.ͼif {text-decoration: line-through;}
.ͼig {font-family: var(--font-family-code);}
.ͼih {color: var(--foreground-dimmest);}
.ͼii {color: var(--accent-blue-strongest);}
.ͼij {color: var(--accent-blue-stronger);}
.ͼik {color: var(--accent-purple-stronger);}
.ͼil {color: var(--accent-pink-stronger);}
.ͼi8.cm-focused {outline: 0 none;}
.ͼi8 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼi8 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼi8 .cm-line {line-height: var(--line-height-small);}
.ͼi8 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼi8 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼi8 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼi8 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼi8.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼi8 .cm-cursor, .ͼi8 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼi8 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼi8 .cm-activeLine {background-color: var(--background-higher);}
.ͼi8 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼi8 .cm-specialChar {color: var(--accent-negative-default);}
.ͼi8 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼi8 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼi8 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼi8 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼi8 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼi8 .cm-vim-panel input {color: var(--foreground-default);}
.ͼi8 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼi8 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼi8 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼi8 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼi8 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼi8 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼi8 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼi8 .cm-matchingBracket, .ͼi8 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼi8 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼi8 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼi8 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼi8 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼi8 .emmet-preview .cm-content {padding: 0 !important;}
.ͼi8 .emmet-preview .cm-scroller {z-index: 1;}
.ͼi8 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼi8 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼi8 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼi8 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼi8 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼi8 .cm-tooltip.multiplayer-tooltip, .ͼi8 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼi8 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼi8 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼi8 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼi8 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼi8 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼi8 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼi8 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼi8 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼi0 {color: var(--foreground-default);}
.ͼi1 {color: var(--outline-stronger);}
.ͼi2 {color: var(--accent-red-default);}
.ͼi3 {color: var(--accent-orange-stronger);}
.ͼi4 {color: var(--accent-yellow-stronger);}
.ͼi5 {color: var(--accent-lime-stronger);}
.ͼi6 {color: var(--accent-green-stronger);}
.ͼi7 {color: var(--accent-teal-stronger);}
.ͼhs {color: var(--foreground-default);}
.ͼht {color: var(--accent-green-default);}
.ͼhu {color: var(--accent-red-stronger);}
.ͼhv {color: var(--accent-orange-strongest);}
.ͼhw {color: var(--accent-yellow-strongest);}
.ͼhx {color: var(--accent-lime-strongest);}
.ͼhy {color: var(--accent-green-strongest);}
.ͼhz {color: var(--accent-teal-strongest);}
.ͼhf {text-decoration: underline;}
.ͼhg {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼhh {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼhi {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼhj {font-style: italic;}
.ͼhk {font-weight: var(--font-weight-bold);}
.ͼhl {text-decoration: line-through;}
.ͼhm {font-family: var(--font-family-code);}
.ͼhn {color: var(--foreground-dimmest);}
.ͼho {color: var(--accent-blue-strongest);}
.ͼhp {color: var(--accent-blue-stronger);}
.ͼhq {color: var(--accent-purple-stronger);}
.ͼhr {color: var(--accent-pink-stronger);}
.ͼhe.cm-focused {outline: 0 none;}
.ͼhe {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼhe .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼhe .cm-line {line-height: var(--line-height-small);}
.ͼhe .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼhe .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼhe .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼhe .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼhe.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼhe .cm-cursor, .ͼhe .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼhe .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼhe .cm-activeLine {background-color: var(--background-higher);}
.ͼhe .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼhe .cm-specialChar {color: var(--accent-negative-default);}
.ͼhe .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼhe .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼhe .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼhe .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼhe .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼhe .cm-vim-panel input {color: var(--foreground-default);}
.ͼhe .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼhe .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼhe .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼhe .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼhe .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼhe .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼhe .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼhe .cm-matchingBracket, .ͼhe .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼhe .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼhe .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼhe .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼhe .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼhe .emmet-preview .cm-content {padding: 0 !important;}
.ͼhe .emmet-preview .cm-scroller {z-index: 1;}
.ͼhe .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼhe .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼhe .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼhe .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼhe .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼhe .cm-tooltip.multiplayer-tooltip, .ͼhe .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼhe .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼhe .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼhe .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼhe .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼhe .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼhe .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼhe .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼhe .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼh6 {color: var(--foreground-default);}
.ͼh7 {color: var(--outline-stronger);}
.ͼh8 {color: var(--accent-red-default);}
.ͼh9 {color: var(--accent-orange-stronger);}
.ͼha {color: var(--accent-yellow-stronger);}
.ͼhb {color: var(--accent-lime-stronger);}
.ͼhc {color: var(--accent-green-stronger);}
.ͼhd {color: var(--accent-teal-stronger);}
.ͼgy {color: var(--foreground-default);}
.ͼgz {color: var(--accent-green-default);}
.ͼh0 {color: var(--accent-red-stronger);}
.ͼh1 {color: var(--accent-orange-strongest);}
.ͼh2 {color: var(--accent-yellow-strongest);}
.ͼh3 {color: var(--accent-lime-strongest);}
.ͼh4 {color: var(--accent-green-strongest);}
.ͼh5 {color: var(--accent-teal-strongest);}
.ͼgl {text-decoration: underline;}
.ͼgm {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼgn {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼgo {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼgp {font-style: italic;}
.ͼgq {font-weight: var(--font-weight-bold);}
.ͼgr {text-decoration: line-through;}
.ͼgs {font-family: var(--font-family-code);}
.ͼgt {color: var(--foreground-dimmest);}
.ͼgu {color: var(--accent-blue-strongest);}
.ͼgv {color: var(--accent-blue-stronger);}
.ͼgw {color: var(--accent-purple-stronger);}
.ͼgx {color: var(--accent-pink-stronger);}
.ͼgk.cm-focused {outline: 0 none;}
.ͼgk {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼgk .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼgk .cm-line {line-height: var(--line-height-small);}
.ͼgk .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼgk .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼgk .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼgk .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼgk.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼgk .cm-cursor, .ͼgk .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼgk .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼgk .cm-activeLine {background-color: var(--background-higher);}
.ͼgk .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼgk .cm-specialChar {color: var(--accent-negative-default);}
.ͼgk .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼgk .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼgk .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼgk .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼgk .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼgk .cm-vim-panel input {color: var(--foreground-default);}
.ͼgk .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼgk .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼgk .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼgk .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼgk .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼgk .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼgk .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼgk .cm-matchingBracket, .ͼgk .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼgk .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼgk .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼgk .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼgk .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼgk .emmet-preview .cm-content {padding: 0 !important;}
.ͼgk .emmet-preview .cm-scroller {z-index: 1;}
.ͼgk .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼgk .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼgk .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼgk .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼgk .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼgk .cm-tooltip.multiplayer-tooltip, .ͼgk .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼgk .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼgk .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼgk .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼgk .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼgk .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼgk .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼgk .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼgk .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼgc {color: var(--foreground-default);}
.ͼgd {color: var(--outline-stronger);}
.ͼge {color: var(--accent-red-default);}
.ͼgf {color: var(--accent-orange-stronger);}
.ͼgg {color: var(--accent-yellow-stronger);}
.ͼgh {color: var(--accent-lime-stronger);}
.ͼgi {color: var(--accent-green-stronger);}
.ͼgj {color: var(--accent-teal-stronger);}
.ͼg4 {color: var(--foreground-default);}
.ͼg5 {color: var(--accent-green-default);}
.ͼg6 {color: var(--accent-red-stronger);}
.ͼg7 {color: var(--accent-orange-strongest);}
.ͼg8 {color: var(--accent-yellow-strongest);}
.ͼg9 {color: var(--accent-lime-strongest);}
.ͼga {color: var(--accent-green-strongest);}
.ͼgb {color: var(--accent-teal-strongest);}
.ͼfr {text-decoration: underline;}
.ͼfs {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼft {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼfu {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼfv {font-style: italic;}
.ͼfw {font-weight: var(--font-weight-bold);}
.ͼfx {text-decoration: line-through;}
.ͼfy {font-family: var(--font-family-code);}
.ͼfz {color: var(--foreground-dimmest);}
.ͼg0 {color: var(--accent-blue-strongest);}
.ͼg1 {color: var(--accent-blue-stronger);}
.ͼg2 {color: var(--accent-purple-stronger);}
.ͼg3 {color: var(--accent-pink-stronger);}
.ͼfq.cm-focused {outline: 0 none;}
.ͼfq {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼfq .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼfq .cm-line {line-height: var(--line-height-small);}
.ͼfq .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼfq .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼfq .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼfq .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼfq.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼfq .cm-cursor, .ͼfq .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼfq .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼfq .cm-activeLine {background-color: var(--background-higher);}
.ͼfq .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼfq .cm-specialChar {color: var(--accent-negative-default);}
.ͼfq .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼfq .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼfq .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼfq .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼfq .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼfq .cm-vim-panel input {color: var(--foreground-default);}
.ͼfq .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼfq .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼfq .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼfq .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼfq .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼfq .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼfq .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼfq .cm-matchingBracket, .ͼfq .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼfq .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼfq .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼfq .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼfq .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼfq .emmet-preview .cm-content {padding: 0 !important;}
.ͼfq .emmet-preview .cm-scroller {z-index: 1;}
.ͼfq .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼfq .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼfq .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼfq .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼfq .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼfq .cm-tooltip.multiplayer-tooltip, .ͼfq .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼfq .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼfq .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼfq .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼfq .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼfq .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼfq .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼfq .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼfq .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼfi {color: var(--foreground-default);}
.ͼfj {color: var(--outline-stronger);}
.ͼfk {color: var(--accent-red-default);}
.ͼfl {color: var(--accent-orange-stronger);}
.ͼfm {color: var(--accent-yellow-stronger);}
.ͼfn {color: var(--accent-lime-stronger);}
.ͼfo {color: var(--accent-green-stronger);}
.ͼfp {color: var(--accent-teal-stronger);}
.ͼfa {color: var(--foreground-default);}
.ͼfb {color: var(--accent-green-default);}
.ͼfc {color: var(--accent-red-stronger);}
.ͼfd {color: var(--accent-orange-strongest);}
.ͼfe {color: var(--accent-yellow-strongest);}
.ͼff {color: var(--accent-lime-strongest);}
.ͼfg {color: var(--accent-green-strongest);}
.ͼfh {color: var(--accent-teal-strongest);}
.ͼex {text-decoration: underline;}
.ͼey {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼez {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼf0 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼf1 {font-style: italic;}
.ͼf2 {font-weight: var(--font-weight-bold);}
.ͼf3 {text-decoration: line-through;}
.ͼf4 {font-family: var(--font-family-code);}
.ͼf5 {color: var(--foreground-dimmest);}
.ͼf6 {color: var(--accent-blue-strongest);}
.ͼf7 {color: var(--accent-blue-stronger);}
.ͼf8 {color: var(--accent-purple-stronger);}
.ͼf9 {color: var(--accent-pink-stronger);}
.ͼew.cm-focused {outline: 0 none;}
.ͼew {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼew .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼew .cm-line {line-height: var(--line-height-small);}
.ͼew .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼew .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼew .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼew .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼew.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼew .cm-cursor, .ͼew .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼew .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼew .cm-activeLine {background-color: var(--background-higher);}
.ͼew .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼew .cm-specialChar {color: var(--accent-negative-default);}
.ͼew .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼew .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼew .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼew .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼew .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼew .cm-vim-panel input {color: var(--foreground-default);}
.ͼew .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼew .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼew .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼew .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼew .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼew .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼew .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼew .cm-matchingBracket, .ͼew .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼew .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼew .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼew .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼew .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼew .emmet-preview .cm-content {padding: 0 !important;}
.ͼew .emmet-preview .cm-scroller {z-index: 1;}
.ͼew .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼew .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼew .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼew .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼew .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼew .cm-tooltip.multiplayer-tooltip, .ͼew .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼew .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼew .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼew .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼew .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼew .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼew .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼew .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼew .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼeo {color: var(--foreground-default);}
.ͼep {color: var(--outline-stronger);}
.ͼeq {color: var(--accent-red-default);}
.ͼer {color: var(--accent-orange-stronger);}
.ͼes {color: var(--accent-yellow-stronger);}
.ͼet {color: var(--accent-lime-stronger);}
.ͼeu {color: var(--accent-green-stronger);}
.ͼev {color: var(--accent-teal-stronger);}
.ͼeg {color: var(--foreground-default);}
.ͼeh {color: var(--accent-green-default);}
.ͼei {color: var(--accent-red-stronger);}
.ͼej {color: var(--accent-orange-strongest);}
.ͼek {color: var(--accent-yellow-strongest);}
.ͼel {color: var(--accent-lime-strongest);}
.ͼem {color: var(--accent-green-strongest);}
.ͼen {color: var(--accent-teal-strongest);}
.ͼe3 {text-decoration: underline;}
.ͼe4 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼe5 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼe6 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼe7 {font-style: italic;}
.ͼe8 {font-weight: var(--font-weight-bold);}
.ͼe9 {text-decoration: line-through;}
.ͼea {font-family: var(--font-family-code);}
.ͼeb {color: var(--foreground-dimmest);}
.ͼec {color: var(--accent-blue-strongest);}
.ͼed {color: var(--accent-blue-stronger);}
.ͼee {color: var(--accent-purple-stronger);}
.ͼef {color: var(--accent-pink-stronger);}
.ͼe2.cm-focused {outline: 0 none;}
.ͼe2 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼe2 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼe2 .cm-line {line-height: var(--line-height-small);}
.ͼe2 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼe2 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼe2 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼe2 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼe2.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼe2 .cm-cursor, .ͼe2 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼe2 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼe2 .cm-activeLine {background-color: var(--background-higher);}
.ͼe2 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼe2 .cm-specialChar {color: var(--accent-negative-default);}
.ͼe2 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼe2 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼe2 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼe2 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼe2 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼe2 .cm-vim-panel input {color: var(--foreground-default);}
.ͼe2 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼe2 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼe2 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼe2 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼe2 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼe2 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼe2 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼe2 .cm-matchingBracket, .ͼe2 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼe2 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼe2 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼe2 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼe2 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼe2 .emmet-preview .cm-content {padding: 0 !important;}
.ͼe2 .emmet-preview .cm-scroller {z-index: 1;}
.ͼe2 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼe2 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼe2 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼe2 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼe2 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼe2 .cm-tooltip.multiplayer-tooltip, .ͼe2 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼe2 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼe2 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼe2 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼe2 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼe2 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼe2 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼe2 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼe2 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼdu {color: var(--foreground-default);}
.ͼdv {color: var(--outline-stronger);}
.ͼdw {color: var(--accent-red-default);}
.ͼdx {color: var(--accent-orange-stronger);}
.ͼdy {color: var(--accent-yellow-stronger);}
.ͼdz {color: var(--accent-lime-stronger);}
.ͼe0 {color: var(--accent-green-stronger);}
.ͼe1 {color: var(--accent-teal-stronger);}
.ͼdm {color: var(--foreground-default);}
.ͼdn {color: var(--accent-green-default);}
.ͼdo {color: var(--accent-red-stronger);}
.ͼdp {color: var(--accent-orange-strongest);}
.ͼdq {color: var(--accent-yellow-strongest);}
.ͼdr {color: var(--accent-lime-strongest);}
.ͼds {color: var(--accent-green-strongest);}
.ͼdt {color: var(--accent-teal-strongest);}
.ͼd9 {text-decoration: underline;}
.ͼda {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼdb {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼdc {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼdd {font-style: italic;}
.ͼde {font-weight: var(--font-weight-bold);}
.ͼdf {text-decoration: line-through;}
.ͼdg {font-family: var(--font-family-code);}
.ͼdh {color: var(--foreground-dimmest);}
.ͼdi {color: var(--accent-blue-strongest);}
.ͼdj {color: var(--accent-blue-stronger);}
.ͼdk {color: var(--accent-purple-stronger);}
.ͼdl {color: var(--accent-pink-stronger);}
.ͼd8.cm-focused {outline: 0 none;}
.ͼd8 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼd8 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼd8 .cm-line {line-height: var(--line-height-small);}
.ͼd8 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼd8 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼd8 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼd8 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼd8.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼd8 .cm-cursor, .ͼd8 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼd8 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼd8 .cm-activeLine {background-color: var(--background-higher);}
.ͼd8 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼd8 .cm-specialChar {color: var(--accent-negative-default);}
.ͼd8 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼd8 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼd8 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼd8 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼd8 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼd8 .cm-vim-panel input {color: var(--foreground-default);}
.ͼd8 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼd8 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼd8 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼd8 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼd8 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼd8 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼd8 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼd8 .cm-matchingBracket, .ͼd8 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼd8 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼd8 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼd8 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼd8 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼd8 .emmet-preview .cm-content {padding: 0 !important;}
.ͼd8 .emmet-preview .cm-scroller {z-index: 1;}
.ͼd8 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼd8 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼd8 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼd8 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼd8 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼd8 .cm-tooltip.multiplayer-tooltip, .ͼd8 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼd8 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼd8 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼd8 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼd8 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼd8 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼd8 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼd8 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼd8 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼd0 {color: var(--foreground-default);}
.ͼd1 {color: var(--outline-stronger);}
.ͼd2 {color: var(--accent-red-default);}
.ͼd3 {color: var(--accent-orange-stronger);}
.ͼd4 {color: var(--accent-yellow-stronger);}
.ͼd5 {color: var(--accent-lime-stronger);}
.ͼd6 {color: var(--accent-green-stronger);}
.ͼd7 {color: var(--accent-teal-stronger);}
.ͼcs {color: var(--foreground-default);}
.ͼct {color: var(--accent-green-default);}
.ͼcu {color: var(--accent-red-stronger);}
.ͼcv {color: var(--accent-orange-strongest);}
.ͼcw {color: var(--accent-yellow-strongest);}
.ͼcx {color: var(--accent-lime-strongest);}
.ͼcy {color: var(--accent-green-strongest);}
.ͼcz {color: var(--accent-teal-strongest);}
.ͼcf {text-decoration: underline;}
.ͼcg {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼch {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼci {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼcj {font-style: italic;}
.ͼck {font-weight: var(--font-weight-bold);}
.ͼcl {text-decoration: line-through;}
.ͼcm {font-family: var(--font-family-code);}
.ͼcn {color: var(--foreground-dimmest);}
.ͼco {color: var(--accent-blue-strongest);}
.ͼcp {color: var(--accent-blue-stronger);}
.ͼcq {color: var(--accent-purple-stronger);}
.ͼcr {color: var(--accent-pink-stronger);}
.ͼce.cm-focused {outline: 0 none;}
.ͼce {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼce .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼce .cm-line {line-height: var(--line-height-small);}
.ͼce .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼce .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼce .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼce .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼce.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼce .cm-cursor, .ͼce .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼce .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼce .cm-activeLine {background-color: var(--background-higher);}
.ͼce .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼce .cm-specialChar {color: var(--accent-negative-default);}
.ͼce .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼce .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼce .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼce .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼce .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼce .cm-vim-panel input {color: var(--foreground-default);}
.ͼce .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼce .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼce .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼce .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼce .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼce .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼce .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼce .cm-matchingBracket, .ͼce .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼce .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼce .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼce .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼce .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼce .emmet-preview .cm-content {padding: 0 !important;}
.ͼce .emmet-preview .cm-scroller {z-index: 1;}
.ͼce .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼce .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼce .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼce .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼce .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼce .cm-tooltip.multiplayer-tooltip, .ͼce .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼce .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼce .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼce .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼce .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼce .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼce .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼce .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼce .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼc6 {color: var(--foreground-default);}
.ͼc7 {color: var(--outline-stronger);}
.ͼc8 {color: var(--accent-red-default);}
.ͼc9 {color: var(--accent-orange-stronger);}
.ͼca {color: var(--accent-yellow-stronger);}
.ͼcb {color: var(--accent-lime-stronger);}
.ͼcc {color: var(--accent-green-stronger);}
.ͼcd {color: var(--accent-teal-stronger);}
.ͼby {color: var(--foreground-default);}
.ͼbz {color: var(--accent-green-default);}
.ͼc0 {color: var(--accent-red-stronger);}
.ͼc1 {color: var(--accent-orange-strongest);}
.ͼc2 {color: var(--accent-yellow-strongest);}
.ͼc3 {color: var(--accent-lime-strongest);}
.ͼc4 {color: var(--accent-green-strongest);}
.ͼc5 {color: var(--accent-teal-strongest);}
.ͼbl {text-decoration: underline;}
.ͼbm {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼbn {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼbo {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼbp {font-style: italic;}
.ͼbq {font-weight: var(--font-weight-bold);}
.ͼbr {text-decoration: line-through;}
.ͼbs {font-family: var(--font-family-code);}
.ͼbt {color: var(--foreground-dimmest);}
.ͼbu {color: var(--accent-blue-strongest);}
.ͼbv {color: var(--accent-blue-stronger);}
.ͼbw {color: var(--accent-purple-stronger);}
.ͼbx {color: var(--accent-pink-stronger);}
.ͼbk.cm-focused {outline: 0 none;}
.ͼbk {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼbk .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼbk .cm-line {line-height: var(--line-height-small);}
.ͼbk .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼbk .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼbk .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼbk .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼbk.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼbk .cm-cursor, .ͼbk .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼbk .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼbk .cm-activeLine {background-color: var(--background-higher);}
.ͼbk .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼbk .cm-specialChar {color: var(--accent-negative-default);}
.ͼbk .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼbk .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼbk .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼbk .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼbk .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼbk .cm-vim-panel input {color: var(--foreground-default);}
.ͼbk .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼbk .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼbk .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼbk .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼbk .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼbk .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼbk .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼbk .cm-matchingBracket, .ͼbk .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼbk .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼbk .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼbk .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼbk .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼbk .emmet-preview .cm-content {padding: 0 !important;}
.ͼbk .emmet-preview .cm-scroller {z-index: 1;}
.ͼbk .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼbk .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼbk .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼbk .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼbk .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼbk .cm-tooltip.multiplayer-tooltip, .ͼbk .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼbk .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼbk .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼbk .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼbk .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼbk .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼbk .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼbk .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼbk .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼbc {color: var(--foreground-default);}
.ͼbd {color: var(--outline-stronger);}
.ͼbe {color: var(--accent-red-default);}
.ͼbf {color: var(--accent-orange-stronger);}
.ͼbg {color: var(--accent-yellow-stronger);}
.ͼbh {color: var(--accent-lime-stronger);}
.ͼbi {color: var(--accent-green-stronger);}
.ͼbj {color: var(--accent-teal-stronger);}
.ͼb4 {color: var(--foreground-default);}
.ͼb5 {color: var(--accent-green-default);}
.ͼb6 {color: var(--accent-red-stronger);}
.ͼb7 {color: var(--accent-orange-strongest);}
.ͼb8 {color: var(--accent-yellow-strongest);}
.ͼb9 {color: var(--accent-lime-strongest);}
.ͼba {color: var(--accent-green-strongest);}
.ͼbb {color: var(--accent-teal-strongest);}
.ͼar {text-decoration: underline;}
.ͼas {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼat {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼau {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼav {font-style: italic;}
.ͼaw {font-weight: var(--font-weight-bold);}
.ͼax {text-decoration: line-through;}
.ͼay {font-family: var(--font-family-code);}
.ͼaz {color: var(--foreground-dimmest);}
.ͼb0 {color: var(--accent-blue-strongest);}
.ͼb1 {color: var(--accent-blue-stronger);}
.ͼb2 {color: var(--accent-purple-stronger);}
.ͼb3 {color: var(--accent-pink-stronger);}
.ͼaq.cm-focused {outline: 0 none;}
.ͼaq {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼaq .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼaq .cm-line {line-height: var(--line-height-small);}
.ͼaq .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼaq .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼaq .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼaq .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼaq.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼaq .cm-cursor, .ͼaq .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼaq .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼaq .cm-activeLine {background-color: var(--background-higher);}
.ͼaq .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼaq .cm-specialChar {color: var(--accent-negative-default);}
.ͼaq .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼaq .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼaq .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼaq .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼaq .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼaq .cm-vim-panel input {color: var(--foreground-default);}
.ͼaq .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼaq .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼaq .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼaq .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼaq .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼaq .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼaq .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼaq .cm-matchingBracket, .ͼaq .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼaq .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼaq .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼaq .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼaq .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼaq .emmet-preview .cm-content {padding: 0 !important;}
.ͼaq .emmet-preview .cm-scroller {z-index: 1;}
.ͼaq .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼaq .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼaq .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼaq .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼaq .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼaq .cm-tooltip.multiplayer-tooltip, .ͼaq .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼaq .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼaq .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼaq .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼaq .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼaq .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼaq .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼaq .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼaq .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼai {color: var(--foreground-default);}
.ͼaj {color: var(--outline-stronger);}
.ͼak {color: var(--accent-red-default);}
.ͼal {color: var(--accent-orange-stronger);}
.ͼam {color: var(--accent-yellow-stronger);}
.ͼan {color: var(--accent-lime-stronger);}
.ͼao {color: var(--accent-green-stronger);}
.ͼap {color: var(--accent-teal-stronger);}
.ͼaa {color: var(--foreground-default);}
.ͼab {color: var(--accent-green-default);}
.ͼac {color: var(--accent-red-stronger);}
.ͼad {color: var(--accent-orange-strongest);}
.ͼae {color: var(--accent-yellow-strongest);}
.ͼaf {color: var(--accent-lime-strongest);}
.ͼag {color: var(--accent-green-strongest);}
.ͼah {color: var(--accent-teal-strongest);}
.ͼ9x {text-decoration: underline;}
.ͼ9y {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ9z {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼa0 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼa1 {font-style: italic;}
.ͼa2 {font-weight: var(--font-weight-bold);}
.ͼa3 {text-decoration: line-through;}
.ͼa4 {font-family: var(--font-family-code);}
.ͼa5 {color: var(--foreground-dimmest);}
.ͼa6 {color: var(--accent-blue-strongest);}
.ͼa7 {color: var(--accent-blue-stronger);}
.ͼa8 {color: var(--accent-purple-stronger);}
.ͼa9 {color: var(--accent-pink-stronger);}
.ͼ9w.cm-focused {outline: 0 none;}
.ͼ9w {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ9w .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ9w .cm-line {line-height: var(--line-height-small);}
.ͼ9w .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ9w .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ9w .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ9w .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ9w.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ9w .cm-cursor, .ͼ9w .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ9w .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ9w .cm-activeLine {background-color: var(--background-higher);}
.ͼ9w .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ9w .cm-specialChar {color: var(--accent-negative-default);}
.ͼ9w .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ9w .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ9w .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ9w .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ9w .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ9w .cm-vim-panel input {color: var(--foreground-default);}
.ͼ9w .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ9w .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ9w .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ9w .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ9w .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ9w .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ9w .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ9w .cm-matchingBracket, .ͼ9w .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ9w .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ9w .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ9w .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ9w .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ9w .emmet-preview .cm-content {padding: 0 !important;}
.ͼ9w .emmet-preview .cm-scroller {z-index: 1;}
.ͼ9w .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ9w .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ9w .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ9w .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ9w .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ9w .cm-tooltip.multiplayer-tooltip, .ͼ9w .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ9w .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ9w .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ9w .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ9w .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ9w .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ9w .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ9w .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ9w .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ9o {color: var(--foreground-default);}
.ͼ9p {color: var(--outline-stronger);}
.ͼ9q {color: var(--accent-red-default);}
.ͼ9r {color: var(--accent-orange-stronger);}
.ͼ9s {color: var(--accent-yellow-stronger);}
.ͼ9t {color: var(--accent-lime-stronger);}
.ͼ9u {color: var(--accent-green-stronger);}
.ͼ9v {color: var(--accent-teal-stronger);}
.ͼ9g {color: var(--foreground-default);}
.ͼ9h {color: var(--accent-green-default);}
.ͼ9i {color: var(--accent-red-stronger);}
.ͼ9j {color: var(--accent-orange-strongest);}
.ͼ9k {color: var(--accent-yellow-strongest);}
.ͼ9l {color: var(--accent-lime-strongest);}
.ͼ9m {color: var(--accent-green-strongest);}
.ͼ9n {color: var(--accent-teal-strongest);}
.ͼ93 {text-decoration: underline;}
.ͼ94 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ95 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ96 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ97 {font-style: italic;}
.ͼ98 {font-weight: var(--font-weight-bold);}
.ͼ99 {text-decoration: line-through;}
.ͼ9a {font-family: var(--font-family-code);}
.ͼ9b {color: var(--foreground-dimmest);}
.ͼ9c {color: var(--accent-blue-strongest);}
.ͼ9d {color: var(--accent-blue-stronger);}
.ͼ9e {color: var(--accent-purple-stronger);}
.ͼ9f {color: var(--accent-pink-stronger);}
.ͼ92.cm-focused {outline: 0 none;}
.ͼ92 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ92 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ92 .cm-line {line-height: var(--line-height-small);}
.ͼ92 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ92 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ92 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ92 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ92.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ92 .cm-cursor, .ͼ92 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ92 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ92 .cm-activeLine {background-color: var(--background-higher);}
.ͼ92 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ92 .cm-specialChar {color: var(--accent-negative-default);}
.ͼ92 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ92 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ92 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ92 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ92 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ92 .cm-vim-panel input {color: var(--foreground-default);}
.ͼ92 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ92 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ92 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ92 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ92 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ92 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ92 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ92 .cm-matchingBracket, .ͼ92 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ92 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ92 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ92 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ92 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ92 .emmet-preview .cm-content {padding: 0 !important;}
.ͼ92 .emmet-preview .cm-scroller {z-index: 1;}
.ͼ92 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ92 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ92 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ92 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ92 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ92 .cm-tooltip.multiplayer-tooltip, .ͼ92 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ92 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ92 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ92 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ92 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ92 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ92 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ92 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ92 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ8u {color: var(--foreground-default);}
.ͼ8v {color: var(--outline-stronger);}
.ͼ8w {color: var(--accent-red-default);}
.ͼ8x {color: var(--accent-orange-stronger);}
.ͼ8y {color: var(--accent-yellow-stronger);}
.ͼ8z {color: var(--accent-lime-stronger);}
.ͼ90 {color: var(--accent-green-stronger);}
.ͼ91 {color: var(--accent-teal-stronger);}
.ͼ8m {color: var(--foreground-default);}
.ͼ8n {color: var(--accent-green-default);}
.ͼ8o {color: var(--accent-red-stronger);}
.ͼ8p {color: var(--accent-orange-strongest);}
.ͼ8q {color: var(--accent-yellow-strongest);}
.ͼ8r {color: var(--accent-lime-strongest);}
.ͼ8s {color: var(--accent-green-strongest);}
.ͼ8t {color: var(--accent-teal-strongest);}
.ͼ89 {text-decoration: underline;}
.ͼ8a {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ8b {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ8c {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ8d {font-style: italic;}
.ͼ8e {font-weight: var(--font-weight-bold);}
.ͼ8f {text-decoration: line-through;}
.ͼ8g {font-family: var(--font-family-code);}
.ͼ8h {color: var(--foreground-dimmest);}
.ͼ8i {color: var(--accent-blue-strongest);}
.ͼ8j {color: var(--accent-blue-stronger);}
.ͼ8k {color: var(--accent-purple-stronger);}
.ͼ8l {color: var(--accent-pink-stronger);}
.ͼ88.cm-focused {outline: 0 none;}
.ͼ88 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ88 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ88 .cm-line {line-height: var(--line-height-small);}
.ͼ88 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ88 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ88 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ88 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ88.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ88 .cm-cursor, .ͼ88 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ88 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ88 .cm-activeLine {background-color: var(--background-higher);}
.ͼ88 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ88 .cm-specialChar {color: var(--accent-negative-default);}
.ͼ88 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ88 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ88 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ88 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ88 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ88 .cm-vim-panel input {color: var(--foreground-default);}
.ͼ88 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ88 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ88 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ88 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ88 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ88 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ88 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ88 .cm-matchingBracket, .ͼ88 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ88 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ88 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ88 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ88 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ88 .emmet-preview .cm-content {padding: 0 !important;}
.ͼ88 .emmet-preview .cm-scroller {z-index: 1;}
.ͼ88 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ88 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ88 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ88 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ88 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ88 .cm-tooltip.multiplayer-tooltip, .ͼ88 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ88 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ88 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ88 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ88 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ88 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ88 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ88 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ88 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ80 {color: var(--foreground-default);}
.ͼ81 {color: var(--outline-stronger);}
.ͼ82 {color: var(--accent-red-default);}
.ͼ83 {color: var(--accent-orange-stronger);}
.ͼ84 {color: var(--accent-yellow-stronger);}
.ͼ85 {color: var(--accent-lime-stronger);}
.ͼ86 {color: var(--accent-green-stronger);}
.ͼ87 {color: var(--accent-teal-stronger);}
.ͼ7s {color: var(--foreground-default);}
.ͼ7t {color: var(--accent-green-default);}
.ͼ7u {color: var(--accent-red-stronger);}
.ͼ7v {color: var(--accent-orange-strongest);}
.ͼ7w {color: var(--accent-yellow-strongest);}
.ͼ7x {color: var(--accent-lime-strongest);}
.ͼ7y {color: var(--accent-green-strongest);}
.ͼ7z {color: var(--accent-teal-strongest);}
.ͼ7f {text-decoration: underline;}
.ͼ7g {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ7h {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ7i {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ7j {font-style: italic;}
.ͼ7k {font-weight: var(--font-weight-bold);}
.ͼ7l {text-decoration: line-through;}
.ͼ7m {font-family: var(--font-family-code);}
.ͼ7n {color: var(--foreground-dimmest);}
.ͼ7o {color: var(--accent-blue-strongest);}
.ͼ7p {color: var(--accent-blue-stronger);}
.ͼ7q {color: var(--accent-purple-stronger);}
.ͼ7r {color: var(--accent-pink-stronger);}
.ͼ7e.cm-focused {outline: 0 none;}
.ͼ7e {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ7e .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ7e .cm-line {line-height: var(--line-height-small);}
.ͼ7e .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ7e .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ7e .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ7e .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ7e.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ7e .cm-cursor, .ͼ7e .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ7e .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ7e .cm-activeLine {background-color: var(--background-higher);}
.ͼ7e .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ7e .cm-specialChar {color: var(--accent-negative-default);}
.ͼ7e .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ7e .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ7e .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ7e .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ7e .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ7e .cm-vim-panel input {color: var(--foreground-default);}
.ͼ7e .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ7e .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ7e .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ7e .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ7e .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ7e .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ7e .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ7e .cm-matchingBracket, .ͼ7e .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ7e .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ7e .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ7e .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ7e .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ7e .emmet-preview .cm-content {padding: 0 !important;}
.ͼ7e .emmet-preview .cm-scroller {z-index: 1;}
.ͼ7e .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ7e .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ7e .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ7e .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ7e .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ7e .cm-tooltip.multiplayer-tooltip, .ͼ7e .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ7e .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ7e .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ7e .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ7e .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ7e .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ7e .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ7e .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ7e .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ76 {color: var(--foreground-default);}
.ͼ77 {color: var(--outline-stronger);}
.ͼ78 {color: var(--accent-red-default);}
.ͼ79 {color: var(--accent-orange-stronger);}
.ͼ7a {color: var(--accent-yellow-stronger);}
.ͼ7b {color: var(--accent-lime-stronger);}
.ͼ7c {color: var(--accent-green-stronger);}
.ͼ7d {color: var(--accent-teal-stronger);}
.ͼ6y {color: var(--foreground-default);}
.ͼ6z {color: var(--accent-green-default);}
.ͼ70 {color: var(--accent-red-stronger);}
.ͼ71 {color: var(--accent-orange-strongest);}
.ͼ72 {color: var(--accent-yellow-strongest);}
.ͼ73 {color: var(--accent-lime-strongest);}
.ͼ74 {color: var(--accent-green-strongest);}
.ͼ75 {color: var(--accent-teal-strongest);}
.ͼ6l {text-decoration: underline;}
.ͼ6m {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ6n {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ6o {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ6p {font-style: italic;}
.ͼ6q {font-weight: var(--font-weight-bold);}
.ͼ6r {text-decoration: line-through;}
.ͼ6s {font-family: var(--font-family-code);}
.ͼ6t {color: var(--foreground-dimmest);}
.ͼ6u {color: var(--accent-blue-strongest);}
.ͼ6v {color: var(--accent-blue-stronger);}
.ͼ6w {color: var(--accent-purple-stronger);}
.ͼ6x {color: var(--accent-pink-stronger);}
.ͼ6k.cm-focused {outline: 0 none;}
.ͼ6k {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ6k .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ6k .cm-line {line-height: var(--line-height-small);}
.ͼ6k .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ6k .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ6k .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ6k .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ6k.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ6k .cm-cursor, .ͼ6k .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ6k .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ6k .cm-activeLine {background-color: var(--background-higher);}
.ͼ6k .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ6k .cm-specialChar {color: var(--accent-negative-default);}
.ͼ6k .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ6k .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ6k .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ6k .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ6k .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ6k .cm-vim-panel input {color: var(--foreground-default);}
.ͼ6k .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ6k .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ6k .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ6k .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ6k .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ6k .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ6k .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ6k .cm-matchingBracket, .ͼ6k .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ6k .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ6k .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ6k .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ6k .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ6k .emmet-preview .cm-content {padding: 0 !important;}
.ͼ6k .emmet-preview .cm-scroller {z-index: 1;}
.ͼ6k .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ6k .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ6k .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ6k .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ6k .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ6k .cm-tooltip.multiplayer-tooltip, .ͼ6k .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ6k .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ6k .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ6k .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ6k .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ6k .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ6k .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ6k .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ6k .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ6c {color: var(--foreground-default);}
.ͼ6d {color: var(--outline-stronger);}
.ͼ6e {color: var(--accent-red-default);}
.ͼ6f {color: var(--accent-orange-stronger);}
.ͼ6g {color: var(--accent-yellow-stronger);}
.ͼ6h {color: var(--accent-lime-stronger);}
.ͼ6i {color: var(--accent-green-stronger);}
.ͼ6j {color: var(--accent-teal-stronger);}
.ͼ64 {color: var(--foreground-default);}
.ͼ65 {color: var(--accent-green-default);}
.ͼ66 {color: var(--accent-red-stronger);}
.ͼ67 {color: var(--accent-orange-strongest);}
.ͼ68 {color: var(--accent-yellow-strongest);}
.ͼ69 {color: var(--accent-lime-strongest);}
.ͼ6a {color: var(--accent-green-strongest);}
.ͼ6b {color: var(--accent-teal-strongest);}
.ͼ5r {text-decoration: underline;}
.ͼ5s {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ5t {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ5u {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ5v {font-style: italic;}
.ͼ5w {font-weight: var(--font-weight-bold);}
.ͼ5x {text-decoration: line-through;}
.ͼ5y {font-family: var(--font-family-code);}
.ͼ5z {color: var(--foreground-dimmest);}
.ͼ60 {color: var(--accent-blue-strongest);}
.ͼ61 {color: var(--accent-blue-stronger);}
.ͼ62 {color: var(--accent-purple-stronger);}
.ͼ63 {color: var(--accent-pink-stronger);}
.ͼ5q.cm-focused {outline: 0 none;}
.ͼ5q {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ5q .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ5q .cm-line {line-height: var(--line-height-small);}
.ͼ5q .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ5q .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ5q .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ5q .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ5q.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ5q .cm-cursor, .ͼ5q .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ5q .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ5q .cm-activeLine {background-color: var(--background-higher);}
.ͼ5q .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ5q .cm-specialChar {color: var(--accent-negative-default);}
.ͼ5q .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ5q .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ5q .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ5q .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ5q .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ5q .cm-vim-panel input {color: var(--foreground-default);}
.ͼ5q .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ5q .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ5q .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ5q .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ5q .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ5q .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ5q .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ5q .cm-matchingBracket, .ͼ5q .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ5q .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ5q .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ5q .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ5q .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ5q .emmet-preview .cm-content {padding: 0 !important;}
.ͼ5q .emmet-preview .cm-scroller {z-index: 1;}
.ͼ5q .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ5q .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ5q .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ5q .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ5q .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ5q .cm-tooltip.multiplayer-tooltip, .ͼ5q .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ5q .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ5q .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ5q .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ5q .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ5q .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ5q .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ5q .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ5q .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ5i {color: var(--foreground-default);}
.ͼ5j {color: var(--outline-stronger);}
.ͼ5k {color: var(--accent-red-default);}
.ͼ5l {color: var(--accent-orange-stronger);}
.ͼ5m {color: var(--accent-yellow-stronger);}
.ͼ5n {color: var(--accent-lime-stronger);}
.ͼ5o {color: var(--accent-green-stronger);}
.ͼ5p {color: var(--accent-teal-stronger);}
.ͼ5a {color: var(--foreground-default);}
.ͼ5b {color: var(--accent-green-default);}
.ͼ5c {color: var(--accent-red-stronger);}
.ͼ5d {color: var(--accent-orange-strongest);}
.ͼ5e {color: var(--accent-yellow-strongest);}
.ͼ5f {color: var(--accent-lime-strongest);}
.ͼ5g {color: var(--accent-green-strongest);}
.ͼ5h {color: var(--accent-teal-strongest);}
.ͼ4x {text-decoration: underline;}
.ͼ4y {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ4z {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ50 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ51 {font-style: italic;}
.ͼ52 {font-weight: var(--font-weight-bold);}
.ͼ53 {text-decoration: line-through;}
.ͼ54 {font-family: var(--font-family-code);}
.ͼ55 {color: var(--foreground-dimmest);}
.ͼ56 {color: var(--accent-blue-strongest);}
.ͼ57 {color: var(--accent-blue-stronger);}
.ͼ58 {color: var(--accent-purple-stronger);}
.ͼ59 {color: var(--accent-pink-stronger);}
.ͼ4w.cm-focused {outline: 0 none;}
.ͼ4w {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ4w .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ4w .cm-line {line-height: var(--line-height-small);}
.ͼ4w .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ4w .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ4w .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ4w .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ4w.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ4w .cm-cursor, .ͼ4w .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ4w .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ4w .cm-activeLine {background-color: var(--background-higher);}
.ͼ4w .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ4w .cm-specialChar {color: var(--accent-negative-default);}
.ͼ4w .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ4w .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ4w .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ4w .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ4w .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ4w .cm-vim-panel input {color: var(--foreground-default);}
.ͼ4w .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ4w .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ4w .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ4w .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ4w .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ4w .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ4w .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ4w .cm-matchingBracket, .ͼ4w .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ4w .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ4w .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ4w .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ4w .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ4w .emmet-preview .cm-content {padding: 0 !important;}
.ͼ4w .emmet-preview .cm-scroller {z-index: 1;}
.ͼ4w .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ4w .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ4w .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ4w .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ4w .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ4w .cm-tooltip.multiplayer-tooltip, .ͼ4w .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ4w .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ4w .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ4w .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ4w .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ4w .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ4w .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ4w .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ4w .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ4o {color: var(--foreground-default);}
.ͼ4p {color: var(--outline-stronger);}
.ͼ4q {color: var(--accent-red-default);}
.ͼ4r {color: var(--accent-orange-stronger);}
.ͼ4s {color: var(--accent-yellow-stronger);}
.ͼ4t {color: var(--accent-lime-stronger);}
.ͼ4u {color: var(--accent-green-stronger);}
.ͼ4v {color: var(--accent-teal-stronger);}
.ͼ4g {color: var(--foreground-default);}
.ͼ4h {color: var(--accent-green-default);}
.ͼ4i {color: var(--accent-red-stronger);}
.ͼ4j {color: var(--accent-orange-strongest);}
.ͼ4k {color: var(--accent-yellow-strongest);}
.ͼ4l {color: var(--accent-lime-strongest);}
.ͼ4m {color: var(--accent-green-strongest);}
.ͼ4n {color: var(--accent-teal-strongest);}
.ͼ43 {text-decoration: underline;}
.ͼ44 {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ45 {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ46 {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ47 {font-style: italic;}
.ͼ48 {font-weight: var(--font-weight-bold);}
.ͼ49 {text-decoration: line-through;}
.ͼ4a {font-family: var(--font-family-code);}
.ͼ4b {color: var(--foreground-dimmest);}
.ͼ4c {color: var(--accent-blue-strongest);}
.ͼ4d {color: var(--accent-blue-stronger);}
.ͼ4e {color: var(--accent-purple-stronger);}
.ͼ4f {color: var(--accent-pink-stronger);}
.ͼ42.cm-focused {outline: 0 none;}
.ͼ42 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ42 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ42 .cm-line {line-height: var(--line-height-small);}
.ͼ42 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ42 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ42 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ42 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ42.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ42 .cm-cursor, .ͼ42 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ42 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ42 .cm-activeLine {background-color: var(--background-higher);}
.ͼ42 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ42 .cm-specialChar {color: var(--accent-negative-default);}
.ͼ42 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ42 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ42 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ42 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ42 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ42 .cm-vim-panel input {color: var(--foreground-default);}
.ͼ42 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ42 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ42 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ42 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ42 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ42 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ42 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ42 .cm-matchingBracket, .ͼ42 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ42 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ42 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ42 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ42 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ42 .emmet-preview .cm-content {padding: 0 !important;}
.ͼ42 .emmet-preview .cm-scroller {z-index: 1;}
.ͼ42 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ42 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ42 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ42 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ42 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ42 .cm-tooltip.multiplayer-tooltip, .ͼ42 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ42 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ42 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ42 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ42 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ42 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ42 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ42 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ42 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ3u {color: var(--foreground-default);}
.ͼ3v {color: var(--outline-stronger);}
.ͼ3w {color: var(--accent-red-default);}
.ͼ3x {color: var(--accent-orange-stronger);}
.ͼ3y {color: var(--accent-yellow-stronger);}
.ͼ3z {color: var(--accent-lime-stronger);}
.ͼ40 {color: var(--accent-green-stronger);}
.ͼ41 {color: var(--accent-teal-stronger);}
.ͼ3m {color: var(--foreground-default);}
.ͼ3n {color: var(--accent-green-default);}
.ͼ3o {color: var(--accent-red-stronger);}
.ͼ3p {color: var(--accent-orange-strongest);}
.ͼ3q {color: var(--accent-yellow-strongest);}
.ͼ3r {color: var(--accent-lime-strongest);}
.ͼ3s {color: var(--accent-green-strongest);}
.ͼ3t {color: var(--accent-teal-strongest);}
.ͼ39 {text-decoration: underline;}
.ͼ3a {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ3b {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ3c {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ3d {font-style: italic;}
.ͼ3e {font-weight: var(--font-weight-bold);}
.ͼ3f {text-decoration: line-through;}
.ͼ3g {font-family: var(--font-family-code);}
.ͼ3h {color: var(--foreground-dimmest);}
.ͼ3i {color: var(--accent-blue-strongest);}
.ͼ3j {color: var(--accent-blue-stronger);}
.ͼ3k {color: var(--accent-purple-stronger);}
.ͼ3l {color: var(--accent-pink-stronger);}
.ͼ38.cm-focused {outline: 0 none;}
.ͼ38 {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ38 .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ38 .cm-line {line-height: var(--line-height-small);}
.ͼ38 .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ38 .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ38 .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ38 .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ38.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ38 .cm-cursor, .ͼ38 .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ38 .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ38 .cm-activeLine {background-color: var(--background-higher);}
.ͼ38 .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ38 .cm-specialChar {color: var(--accent-negative-default);}
.ͼ38 .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ38 .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ38 .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ38 .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ38 .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ38 .cm-vim-panel input {color: var(--foreground-default);}
.ͼ38 .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ38 .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ38 .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ38 .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ38 .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ38 .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ38 .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ38 .cm-matchingBracket, .ͼ38 .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ38 .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ38 .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ38 .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ38 .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ38 .emmet-preview .cm-content {padding: 0 !important;}
.ͼ38 .emmet-preview .cm-scroller {z-index: 1;}
.ͼ38 .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ38 .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ38 .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ38 .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ38 .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ38 .cm-tooltip.multiplayer-tooltip, .ͼ38 .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ38 .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ38 .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ38 .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ38 .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ38 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ38 .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ38 .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ38 .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ30 {color: var(--foreground-default);}
.ͼ31 {color: var(--outline-stronger);}
.ͼ32 {color: var(--accent-red-default);}
.ͼ33 {color: var(--accent-orange-stronger);}
.ͼ34 {color: var(--accent-yellow-stronger);}
.ͼ35 {color: var(--accent-lime-stronger);}
.ͼ36 {color: var(--accent-green-stronger);}
.ͼ37 {color: var(--accent-teal-stronger);}
.ͼ2s {color: var(--foreground-default);}
.ͼ2t {color: var(--accent-green-default);}
.ͼ2u {color: var(--accent-red-stronger);}
.ͼ2v {color: var(--accent-orange-strongest);}
.ͼ2w {color: var(--accent-yellow-strongest);}
.ͼ2x {color: var(--accent-lime-strongest);}
.ͼ2y {color: var(--accent-green-strongest);}
.ͼ2z {color: var(--accent-teal-strongest);}
.ͼ2f {text-decoration: underline;}
.ͼ2g {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ2h {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ2i {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ2j {font-style: italic;}
.ͼ2k {font-weight: var(--font-weight-bold);}
.ͼ2l {text-decoration: line-through;}
.ͼ2m {font-family: var(--font-family-code);}
.ͼ2n {color: var(--foreground-dimmest);}
.ͼ2o {color: var(--accent-blue-strongest);}
.ͼ2p {color: var(--accent-blue-stronger);}
.ͼ2q {color: var(--accent-purple-stronger);}
.ͼ2r {color: var(--accent-pink-stronger);}
.ͼ2e.cm-focused {outline: 0 none;}
.ͼ2e {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ2e .cm-content {font-family: var(--font-family-code); padding-bottom: 0px;}
.ͼ2e .cm-line {line-height: var(--line-height-small);}
.ͼ2e .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ2e .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ2e .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ2e .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ2e.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ2e .cm-cursor, .ͼ2e .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ2e .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ2e .cm-activeLine {background-color: var(--background-higher);}
.ͼ2e .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ2e .cm-specialChar {color: var(--accent-negative-default);}
.ͼ2e .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ2e .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ2e .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ2e .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ2e .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ2e .cm-vim-panel input {color: var(--foreground-default);}
.ͼ2e .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ2e .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ2e .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ2e .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ2e .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ2e .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ2e .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ2e .cm-matchingBracket, .ͼ2e .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ2e .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ2e .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ2e .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ2e .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ2e .emmet-preview .cm-content {padding: 0 !important;}
.ͼ2e .emmet-preview .cm-scroller {z-index: 1;}
.ͼ2e .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ2e .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ2e .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ2e .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ2e .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ2e .cm-tooltip.multiplayer-tooltip, .ͼ2e .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ2e .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ2e .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ2e .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ2e .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ2e .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ2e .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ2e .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ2e .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ26 {color: var(--foreground-default);}
.ͼ27 {color: var(--outline-stronger);}
.ͼ28 {color: var(--accent-red-default);}
.ͼ29 {color: var(--accent-orange-stronger);}
.ͼ2a {color: var(--accent-yellow-stronger);}
.ͼ2b {color: var(--accent-lime-stronger);}
.ͼ2c {color: var(--accent-green-stronger);}
.ͼ2d {color: var(--accent-teal-stronger);}
.ͼ1y {color: var(--foreground-default);}
.ͼ1z {color: var(--accent-green-default);}
.ͼ20 {color: var(--accent-red-stronger);}
.ͼ21 {color: var(--accent-orange-strongest);}
.ͼ22 {color: var(--accent-yellow-strongest);}
.ͼ23 {color: var(--accent-lime-strongest);}
.ͼ24 {color: var(--accent-green-strongest);}
.ͼ25 {color: var(--accent-teal-strongest);}
.ͼ1l {text-decoration: underline;}
.ͼ1m {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼ1n {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼ1o {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼ1p {font-style: italic;}
.ͼ1q {font-weight: var(--font-weight-bold);}
.ͼ1r {text-decoration: line-through;}
.ͼ1s {font-family: var(--font-family-code);}
.ͼ1t {color: var(--foreground-dimmest);}
.ͼ1u {color: var(--accent-blue-strongest);}
.ͼ1v {color: var(--accent-blue-stronger);}
.ͼ1w {color: var(--accent-purple-stronger);}
.ͼ1x {color: var(--accent-pink-stronger);}
.ͼ1 .cm-diagnostic {padding: 3px 6px 3px 8px; margin-left: -1px; display: block; white-space: pre-wrap;}
.ͼ1 .cm-diagnostic-error {border-left: 5px solid #d11;}
.ͼ1 .cm-diagnostic-warning {border-left: 5px solid orange;}
.ͼ1 .cm-diagnostic-info {border-left: 5px solid #999;}
.ͼ1 .cm-diagnosticAction {font: inherit; border: none; padding: 2px 4px; background-color: #444; color: white; border-radius: 3px; margin-left: 8px;}
.ͼ1 .cm-diagnosticSource {font-size: 70%; opacity: 0.7;}
.ͼ1 .cm-lintRange {background-position: left bottom; background-repeat: repeat-x; padding-bottom: 0.7px;}
.ͼ1 .cm-lintRange-error {background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="6" height="3">%3Cpath%20d%3D%22m0%202.5%20l2%20-1.5%20l1%200%20l2%201.5%20l1%200%22%20stroke%3D%22%23d11%22%20fill%3D%22none%22%20stroke-width%3D%22.7%22%2F%3E</svg>');}
.ͼ1 .cm-lintRange-warning {background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="6" height="3">%3Cpath%20d%3D%22m0%202.5%20l2%20-1.5%20l1%200%20l2%201.5%20l1%200%22%20stroke%3D%22orange%22%20fill%3D%22none%22%20stroke-width%3D%22.7%22%2F%3E</svg>');}
.ͼ1 .cm-lintRange-info {background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="6" height="3">%3Cpath%20d%3D%22m0%202.5%20l2%20-1.5%20l1%200%20l2%201.5%20l1%200%22%20stroke%3D%22%23999%22%20fill%3D%22none%22%20stroke-width%3D%22.7%22%2F%3E</svg>');}
.ͼ1 .cm-lintRange-active {background-color: #ffdd9980;}
.ͼ1 .cm-tooltip-lint {padding: 0; margin: 0;}
.ͼ1 .cm-lintPoint:after {content: ""; position: absolute; bottom: 0; left: -2px; border-left: 3px solid transparent; border-right: 3px solid transparent; border-bottom: 4px solid #d11;}
.ͼ1 .cm-lintPoint {position: relative;}
.ͼ1 .cm-lintPoint-warning:after {border-bottom-color: orange;}
.ͼ1 .cm-lintPoint-info:after {border-bottom-color: #999;}
.ͼ1 .cm-panel.cm-panel-lint ul [aria-selected] u {text-decoration: underline;}
.ͼ1 .cm-panel.cm-panel-lint ul [aria-selected] {background-color: #ddd;}
.ͼ1 .cm-panel.cm-panel-lint ul:focus [aria-selected] {background: #bdf; background-color: Highlight; color: white; color: HighlightText;}
.ͼ1 .cm-panel.cm-panel-lint ul u {text-decoration: none;}
.ͼ1 .cm-panel.cm-panel-lint ul {max-height: 100px; overflow-y: auto; padding: 0; margin: 0;}
.ͼ1 .cm-panel.cm-panel-lint [name=close] {position: absolute; top: 0; right: 2px; background: inherit; border: none; font: inherit; padding: 0; margin: 0;}
.ͼ1 .cm-panel.cm-panel-lint {position: relative;}
.ͼ1 .explain-code-decoration {background: var(--accent-purple-dimmest);}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .cm-debuggerLine {background-color: var(--accent-primary-dimmest); border-radius: var(--border-radius-4); margin-right: var(--space-4);}
.ͼ1 .cm-breakpoint-gutter .cm-gutterElement {color: var(--accent-primary-default); padding-left: var(--space-4); padding-right: var(--space-2); cursor: default;}
.ͼ1 .replit-code-anchor {background: var(--accent-purple-dimmest);}
.ͼ1 .cm-foldPlaceholder {background-color: #eee; border: 1px solid #ddd; color: #888; border-radius: .2em; margin: 0 1px; padding: 0 1px; cursor: pointer;}
.ͼ1 .cm-foldGutter span {padding: 0 1px; cursor: pointer;}
.ͼ1 .cm-line {position: relative;}
.ͼ1 .cm-indentation-marker {display: inline-block;}
.ͼ2 .cm-indentation-marker {background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") left repeat-y;}
.ͼ3 .cm-indentation-marker {background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQImWNgYGBgYHB3d/8PAAOIAdULw8qMAAAAAElFTkSuQmCC) left repeat-y;}
.ͼ1 .cm-selectionMatch {background-color: #99ff7780;}
.ͼ1 .cm-searchMatch .cm-selectionMatch {background-color: transparent;}
.ͼ1 .cm-panel.cm-search [name=close] {position: absolute; top: 0; right: 4px; background-color: inherit; border: none; font: inherit; padding: 0; margin: 0;}
.ͼ1 .cm-panel.cm-search input, .ͼ1 .cm-panel.cm-search button, .ͼ1 .cm-panel.cm-search label {margin: .2em .6em .2em 0;}
.ͼ1 .cm-panel.cm-search input[type=checkbox] {margin-right: .2em;}
.ͼ1 .cm-panel.cm-search label {font-size: 80%; white-space: pre;}
.ͼ1 .cm-panel.cm-search {padding: 2px 6px 4px; position: relative;}
.ͼ2 .cm-searchMatch {background-color: #ffff0054;}
.ͼ3 .cm-searchMatch {background-color: #00ffff8a;}
.ͼ2 .cm-searchMatch-selected {background-color: #ff6a0054;}
.ͼ3 .cm-searchMatch-selected {background-color: #ff00ff8a;}
.ͼ1 .cm-tooltip.cm-tooltip-autocomplete > ul > li {overflow-x: hidden; text-overflow: ellipsis; cursor: pointer; padding: 1px 3px; line-height: 1.2;}
.ͼ1 .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: monospace; white-space: nowrap; overflow: hidden auto; max-width: 700px; max-width: min(700px, 95vw); min-width: 250px; max-height: 10em; list-style: none; margin: 0; padding: 0;}
.ͼ2 .cm-tooltip-autocomplete ul li[aria-selected] {background: #17c; color: white;}
.ͼ3 .cm-tooltip-autocomplete ul li[aria-selected] {background: #347; color: white;}
.ͼ1 .cm-completionListIncompleteTop:before, .ͼ1 .cm-completionListIncompleteBottom:after {content: "···"; opacity: 0.5; display: block; text-align: center;}
.ͼ1 .cm-tooltip.cm-completionInfo {position: absolute; padding: 3px 9px; width: max-content; max-width: 300px;}
.ͼ1 .cm-completionInfo.cm-completionInfo-left {right: 100%;}
.ͼ1 .cm-completionInfo.cm-completionInfo-right {left: 100%;}
.ͼ2 .cm-snippetField {background-color: #00000022;}
.ͼ3 .cm-snippetField {background-color: #ffffff22;}
.ͼ1 .cm-snippetFieldPosition {vertical-align: text-top; width: 0; height: 1.15em; margin: 0 -0.7px -.7em; border-left: 1.4px dotted #888;}
.ͼ1 .cm-completionMatchedText {text-decoration: underline;}
.ͼ1 .cm-completionDetail {margin-left: 0.5em; font-style: italic;}
.ͼ1 .cm-completionIcon {font-size: 90%; width: .8em; display: inline-block; text-align: center; padding-right: .6em; opacity: 0.6;}
.ͼ1 .cm-completionIcon-function:after, .ͼ1 .cm-completionIcon-method:after {content: 'ƒ';}
.ͼ1 .cm-completionIcon-class:after {content: '○';}
.ͼ1 .cm-completionIcon-interface:after {content: '◌';}
.ͼ1 .cm-completionIcon-variable:after {content: '𝑥';}
.ͼ1 .cm-completionIcon-constant:after {content: '𝐶';}
.ͼ1 .cm-completionIcon-type:after {content: '𝑡';}
.ͼ1 .cm-completionIcon-enum:after {content: '∪';}
.ͼ1 .cm-completionIcon-property:after {content: '□';}
.ͼ1 .cm-completionIcon-keyword:after {content: '🔑︎';}
.ͼ1 .cm-completionIcon-namespace:after {content: '▢';}
.ͼ1 .cm-completionIcon-text:after {content: 'abc'; font-size: 50%; vertical-align: middle;}
.ͼ1 .cm-tooltip {z-index: 100;}
.ͼ2 .cm-tooltip {border: 1px solid #bbb; background-color: #f5f5f5;}
.ͼ2 .cm-tooltip-section:not(:first-child) {border-top: 1px solid #bbb;}
.ͼ3 .cm-tooltip {background-color: #333338; color: white;}
.ͼ1 .cm-tooltip-arrow:before, .ͼ1 .cm-tooltip-arrow:after {content: ''; position: absolute; width: 0; height: 0; border-left: 7px solid transparent; border-right: 7px solid transparent;}
.ͼ1 .cm-tooltip-above .cm-tooltip-arrow:before {border-top: 7px solid #bbb;}
.ͼ1 .cm-tooltip-above .cm-tooltip-arrow:after {border-top: 7px solid #f5f5f5; bottom: 1px;}
.ͼ1 .cm-tooltip-above .cm-tooltip-arrow {bottom: -7px;}
.ͼ1 .cm-tooltip-below .cm-tooltip-arrow:before {border-bottom: 7px solid #bbb;}
.ͼ1 .cm-tooltip-below .cm-tooltip-arrow:after {border-bottom: 7px solid #f5f5f5; top: 1px;}
.ͼ1 .cm-tooltip-below .cm-tooltip-arrow {top: -7px;}
.ͼ1 .cm-tooltip-arrow {height: 7px; width: 14px; position: absolute; z-index: -1; overflow: hidden;}
.ͼ3 .cm-tooltip .cm-tooltip-arrow:before {border-top-color: #333338; border-bottom-color: #333338;}
.ͼ3 .cm-tooltip .cm-tooltip-arrow:after {border-top-color: transparent; border-bottom-color: transparent;}
.ͼ1.cm-focused .cm-matchingBracket {background-color: #328c8252;}
.ͼ1.cm-focused .cm-nonmatchingBracket {background-color: #bb555544;}
.ͼp .cm-interact {background: rgba(128, 128, 255, 0.2); border-radius: 4px;}
.ͼ28y .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼ28y .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼ28y .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼ28y .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼ283 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼ283 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼ283 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼ283 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼ278 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼ278 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼ278 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼ278 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼ23v .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼ23v .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼ23v .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼ23v .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼ230 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼ230 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼ230 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼ230 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼ1nz .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼ1nz .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼ1nz .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼ1nz .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼ1n4 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼ1n4 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼ1n4 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼ1n4 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼ1n3 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼ1n3 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼ1n3 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼ1n3 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼ1n2 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼ1n2 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼ1n2 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼ1n2 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼ1n1 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼ1n1 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼ1n1 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼ1n1 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼ1n0 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼ1n0 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼ1n0 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼ1n0 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼ1lb .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼ1lb .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼ1lb .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼ1lb .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼ1kg .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼ1kg .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼ1kg .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼ1kg .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼ1kf .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼ1kf .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼ1kf .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼ1kf .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼ1jk .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼ1jk .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼ1jk .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼ1jk .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼ1ip .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼ1ip .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼ1ip .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼ1ip .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼr6 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼr6 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼr6 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼr6 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼr5 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼr5 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼr5 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼr5 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼr4 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼr4 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼr4 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼr4 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼr3 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼr3 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼr3 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼr3 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼpe .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼpe .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼpe .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼpe .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼpd .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼpd .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼpd .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼpd .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼpc .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼpc .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼpc .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼpc .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼpb .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼpb .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼpb .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼpb .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼnm .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼnm .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼnm .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼnm .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼk9 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼk9 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼk9 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼk9 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼk8 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼk8 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼk8 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼk8 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼk7 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼk7 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼk7 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼk7 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼk6 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼk6 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼk6 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼk6 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼk5 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼk5 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼk5 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼk5 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼk4 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼk4 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼk4 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼk4 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼk3 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼk3 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼk3 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼk3 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼk2 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼk2 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼk2 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼk2 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼk1 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼk1 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼk1 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼk1 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼj6 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼj6 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼj6 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼj6 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼj5 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼj5 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼj5 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼj5 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼj4 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼj4 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼj4 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼj4 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼj3 .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼj3 .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼj3 .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼj3 .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼ1k .rendered-markdown .hover-tooltip-content p {font-size: calc(var(--font-size-default) + 1px); padding: var(--space-2) var(--space-8); line-height: 1.4; margin-bottom: 0;}
.ͼ1k .rendered-markdown .hover-tooltip-content p:last-child {margin-bottom: var(--space-4) !important;}
.ͼ1k .rendered-markdown .hover-tooltip-content pre {margin: var(--space-2) var(--space-8) var(--space-2) var(--space-4);}
.ͼ1k .rendered-markdown .hover-tooltip-content pre + p {border-top: 1px solid var(--outline-dimmest); padding-top: var(--space-4);}
.ͼ1j.cm-focused {outline: 0 none;}
.ͼ1j {background-color: var(--background-default); color: var(--foreground-default); font-size: 14px;}
.ͼ1j .cm-content {font-family: var(--font-family-code); padding-bottom: 400px;}
.ͼ1j .cm-line {line-height: var(--line-height-small);}
.ͼ1j .cm-scroller {overflow: auto; font-family: var(--font-family-code); font-size: 14px;}
.ͼ1j .cm-gutters {background-color: var(--background-default); color: var(--foreground-dimmest); border: none; min-width: fit-content; display: flex; justify-content: flex-end;}
.ͼ1j .cm-selectionBackground {background: var(--accent-primary-dimmest) !important;}
.ͼ1j .cm-selected {background: var(--accent-primary-dimmest) !important;}
.ͼ1j.cm-focused .cm-selectionBackgroundFocused {background: var(--accent-primary-dimmest);}
.ͼ1j .cm-cursor, .ͼ1j .cm-dropCursor {border-left-color: var(--accent-primary-default); border-left-width: 2px; border-radius: 2px;}
.ͼ1j .cm-cursorFocused {border-left-color: var(--accent-primary-default);}
.ͼ1j .cm-activeLine {background-color: var(--background-higher);}
.ͼ1j .cm-activeLineGutter {background-color: var(--background-higher);}
.ͼ1j .cm-specialChar {color: var(--accent-negative-default);}
.ͼ1j .cm-placeholder {color: var(--foreground-dimmer); display: inline-block;}
.ͼ1j .cm-textfield {border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); background-color: var(--background-default);}
.ͼ1j .cm-foldPlaceholder {padding: 0 var(--space-4); border-radius: var(--border-radius-4); background-color: var(--background-root); border: none; color: var(--foreground-dimmer);}
.ͼ1j .cm-panels {background-color: var(--background-overlay); font-size: var(--font-size-subhead-default); color: var(--foreground-default); z-index: 101;}
.ͼ1j .cm-panels-bottom {border-top: 2px solid var(--outline-dimmest);}
.ͼ1j .cm-vim-panel input {color: var(--foreground-default);}
.ͼ1j .cm-search {padding: var(--space-8) var(--space-8) var(--space-4) !important;}
.ͼ1j .cm-search .cm-textfield {margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1j .cm-search input {margin: 0 var(--space-4) 0 0; cursor: pointer;}
.ͼ1j .cm-search button {color: var(--foreground-default); cursor: pointer;}
.ͼ1j .cm-search .cm-button {background-image: none; background-color: var(--background-higher); margin: var(--space-2) var(--space-8) var(--space-2) 0 !important;}
.ͼ1j .cm-searchMatch {background-color: var(--accent-primary-dimmer);}
.ͼ1j .cm-searchMatch-selected {background-color: var(--accent-primary-default);}
.ͼ1j .cm-matchingBracket, .ͼ1j .cm-nonmatchingBracket {color: inherit; box-shadow: inset 0 0 0 1px var(--outline-default);}
.ͼ1j .replit-tooltip {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1j .emmet-preview {background-color: var(--background-default); color: var(--foreground-default); box-shadow: var(--shadow-1); border: 1px solid var(--outline-dimmest); border-radius: var(--border-radius-4); padding: var(--space-4);}
.ͼ1j .emmet-preview .cm-line {background-color: var(--background-default) !important;}
.ͼ1j .emmet-preview .cm-line::selection {background-color: var(--background-default) !important;}
.ͼ1j .emmet-preview .cm-content {padding: 0 !important;}
.ͼ1j .emmet-preview .cm-scroller {z-index: 1;}
.ͼ1j .cm-tooltip.multiplayer-tooltip {pointer-events: none;}
.ͼ1j .multiplayer-cursor {top: calc(100% - 1px); left: -1px; width: 2px; border-radius: var(--border-radius-4); pointer-events: none; position: absolute; color: transparent;}
.ͼ1j .cm-tooltip.multiplayer-tooltip .multiplayer-label {box-shadow: var(--shadow-1); padding: 1px; position: relative; left: -1px; border-radius: var(--border-radius-4); border-bottom-left-radius: 0px; animation: fadeOut 2s ease-in forwards;}
.ͼ1j .cm-completionInfo {white-space: pre-wrap; background-color: var(--background-higher); box-shadow: var(--shadow-1); border-radius: var(--border-radius-8); padding: var(--space-4) !important; border-color: transparent; z-index: -1; max-height: 70vh; max-width: min(300px, 30vw) !important; width: 100%; overflow: auto;}
.ͼ1j .cm-tooltip {box-shadow: var(--shadow-1); border-radius: var(--border-radius-4); border: 1px solid var(--outline-dimmest);}
.ͼ1j .cm-tooltip.multiplayer-tooltip, .ͼ1j .cm-generate-code-tooltip {background-color: transparent; box-shadow: none; border: 0 none; padding: 0px;}
.ͼ1j .cm-tooltip-lint {background-color: var(--background-higher);}
.ͼ1j .cm-tooltip-autocomplete > ul {background-color: var(--background-higher); border-radius: calc(var(--border-radius-4) - 1px); box-shadow: var(--shadow-default);}
.ͼ1j .cm-tooltip-autocomplete > ul > li:hover {background-color: var(--accent-primary-dimmest);}
.ͼ1j .cm-tooltip-autocomplete > ul > li[aria-selected] {background-color: var(--accent-primary-dimmer); color: var(--white);}
.ͼ1j .cm-tooltip.cm-tooltip-autocomplete > ul {font-family: var(--font-family-code);}
.ͼ1j .cm-tooltip.cm-tooltip-autocomplete > ul > li {padding-top: var(--space-4); padding-bottom: var(--space-4);}
.ͼ1j .cm-autocomplete-replit-icon {padding-inline: var(--space-4);}
@keyframes fadeOut {0% {opacity: 1;} 100% {opacity: 0;}}
.ͼ1j .cm-tooltip-autocomplete .cm-completionMatchedText {color: var(--accent-primary-stronger); text-decoration: unset;}
.ͼ1b {color: var(--foreground-default);}
.ͼ1c {color: var(--outline-stronger);}
.ͼ1d {color: var(--accent-red-default);}
.ͼ1e {color: var(--accent-orange-stronger);}
.ͼ1f {color: var(--accent-yellow-stronger);}
.ͼ1g {color: var(--accent-lime-stronger);}
.ͼ1h {color: var(--accent-green-stronger);}
.ͼ1i {color: var(--accent-teal-stronger);}
.ͼ13 {color: var(--foreground-default);}
.ͼ14 {color: var(--accent-green-default);}
.ͼ15 {color: var(--accent-red-stronger);}
.ͼ16 {color: var(--accent-orange-strongest);}
.ͼ17 {color: var(--accent-yellow-strongest);}
.ͼ18 {color: var(--accent-lime-strongest);}
.ͼ19 {color: var(--accent-green-strongest);}
.ͼ1a {color: var(--accent-teal-strongest);}
.ͼq {text-decoration: underline;}
.ͼr {font-weight: var(--font-weight-bold); font-size: 1.2em;}
.ͼs {font-weight: var(--font-weight-bold); font-size: 1.1em;}
.ͼt {font-weight: var(--font-weight-bold); font-size: 1.05;}
.ͼu {font-style: italic;}
.ͼv {font-weight: var(--font-weight-bold);}
.ͼw {text-decoration: line-through;}
.ͼx {font-family: var(--font-family-code);}
.ͼy {color: var(--foreground-dimmest);}
.ͼz {color: var(--accent-blue-strongest);}
.ͼ10 {color: var(--accent-blue-stronger);}
.ͼ11 {color: var(--accent-purple-stronger);}
.ͼ12 {color: var(--accent-pink-stronger);}
.ͼ4 .cm-line ::selection {background-color: transparent !important;}
.ͼ4 .cm-line::selection {background-color: transparent !important;}
.ͼ4 .cm-line {caret-color: transparent !important;}
</style><title>main.py - ыввы - Replit</title><link rel="shortcut icon" href="https://replit.com/public/icons/favicon-196.png" sizes="196x196" type="image/png"><meta property="og:type" content="article"><meta property="og:image" content="https://replit.com/public/icons/apple-icon-180.png"><meta property="og:site_name" content="replit"><meta property="fb:app_id" content="1775481339348651"><meta itemprop="name" content="replit"><meta itemprop="image" content="https://replit.com/public/icons/apple-icon-180.png"><meta name="keywords" content="IDE,Interpreter,Compiler,Teach,Host,Learn,Code,REPL,Compiler,Clojure,Haskell,Kotlin,QBasic,Forth,LOLCODE,BrainF,Emoticon,Bloop,Unlambda,CoffeeScript,Scheme,APL,Lua,Ruby,Roy,Python,Node.js,Deno (beta),Go,C++,C,C#,F#,HTML, CSS, JS,Rust,Swift,Python (with Turtle),Basic (beta),R,Bash,Crystal,Julia,Elixir,Nim,Dart,Reason Node.js,Tcl,Erlang,TypeScript,Pygame,Love2D,Emacs Lisp (Elisp),PHP Web Server,SQLite,Java,PHP CLI,Pyxel,Raku,Scala (beta),Nix (beta),Kaboom (beta)"><meta name="author" property="og:author" content="replit"><meta name="twitter:card" content="summary"><meta name="twitter:site" content="@replit"><meta name="twitter:image" content="https://replit.com/public/icons/apple-icon-180.png"><meta name="google" value="notranslate"><meta name="viewport" content="width=device-width, initial-scale=1"><style>

    /* PLEX SANS */

    /* ibm-plex-sans-regular - latin */
    @font-face {
      font-family: 'IBM Plex Sans';
      font-style: normal;
      font-weight: 400;
      src: local('IBM Plex Sans Regular'), local('IBMPlexSans-Regular'),
          url('/public/fonts/ibm-plex-sans-v8-latin-regular.woff2') format('woff2'), /* Chrome 26+, Opera 23+, Firefox 39+ */
          url('/public/fonts/ibm-plex-sans-v8-latin-regular.woff') format('woff'); /* Chrome 6+, Firefox 3.6+, IE 9+, Safari 5.1+ */
    }
    /* ibm-plex-sans-italic - latin */
    @font-face {
      font-family: 'IBM Plex Sans';
      font-style: italic;
      font-weight: 400;
      src: local('IBM Plex Sans Italic'), local('IBMPlexSans-Italic'),
          url('/public/fonts/ibm-plex-sans-v8-latin-italic.woff2') format('woff2'), /* Chrome 26+, Opera 23+, Firefox 39+ */
          url('/public/fonts/ibm-plex-sans-v8-latin-italic.woff') format('woff'); /* Chrome 6+, Firefox 3.6+, IE 9+, Safari 5.1+ */
    }
    /* ibm-plex-sans-500 - latin */
    @font-face {
      font-family: 'IBM Plex Sans';
      font-style: normal;
      font-weight: 500;
      src: local('IBM Plex Sans Medium'), local('IBMPlexSans-Medium'),
          url('/public/fonts/ibm-plex-sans-v8-latin-500.woff2') format('woff2'), /* Chrome 26+, Opera 23+, Firefox 39+ */
          url('/public/fonts/ibm-plex-sans-v8-latin-500.woff') format('woff'); /* Chrome 6+, Firefox 3.6+, IE 9+, Safari 5.1+ */
    }
    /* ibm-plex-sans-500italic - latin */
    @font-face {
      font-family: 'IBM Plex Sans';
      font-style: italic;
      font-weight: 500;
      src: local('IBM Plex Sans Medium Italic'), local('IBMPlexSans-Medium-Italic'),
          url('/public/fonts/ibm-plex-sans-v8-latin-500italic.woff2') format('woff2'), /* Chrome 26+, Opera 23+, Firefox 39+ */
          url('/public/fonts/ibm-plex-sans-v8-latin-500italic.woff') format('woff'); /* Chrome 6+, Firefox 3.6+, IE 9+, Safari 5.1+ */
    }
    /* ibm-plex-sans-600 - latin */
    @font-face {
      font-family: 'IBM Plex Sans';
      font-style: normal;
      font-weight: 600;
      src: local('IBM Plex Sans Semibold'), local('IBMPlexSans-Semibold'),
          url('/public/fonts/ibm-plex-sans-v8-latin-600.woff2') format('woff2'), /* Chrome 26+, Opera 23+, Firefox 39+ */
          url('/public/fonts/ibm-plex-sans-v8-latin-600.woff') format('woff'); /* Chrome 6+, Firefox 3.6+, IE 9+, Safari 5.1+ */
    }
    /* ibm-plex-sans-600italic - latin */
    @font-face {
      font-family: 'IBM Plex Sans';
      font-style: italic;
      font-weight: 600;
      src: local('IBM Plex Sans Semibold Italic'), local('IBMPlexSans-Semibold-Italic'),
          url('/public/fonts/ibm-plex-sans-v8-latin-600italic.woff2') format('woff2'), /* Chrome 26+, Opera 23+, Firefox 39+ */
          url('/public/fonts/ibm-plex-sans-v8-latin-600italic.woff') format('woff'); /* Chrome 6+, Firefox 3.6+, IE 9+, Safari 5.1+ */
    }

    /* PLEX MONO */

    /* ibm-plex-mono-regular - latin */
    @font-face {
      font-family: 'IBM Plex Mono';
      font-style: normal;
      font-weight: 400;
      src: local('IBM Plex Mono Regular'), local('IBMPlexMono-Regular'),
          url('/public/fonts/ibm-plex-mono-v6-latin-regular.woff2') format('woff2'), /* Chrome 26+, Opera 23+, Firefox 39+ */
          url('/public/fonts/ibm-plex-mono-v6-latin-regular.woff') format('woff'); /* Chrome 6+, Firefox 3.6+, IE 9+, Safari 5.1+ */
    }
    /* ibm-plex-mono-500 - latin */
    @font-face {
      font-family: 'IBM Plex Mono';
      font-style: normal;
      font-weight: 500;
       src: local('IBM Plex Mono Medium'), local('IBMPlexMono-Medium'),
          url('/public/fonts/ibm-plex-mono-v6-latin-500.woff2') format('woff2'), /* Chrome 26+, Opera 23+, Firefox 39+ */
          url('/public/fonts/ibm-plex-mono-v6-latin-500.woff') format('woff'); /* Chrome 6+, Firefox 3.6+, IE 9+, Safari 5.1+ */
    }
    /* ibm-plex-mono-italic - latin */
    @font-face {
      font-family: 'IBM Plex Mono';
      font-style: italic;
      font-weight: 400;
      src: local('IBM Plex Mono Italic'), local('IBMPlexMono-Italic'),
          url('/public/fonts/ibm-plex-mono-v6-latin-italic.woff2') format('woff2'), /* Chrome 26+, Opera 23+, Firefox 39+ */
          url('/public/fonts/ibm-plex-mono-v6-latin-italic.woff') format('woff'); /* Chrome 6+, Firefox 3.6+, IE 9+, Safari 5.1+ */
    }
    /* ibm-plex-mono-500italic - latin */
    @font-face {
      font-family: 'IBM Plex Mono';
      font-style: italic;
      font-weight: 500;
      src: local('IBM Plex Mono Medium Italic'), local('IBMPlexMono-Medium-Italic'),
          url('/public/fonts/ibm-plex-mono-v6-latin-500italic.woff2') format('woff2'), /* Chrome 26+, Opera 23+, Firefox 39+ */
          url('/public/fonts/ibm-plex-mono-v6-latin-500italic.woff') format('woff'); /* Chrome 6+, Firefox 3.6+, IE 9+, Safari 5.1+ */
    }
    /* ibm-plex-mono-600 - latin */
    @font-face {
      font-family: 'IBM Plex Mono';
      font-style: normal;
      font-weight: 600;
      src: local('IBM Plex Mono Semibold'), local('IBMPlexMono-Semibold'),
          url('/public/fonts/ibm-plex-mono-v6-latin-600.woff2') format('woff2'), /* Chrome 26+, Opera 23+, Firefox 39+ */
          url('/public/fonts/ibm-plex-mono-v6-latin-600.woff') format('woff'); /* Chrome 6+, Firefox 3.6+, IE 9+, Safari 5.1+ */
    }
    /* ibm-plex-mono-600italic - latin */
    @font-face {
      font-family: 'IBM Plex Mono';
      font-style: italic;
      font-weight: 600;
      src: local('IBM Plex Mono Semibold Italic'), local('IBMPlexMono-Semibold-Italic'),
          url('/public/fonts/ibm-plex-mono-v6-latin-600italic.woff2') format('woff2'), /* Chrome 26+, Opera 23+, Firefox 39+ */
          url('/public/fonts/ibm-plex-mono-v6-latin-600italic.woff') format('woff'); /* Chrome 6+, Firefox 3.6+, IE 9+, Safari 5.1+ */
    }

    
  </style><link rel="manifest" href="https://replit.com/public/manifest.json"><meta name="theme-color" content="#12141A"><meta http-equiv="origin-trial" content="AsKJNnBESA8LBSWSiA1TeHAuM7wj/zSm2MVlsxnG6yMeAuorNg9zyAEC3w+lp88yOz+9zkJmIQ++T1Cl4asHoAUAAABQeyJvcmlnaW4iOiJodHRwczovL3JlcGxpdC5jb206NDQzIiwiZmVhdHVyZSI6IkRpZ2l0YWxHb29kcyIsImV4cGlyeSI6MTYzMTY2Mzk5OX0="><link rel="apple-touch-icon" href="https://replit.com/public/icons/apple-icon-180.png"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-title" content="Replit"><link rel="search" type="application/opensearchdescription+xml" href="https://replit.com/public/opensearch.xml" title="Replit"><style>
        @font-face {
          font-family: 'ReplitHack';
          src: url('/public/fonts/hack-regular.woff2?sha=3114f1256') format('woff2'), url('/public/fonts/hack-regular.woff?sha=3114f1256') format('woff');
          font-weight: 400;
          font-style: normal;
        }
        
        @font-face {
          font-family: 'ReplitHack';
          src: url('/public/fonts/hack-bold.woff2?sha=3114f1256') format('woff2'), url('/public/fonts/hack-bold.woff?sha=3114f1256') format('woff');
          font-weight: 700;
          font-style: normal;
        }
        
        @font-face {
          font-family: 'ReplitHack';
          src: url('/public/fonts/hack-italic.woff2?sha=3114f1256') format('woff2'), url('/public/fonts/hack-italic.woff?sha=3114f1256') format('woff');
          font-weight: 400;
          font-style: italic;
        }
        
        @font-face {
          font-family: 'ReplitHack';
          src: url('/public/fonts/hack-bolditalic.woff2?sha=3114f1256') format('woff2'), url('/public/fonts/hack-bolditalic.woff?sha=3114f1256') format('woff');
          font-weight: 700;
          font-style: italic;
        }
        </style><meta property="og:title" content="ыввы"><meta property="og:description" content="A Nix (beta) repl"><meta itemprop="description" content="A Nix (beta) repl"><meta name="description" content="A Nix (beta) repl"><meta name="twitter:title" content="ыввы"><meta name="twitter:description" content="A Nix (beta) repl"><link rel="alternate" type="application/json+oembed" href="https://replit.com/data/oembed?url=https%3A%2F%2Freplit.com%2F%40l2darkness38%2Fyvvy" title="Replit - select language"><meta name="next-head-count" content="32"><script type="text/javascript" async="" src="./tren_files/js"></script><script type="text/javascript" async="" src="./tren_files/analytics.js"></script><script type="text/javascript" src="./tren_files/commons.54701049fd6fb8497e9e.js.gz" async="" status="loaded"></script><script type="text/javascript" src="./tren_files/google-analytics.dynamic.js.gz" async="" status="loaded"></script><script type="text/javascript" async="" src="./tren_files/sdk.min.js"></script><script type="text/javascript">/* Polyfill service v4.0.0
 * Disable minification (remove `.min` from URL path) for more info */

</script><script type="text/javascript">KNOWN_LANGUAGES = JSON.parse(atob('eyJjbG9qdXJlIjp7ImRpc3BsYXlOYW1lIjoiQ2xvanVyZSIsInRhZ2xpbmUiOiJBIG1vZGVybiBKVk0tYmFzZWQgTGlzcCBkaWFsZWN0IHdpdGggYSBmb2N1cyBvbiBpbW11dGFiaWxpdHkiLCJrZXkiOiJjbG9qdXJlIiwiZW50cnlwb2ludCI6Im1haW4uY2xqIiwiZXh0IjoiY2xqIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjp0cnVlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiQ2xvanVyZSAxLjguMFxuSmF2YSBIb3RTcG90KFRNKSA2NC1CaXQgU2VydmVyIFZNIDEuOC4wXzkxLWIxNCIsImNhdGVnb3J5IjoiUHJhY3RpY2FsIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9jbG9qdXJlLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwiaGFza2VsbCI6eyJkaXNwbGF5TmFtZSI6Ikhhc2tlbGwiLCJ0YWdsaW5lIjoiQW4gYWR2YW5jZWQsIHB1cmVseSBmdW5jdGlvbmFsIHByb2dyYW1taW5nIGxhbmd1YWdlIiwia2V5IjoiaGFza2VsbCIsImVudHJ5cG9pbnQiOiJtYWluLmhzIiwiZXh0IjoiaHMiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6dHJ1ZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IkdIQ2ksIHZlcnNpb24gOC42LjUiLCJjYXRlZ29yeSI6IlByYWN0aWNhbCIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvaGFza2VsbC5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImtvdGxpbiI6eyJkaXNwbGF5TmFtZSI6IktvdGxpbiIsInRhZ2xpbmUiOiJTdGF0aWNhbGx5IHR5cGVkIHByb2dyYW1taW5nIGxhbmd1YWdlIGludGVyb3BlcmFibGUgd2l0aCBKYXZhIGFuZCBBbmRyb2lkIiwia2V5Ijoia290bGluIiwiZW50cnlwb2ludCI6Im1haW4ua3QiLCJleHQiOiJrdCIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0IjpmYWxzZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJrb3RsaW5jLWp2bSAxLjMuNzIgKEpSRSAxMS4wLjgrMTAtcG9zdC1VYnVudHUtMHVidW50dTExOC4wNC4xKVxuXG5IaW50OiBydW4gXHUwMDFiWzMybWtvdGxpbmMtanZtXHUwMDFiWzBtIGZvciB0aGUgaW50ZXJhY3RpdmUgcmVwbCIsImNhdGVnb3J5IjoiUHJhY3RpY2FsIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9rb3RsaW4uc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJxYmFzaWMiOnsiZGlzcGxheU5hbWUiOiJRQmFzaWMiLCJ0YWdsaW5lIjoiU3RydWN0dXJlZCBwcm9ncmFtbWluZyBmb3IgYmVnaW5uZXJzLiIsImtleSI6InFiYXNpYyIsImVudHJ5cG9pbnQiOiJtYWluLmJhcyIsImV4dCI6ImJhcyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6ZmFsc2UsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJRQmFzaWMgKHFiLmpzKVxuQ29weXJpZ2h0IChjKSAyMDEwIFN0ZXZlIEhhbm92IiwiY2F0ZWdvcnkiOiJDbGFzc2ljIiwiaWNvbiI6Ii9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9sYW5ndWFnZS5zdmciLCJlbmdpbmUiOiJyZXBsYm94IiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwiZm9ydGgiOnsiZGlzcGxheU5hbWUiOiJGb3J0aCIsInRhZ2xpbmUiOiJBbiBpbnRlcmFjdGl2ZSBzdGFjay1vcmllbnRlZCBsYW5ndWFnZS4iLCJrZXkiOiJmb3J0aCIsImVudHJ5cG9pbnQiOiJtYWluLmZ0aCIsImV4dCI6ImZ0aCIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6ZmFsc2UsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJKUy1Gb3J0aCAwLjUyMDA4MDQxNzEzNDJcbmh0dHA6Ly93d3cuZm9ydGhmcmVhay5uZXQvanNmb3J0aC5odG1sXG5UaGlzIHByb2dyYW0gaXMgcHVibGlzaGVkIHVuZGVyIHRoZSBHUEwuIiwiY2F0ZWdvcnkiOiJDbGFzc2ljIiwiaWNvbiI6Ii9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9sYW5ndWFnZS5zdmciLCJlbmdpbmUiOiJyZXBsYm94IiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwibG9sY29kZSI6eyJkaXNwbGF5TmFtZSI6IkxPTENPREUiLCJ0YWdsaW5lIjoiVGhlIGJhc2ljIGxhbmd1YWdlIG9mIGxvbGNhdHMuIiwia2V5IjoibG9sY29kZSIsImVudHJ5cG9pbnQiOiJtYWluLmxvbCIsImV4dCI6ImxvbCIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6ZmFsc2UsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJMT0xDT0RFIHYxLjIgKGxvbC1jb2ZmZWUpXG5Db3B5cmlnaHQgKGMpIDIwMTEgTWF4IFNoYXdhYmtlaCIsImNhdGVnb3J5IjoiRXNvdGVyaWMiLCJpY29uIjoiL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2xvbGNvZGUuc3ZnIiwiZW5naW5lIjoicmVwbGJveCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImJyYWluZnVjayI6eyJkaXNwbGF5TmFtZSI6IkJyYWluRiIsInRhZ2xpbmUiOiJBIHB1cmUgVHVyaW5nIG1hY2hpbmUgY29udHJvbGxlci4iLCJrZXkiOiJicmFpbmZ1Y2siLCJlbnRyeXBvaW50IjoibWFpbi5iZiIsImV4dCI6ImJmIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IkJyYWluRioqKiwgYmZqc1xuQ29weXJpZ2h0IChjKSAyMDExIEFtamFkIE1hc2FkIiwiY2F0ZWdvcnkiOiJFc290ZXJpYyIsImljb24iOiIvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvYnJhaW5mdWNrLnN2ZyIsImVuZ2luZSI6InJlcGxib3giLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJlbW90aWNvbiI6eyJkaXNwbGF5TmFtZSI6IkVtb3RpY29uIiwidGFnbGluZSI6IlByb2dyYW1taW5nIHdpdGggYW4gZXh0cmEgZG9zZSBvZiBzbWlsZS4iLCJrZXkiOiJlbW90aWNvbiIsImVudHJ5cG9pbnQiOiJtYWluLmVtb3RpY29uIiwiZXh0IjoiZW1vdGljb24iLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOmZhbHNlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiRW1vdGljb24gdjEuNSAoZW1vdGljb2ZmZWUpXG5Db3B5cmlnaHQgKGMpIDIwMTEgQW1qYWQgTWFzYWQiLCJjYXRlZ29yeSI6IkVzb3RlcmljIiwiaWNvbiI6Ii9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9sYW5ndWFnZS5zdmciLCJlbmdpbmUiOiJyZXBsYm94IiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwiYmxvb3AiOnsiZGlzcGxheU5hbWUiOiJCbG9vcCIsInRhZ2xpbmUiOiJOb3RoaW5nIGJ1dCBib3VuZGVkIGxvb3BzLiIsImtleSI6ImJsb29wIiwiZW50cnlwb2ludCI6Im1haW4uYmxvb3AiLCJleHQiOiJibG9vcCIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6ZmFsc2UsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJCbG9vUGpzXG5Db3B5cmlnaHQgKGMpIDIwMDUgVGltIENhbWVyb24gUnlhblxuQmFzZWQgb24gUGVybCBjb2RlIGJ5IEpvaG4gQ293YW4sIDE5OTQiLCJjYXRlZ29yeSI6IkVzb3RlcmljIiwiaWNvbiI6Ii9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9sYW5ndWFnZS5zdmciLCJlbmdpbmUiOiJyZXBsYm94IiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwicmVhY3RfbmF0aXZlIjp7ImRpc3BsYXlOYW1lIjoiUmVhY3QgTmF0aXZlIiwidGFnbGluZSI6IkNyZWF0ZSBtb2JpbGUgYXBwcyB3aXRoIFJlYWN0IE5hdGl2ZSBhbmQgRXhwbyIsImtleSI6InJlYWN0X25hdGl2ZSIsImVudHJ5cG9pbnQiOiJpbmRleC5qcyIsImV4dCI6ImpzIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6dHJ1ZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6ZmFsc2UsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiUmVhY3QgTmF0aXZlIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL3JlYWN0LnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwidW5sYW1iZGEiOnsiZGlzcGxheU5hbWUiOiJVbmxhbWJkYSIsInRhZ2xpbmUiOiJGdW5jdGlvbmFsIHB1cml0eSBnaXZlbiBmb3JtLiIsImtleSI6InVubGFtYmRhIiwiZW50cnlwb2ludCI6Im1haW4udW5sIiwiZXh0IjoidW5sIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IlVubGFtYmRhIHYyLjAgKHVubGFtYmRhLWNvZmZlZSlcbkNvcHlyaWdodCAoYykgMjAxMSBNYXggU2hhd2Fia2VoIiwiY2F0ZWdvcnkiOiJFc290ZXJpYyIsImljb24iOiIvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvbGFuZ3VhZ2Uuc3ZnIiwiZW5naW5lIjoicmVwbGJveCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImphdmFzY3JpcHQiOnsiZGlzcGxheU5hbWUiOiJKYXZhU2NyaXB0IiwidGFnbGluZSI6IlRoZSBkZSBmYWN0byBsYW5ndWFnZSBvZiB0aGUgV2ViLiIsImtleSI6ImphdmFzY3JpcHQiLCJlbnRyeXBvaW50IjoibWFpbi5qcyIsImV4dCI6ImpzIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6Ik5hdGl2ZSBCcm93c2VyIEphdmFTY3JpcHQiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiIvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvamF2YXNjcmlwdC5zdmciLCJlbmdpbmUiOiJyZXBsYm94IiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwiYmFiZWwiOnsiZGlzcGxheU5hbWUiOiJFUzYiLCJ0YWdsaW5lIjoiTmV4dCBnZW5lcmF0aW9uIEphdmFTY3JpcHQuIiwia2V5IjoiYmFiZWwiLCJlbnRyeXBvaW50IjoibWFpbi5qcyIsImV4dCI6ImpzIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IkJhYmVsIENvbXBpbGVyIHY2LjQuNFxuQ29weXJpZ2h0IChjKSAyMDE0LTIwMTUgU2ViYXN0aWFuIE1jS2VuemllIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2phdmFzY3JpcHQuc3ZnIiwiZW5naW5lIjoicmVwbGJveCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImNvZmZlZXNjcmlwdCI6eyJkaXNwbGF5TmFtZSI6IkNvZmZlZVNjcmlwdCIsInRhZ2xpbmUiOiJVbmZhbmN5IEphdmFTY3JpcHQuIiwia2V5IjoiY29mZmVlc2NyaXB0IiwiZW50cnlwb2ludCI6Im1haW4uY29mZmVlIiwiZXh0IjoiY29mZmVlIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IkNvZmZlZVNjcmlwdCB2MS4xMFxuQ29weXJpZ2h0IChjKSAyMDE2LCBKZXJlbXkgQXNoa2VuYXMiLCJjYXRlZ29yeSI6IldlYiIsImljb24iOiIvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvY29mZmVlc2NyaXB0LnN2ZyIsImVuZ2luZSI6InJlcGxib3giLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJzY2hlbWUiOnsiZGlzcGxheU5hbWUiOiJTY2hlbWUiLCJ0YWdsaW5lIjoiQW4gZWxlZ2FudCBkeW5hbWljIGRpYWxlY3Qgb2YgTGlzcC4iLCJrZXkiOiJzY2hlbWUiLCJlbnRyeXBvaW50IjoibWFpbi5zY20iLCJleHQiOiJzY20iLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOmZhbHNlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiQml3YVNjaGVtZSBJbnRlcnByZXRlciB2ZXJzaW9uIDAuNi40XG5Db3B5cmlnaHQgKEMpIDIwMDctMjAxNCBZdXRha2EgSEFSQSBhbmQgdGhlIEJpd2FTY2hlbWUgdGVhbSIsImNhdGVnb3J5IjoiUHJhY3RpY2FsIiwiaWNvbiI6Ii9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9zY2hlbWUuc3ZnIiwiZW5naW5lIjoicmVwbGJveCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImFwbCI6eyJkaXNwbGF5TmFtZSI6IkFQTCIsInRhZ2xpbmUiOiJBbiBhcnJheS1vcmllbnRlZCBsYW5ndWFnZSB1c2luZyBmdW5ueSBjaGFyYWN0ZXJzLiIsImtleSI6ImFwbCIsImVudHJ5cG9pbnQiOiJtYWluLmFwbCIsImV4dCI6ImFwbCIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6ZmFsc2UsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJuZ24vYXBsIiwiY2F0ZWdvcnkiOiJDbGFzc2ljIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9sYW5ndWFnZS5zdmciLCJlbmdpbmUiOiJyZXBsYm94IiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwibHVhIjp7ImRpc3BsYXlOYW1lIjoiTHVhIiwidGFnbGluZSI6IkEgbGlnaHR3ZWlnaHQgbXVsdGktcGFyYWRpZ20gc2NyaXB0aW5nIGxhbmd1YWdlLiIsImtleSI6Imx1YSIsImVudHJ5cG9pbnQiOiJtYWluLmx1YSIsImV4dCI6Imx1YSIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6dHJ1ZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJMdWEgNS4xLjUiLCJjYXRlZ29yeSI6IlByYWN0aWNhbCIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvbHVhLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwicHl0aG9uIjp7ImRpc3BsYXlOYW1lIjoiUHl0aG9uIDIuNyIsInRhZ2xpbmUiOiJBIGR5bmFtaWMgbGFuZ3VhZ2UgZW1waGFzaXppbmcgcmVhZGFiaWxpdHkuIiwia2V5IjoicHl0aG9uIiwiZW50cnlwb2ludCI6Im1haW4ucHkiLCJleHQiOiJweSIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOnRydWUsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6dHJ1ZSwiaGFzVVBNIjp0cnVlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOnRydWUsImhhc0ludGVycHJldGVyIjp0cnVlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiUHl0aG9uIDIuNy4xNiAoZGVmYXVsdCwgSnVsIDEzIDIwMTksIDE2OjAxOjUxKVxuW0dDQyA4LjMuMF0gb24gbGludXgyIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL3B5dGhvbi5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInJ1YnkiOnsiZGlzcGxheU5hbWUiOiJSdWJ5IiwidGFnbGluZSI6IkEgbmF0dXJhbCBkeW5hbWljIG9iamVjdC1vcmllbnRlZCBsYW5ndWFnZS4iLCJrZXkiOiJydWJ5IiwiZW50cnlwb2ludCI6Im1haW4ucmIiLCJleHQiOiJyYiIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOnRydWUsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6InJ1YnkgMi41LjVwMTU3ICgyMDE5LTAzLTE1IHJldmlzaW9uIDY3MjYwKSBbeDg2XzY0LWxpbnV4XVxuXG5IaW50OiBydW4gXHUwMDFiWzMybWlyYlx1MDAxYlswbSBmb3IgdGhlIGludGVyYWN0aXZlIHJlcGwiLCJjYXRlZ29yeSI6IlByYWN0aWNhbCIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvcnVieS5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInJveSI6eyJkaXNwbGF5TmFtZSI6IlJveSIsInRhZ2xpbmUiOiJTbWFsbCBmdW5jdGlvbmFsIGxhbmd1YWdlIHRoYXQgY29tcGlsZXMgdG8gSmF2YVNjcmlwdC4iLCJrZXkiOiJyb3kiLCJlbnRyeXBvaW50IjoibWFpbi5yb3kiLCJleHQiOiJyb3kiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOmZhbHNlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiUm95IDAuMS4zXG5Db3B5cmlnaHQgKEMpIDIwMTEgQnJpYW4gTWNLZW5uYSIsImNhdGVnb3J5IjoiV2ViIiwiaWNvbiI6Ii9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9yb3kuc3ZnIiwiZW5naW5lIjoicmVwbGJveCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInBocCI6eyJkaXNwbGF5TmFtZSI6IlBIUCAoTGVnYWN5KSIsInRhZ2xpbmUiOiJBIHBvcHVsYXIgZ2VuZXJhbC1wdXJwb3NlIHNjcmlwdGluZyBsYW5ndWFnZS4iLCJrZXkiOiJwaHAiLCJlbnRyeXBvaW50IjoibWFpbi5waHAiLCJleHQiOiJwaHAiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOmZhbHNlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOnRydWUsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJQSFAgNy4wLjggKExlZ2FjeTogdXNlIHRoZSBmb2xsb3dpbmcgZm9yIG5ldyBmZWF0dXJlczpcbkNvbW1hbmQtbGluZSBQSFA6IGh0dHBzOi8vcmVwbGl0LmNvbS9sYW5ndWFnZXMvcGhwX2NsaVxuUEhQIFdlYiBTZXJ2ZXI6IGh0dHBzOi8vcmVwbGl0LmNvbS9sYW5ndWFnZXMvcGhwNyIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9waHAuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJweXRob24zIjp7ImRpc3BsYXlOYW1lIjoiUHl0aG9uIiwidGFnbGluZSI6IkEgZHluYW1pYyBsYW5ndWFnZSBlbXBoYXNpemluZyByZWFkYWJpbGl0eS4iLCJrZXkiOiJweXRob24zIiwiZW50cnlwb2ludCI6Im1haW4ucHkiLCJleHQiOiJweSIsImhhc0xpbnQiOnRydWUsImhhc1VuaXRUZXN0cyI6dHJ1ZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjp0cnVlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOnRydWUsImhhc0ludGVycHJldGVyIjp0cnVlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGFzREFQIjp0cnVlLCJoZWFkZXIiOiJQeXRob24gMy44LjIgKGRlZmF1bHQsIEZlYiAyNiAyMDIwLCAwMjo1NjoxMCkiLCJjYXRlZ29yeSI6IlByYWN0aWNhbCIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvcHl0aG9uLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwibm9kZWpzIjp7ImRpc3BsYXlOYW1lIjoiTm9kZS5qcyIsInRhZ2xpbmUiOiJFdmVudGVkIEkvTyBmb3IgVjggSmF2YVNjcmlwdC4iLCJrZXkiOiJub2RlanMiLCJlbnRyeXBvaW50IjoiaW5kZXguanMiLCJleHQiOiJqcyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOnRydWUsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6dHJ1ZSwiaGFzVVBNIjp0cnVlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOnRydWUsImhhc0ludGVycHJldGVyIjp0cnVlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGFzREFQIjp0cnVlLCJoZWFkZXIiOiJub2RlIHYxMi4xNi4xIiwiY2F0ZWdvcnkiOiJQcmFjdGljYWwiLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL25vZGVqcy5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfSwiYWxpYXNlcyI6W3siZGlzcGxheU5hbWUiOiJKYXZhU2NyaXB0IiwidGFnbGluZSI6IlRoZSBkZSBmYWN0byBsYW5ndWFnZSBvZiB0aGUgV2ViLiIsImljb24iOiIvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvamF2YXNjcmlwdC5zdmciLCJjYXRlZ29yeSI6IldlYiJ9XX0sImRlbm8iOnsiZGlzcGxheU5hbWUiOiJEZW5vIChiZXRhKSIsInRhZ2xpbmUiOiJBIHNlY3VyZSBydW50aW1lIGZvciBKYXZhU2NyaXB0IGFuZCBUeXBlU2NyaXB0Iiwia2V5IjoiZGVubyIsImVudHJ5cG9pbnQiOiJpbmRleC50cyIsImV4dCI6InRzIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IkRlbm8gMS43LjBcblxuSGludDogcnVuIFx1MDAxYlszMm1kZW5vXHUwMDFiWzBtIGZvciB0aGUgaW50ZXJhY3RpdmUgcmVwbCIsImNhdGVnb3J5IjoiUHJhY3RpY2FsIiwiaWNvbiI6Imh0dHBzOi8vaWNvbnMudXRpbC5yZXBsLmNvL2Rlbm8tbm8tdHJhbnNwYXJlbnQuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6dHJ1ZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImVuenltZSI6eyJkaXNwbGF5TmFtZSI6IkVuenltZSIsInRhZ2xpbmUiOiJBIEphdmFTY3JpcHQgVGVzdGluZyB1dGlsaXR5IGZvciBSZWFjdCIsImtleSI6ImVuenltZSIsImVudHJ5cG9pbnQiOiJpbmRleC5qcyIsImV4dCI6ImpzIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0IjpmYWxzZSwiaGFzRXZhbCI6dHJ1ZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6Im5vZGUgdjcuNCBsaW51eC9hbWQ2NCIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9yZWFjdC5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImdvIjp7ImRpc3BsYXlOYW1lIjoiR28iLCJ0YWdsaW5lIjoiU3RhdGljYWxseSB0eXBlZCB5ZXQgZXhwcmVzc2l2ZSBsYW5ndWFnZSB3aXRoIGEgZm9jdXMgb24gY29uY3VycmVuY3kuIiwia2V5IjoiZ28iLCJlbnRyeXBvaW50IjoibWFpbi5nbyIsImV4dCI6ImdvIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6ImdvIHZlcnNpb24gZ28xLjE0IGxpbnV4L2FtZDY0IiwiY2F0ZWdvcnkiOiJQcmFjdGljYWwiLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2dvLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwiamF2YSI6eyJkaXNwbGF5TmFtZSI6IkphdmEiLCJ0YWdsaW5lIjoiQSBjb25jdXJyZW50LCBjbGFzcy1iYXNlZCwgc3RhdGljYWxseSB0eXBlZCBvYmplY3Qtb3JpZW50ZWQgbGFuZ3VhZ2UuIiwia2V5IjoiamF2YSIsImVudHJ5cG9pbnQiOiJNYWluLmphdmEiLCJleHQiOiJqYXZhIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6dHJ1ZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6ZmFsc2UsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJqYXZhIHZlcnNpb24gXCIxLjguMF8zMVwiXG5KYXZhKFRNKSBTRSBSdW50aW1lIEVudmlyb25tZW50IChidWlsZCAxLjguMF8zMS1iMTMpXG5KYXZhIEhvdFNwb3QoVE0pIDY0LUJpdCBTZXJ2ZXIgVk0gKGJ1aWxkIDI1LjMxLWIwNywgbWl4ZWQgbW9kZSkiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvamF2YS5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImNwcCI6eyJkaXNwbGF5TmFtZSI6IkMrKyIsInRhZ2xpbmUiOiJBIGdlbmVyYWwgcHVycG9zZSBzeXN0ZW0gcHJvZ3JhbW1pbmcgbGFuZ3VhZ2UuIiwia2V5IjoiY3BwIiwiZW50cnlwb2ludCI6Im1haW4uY3BwIiwiZXh0IjoiY3BwIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhhc0RBUCI6dHJ1ZSwiaGVhZGVyIjoiY2xhbmcgdmVyc2lvbiA3LjAuMC0zfnVidW50dTAuMTguMDQuMSAodGFncy9SRUxFQVNFXzcwMC9maW5hbCkiLCJjYXRlZ29yeSI6IlByYWN0aWNhbCIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvY3BwLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwiY3BwMTEiOnsiZGlzcGxheU5hbWUiOiJDKysxMSIsInRhZ2xpbmUiOiJBIGdlbmVyYWwgcHVycG9zZSBzeXN0ZW0gcHJvZ3JhbW1pbmcgbGFuZ3VhZ2UuIiwia2V5IjoiY3BwMTEiLCJlbnRyeXBvaW50IjoibWFpbi5jcHAiLCJleHQiOiJjcHAiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiY2xhbmcgdmVyc2lvbiA3LjAuMC0zfnVidW50dTAuMTguMDQuMSAodGFncy9SRUxFQVNFXzcwMC9maW5hbCkiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvY3BwLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwiYyI6eyJkaXNwbGF5TmFtZSI6IkMiLCJ0YWdsaW5lIjoiTG93LWxldmVsIGFuZCBjcm9zcy1wbGF0Zm9ybSBpbXBlcmF0aXZlIGxhbmd1YWdlLiIsImtleSI6ImMiLCJlbnRyeXBvaW50IjoibWFpbi5jIiwiZXh0IjoiYyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOnRydWUsImhlYWRlciI6ImNsYW5nIHZlcnNpb24gNy4wLjAtM351YnVudHUwLjE4LjA0LjEgKHRhZ3MvUkVMRUFTRV83MDAvZmluYWwpIiwiY2F0ZWdvcnkiOiJQcmFjdGljYWwiLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2Muc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJjc2hhcnAiOnsiZGlzcGxheU5hbWUiOiJDIyIsInRhZ2xpbmUiOiJBIE1pY3Jvc29mdCAuTkVUIHByb2dyYW1taW5nIGxhbmd1YWdlLiIsImtleSI6ImNzaGFycCIsImVudHJ5cG9pbnQiOiJtYWluLmNzIiwiZXh0IjoiY3MiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJNb25vIEMjIGNvbXBpbGVyIHZlcnNpb24gNi44LjAuMTIzIiwiY2F0ZWdvcnkiOiJQcmFjdGljYWwiLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2NzaGFycC5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImZzaGFycCI6eyJkaXNwbGF5TmFtZSI6IkYjIiwidGFnbGluZSI6IkEgTWljcm9zb2Z0IC5ORVQgZnVuY3Rpb25hbCBwcm9ncmFtbWluZyBsYW5ndWFnZS4iLCJrZXkiOiJmc2hhcnAiLCJlbnRyeXBvaW50IjoibWFpbi5mcyIsImV4dCI6ImZzIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiRiMgQ29tcGlsZXIgZm9yIEYjIDQuNSAoT3BlbiBTb3VyY2UgRWRpdGlvbikiLCJjYXRlZ29yeSI6IlByYWN0aWNhbCIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvZnNoYXJwLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwid2ViX3Byb2plY3QiOnsiZGlzcGxheU5hbWUiOiJIVE1MLCBDU1MsIEpTIiwidGFnbGluZSI6IlRoZSBsYW5ndWFnZXMgdGhhdCBtYWtlIHVwIHRoZSB3ZWIuIiwia2V5Ijoid2ViX3Byb2plY3QiLCJlbnRyeXBvaW50IjoibWFpbi5odG1sIiwiZXh0IjoiaHRtbCIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6ZmFsc2UsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiIvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvd2ViX3Byb2plY3Quc3ZnIiwiZW5naW5lIjoicmVwbGJveCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImh0bWwiOnsiZGlzcGxheU5hbWUiOiJIVE1MLCBDU1MsIEpTIiwidGFnbGluZSI6IlRoZSBsYW5ndWFnZXMgdGhhdCBtYWtlIHVwIHRoZSB3ZWIuIiwia2V5IjoiaHRtbCIsImVudHJ5cG9pbnQiOiJpbmRleC5odG1sIiwiZXh0IjoiaHRtbCIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6ZmFsc2UsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJjYXRlZ29yeSI6IldlYiIsImljb24iOiIvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvd2ViX3Byb2plY3Quc3ZnIiwiZW5naW5lIjoicmVwbGJveCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInJ1c3QiOnsiZGlzcGxheU5hbWUiOiJSdXN0IiwidGFnbGluZSI6IkEgZmFzdCBhbmQgc2FmZSBzeXN0ZW1zIHByb2dyYW1taW5nIGxhbmd1YWdlLiIsImtleSI6InJ1c3QiLCJlbnRyeXBvaW50IjoibWFpbi5ycyIsImV4dCI6InJzIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoicnVzdGMgMS40NC4wICg0OWNhZTU1NzYgMjAyMC0wNi0wMSkiLCJjYXRlZ29yeSI6IlByYWN0aWNhbCIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvcnVzdC5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInN3aWZ0Ijp7ImRpc3BsYXlOYW1lIjoiU3dpZnQiLCJ0YWdsaW5lIjoiQSBtb2Rlcm4gZ2VuZXJhbC1wdXJwb3NlIHByb2dyYW1taW5nIGxhbmd1YWdlIGZyb20gQXBwbGUuIiwia2V5Ijoic3dpZnQiLCJlbnRyeXBvaW50IjoibWFpbi5zd2lmdCIsImV4dCI6InN3aWZ0IiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiU3dpZnQgdmVyc2lvbiA1LjAuMSAoc3dpZnQtNS4wLjEtUkVMRUFTRSkiLCJjYXRlZ29yeSI6IlByYWN0aWNhbCIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvc3dpZnQuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJweXRob25fdHVydGxlIjp7ImRpc3BsYXlOYW1lIjoiUHl0aG9uICh3aXRoIFR1cnRsZSkiLCJ0YWdsaW5lIjoiQSBzaW1wbGUgdmVyc2lvbiBvZiBQeXRob24gdGhhdCBzdXBwb3J0cyBUdXJ0bGUuIiwia2V5IjoicHl0aG9uX3R1cnRsZSIsImVudHJ5cG9pbnQiOiJtYWluLnB5IiwiZXh0IjoicHkiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOmZhbHNlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiY2F0ZWdvcnkiOiJQcmF0aWNhbCIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvcHl0aG9uX3R1cnRsZS5zdmciLCJlbmdpbmUiOiJyZXBsYm94IiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwiYmFzaWMiOnsiZGlzcGxheU5hbWUiOiJCYXNpYyAoYmV0YSkiLCJ0YWdsaW5lIjoiQSBmdW4gYW5kIHNpbXBsZSBwcm9ncmFtbWluZyBsYW5ndWFnZSBmb3IgYmVnaW5uZXJzIiwia2V5IjoiYmFzaWMiLCJlbnRyeXBvaW50IjoicHJvZ3JhbS5iYXMiLCJleHQiOiJiYXMiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOmZhbHNlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoicGctYmFzaWMgdjAuMSBcbihjKSAyMDIwIEFtamFkICYgRmFyaXMgTWFzYWQiLCJjYXRlZ29yeSI6IkNsYXNzaWMiLCJpY29uIjoiaHR0cHM6Ly9pY29ucy0tdXRpbC5yZXBsLmNvL2Jhc2ljLnN2ZyIsImRvY3MiOiJodHRwczovL2RvY3MucmVwbGl0LmNvbS9taXNjL2Jhc2ljIiwiZW5naW5lIjoicmVwbGJveCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImplc3QiOnsiZGlzcGxheU5hbWUiOiJKZXN0IiwidGFnbGluZSI6IlBhaW5sZXNzIEphdmFTY3JpcHQgVGVzdGluZy4iLCJrZXkiOiJqZXN0IiwiZW50cnlwb2ludCI6ImNvbmZpZy5qc29uIiwiZXh0IjoianMiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6ZmFsc2UsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiSmVzdCB2MjQuOS4wIG5vZGUgdjEwLjE2LjMgbGludXgvYW1kNjQiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvamVzdC5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImRqYW5nbyI6eyJkaXNwbGF5TmFtZSI6IkRqYW5nbyIsInRhZ2xpbmUiOiJQeXRob24gZnJhbWV3b3JrIHRoYXQgZW5jb3VyYWdlcyByYXBpZCBkZXZlbG9wbWVudC4iLCJrZXkiOiJkamFuZ28iLCJlbnRyeXBvaW50IjoibWFpbi92aWV3cy5weSIsImV4dCI6InB5IiwiaGFzTGludCI6dHJ1ZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjp0cnVlLCJoYXNVUE0iOnRydWUsImhhc0dpdCI6ZmFsc2UsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJQeXRob24gMy42LjEgKGRlZmF1bHQsIEp1biAyMSAyMDE3LCAxODo0ODozNSlcbltHQ0MgNC45LjJdIG9uIGxpbnV4IiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2RqYW5nby5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImV4cHJlc3MiOnsiZGlzcGxheU5hbWUiOiJFeHByZXNzIiwidGFnbGluZSI6IkphdmFTY3JpcHQgZnJhbWV3b3JrIGRlc2lnbmVkIGZvciBidWlsZGluZyB3ZWIgYXBwbGljYXRpb25zIGFuZCBBUElzLiIsImtleSI6ImV4cHJlc3MiLCJlbnRyeXBvaW50IjoiaW5kZXguanMiLCJleHQiOiJqcyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOnRydWUsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6dHJ1ZSwiaGFzVVBNIjp0cnVlLCJoYXNHaXQiOmZhbHNlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6Im5vZGUgdjkuNy4xIGxpbnV4L2FtZDY0IiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2V4cHJlc3Muc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJzaW5hdHJhIjp7ImRpc3BsYXlOYW1lIjoiU2luYXRyYSIsInRhZ2xpbmUiOiJEU0wgZm9yIHF1aWNrbHkgY3JlYXRpbmcgd2ViIGFwcGxpY2F0aW9ucyBpbiBSdWJ5IHdpdGggbWluaW1hbCBlZmZvcnQiLCJrZXkiOiJzaW5hdHJhIiwiZW50cnlwb2ludCI6Im1haW4ucmIiLCJleHQiOiJyYiIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOnRydWUsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6dHJ1ZSwiaGFzVVBNIjp0cnVlLCJoYXNHaXQiOmZhbHNlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6InJ1YnkgMi41LjBwMCAoMjAxNy0xMi0yNSByZXZpc2lvbiA2MTQ2OCkgW3g4Nl82NC1saW51eF0iLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvc2luYXRyYS5wbmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInJhaWxzIjp7ImRpc3BsYXlOYW1lIjoiUnVieSBvbiBSYWlscyIsInRhZ2xpbmUiOiJBIHdlYi1hcHBsaWNhdGlvbiBmcmFtZXdvcmsgdGhhdCBpbmNsdWRlcyBldmVyeXRoaW5nIG5lZWRlZCB0byBjcmVhdGUgd2ViIGFwcGxpY2F0aW9ucyIsImtleSI6InJhaWxzIiwiZW50cnlwb2ludCI6ImNvbmZpZy9yb3V0ZXMucmIiLCJleHQiOiJyYiIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOnRydWUsImhhc1VQTSI6dHJ1ZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6InJ1YnkgMi41LjBwMCAoMjAxNy0xMi0yNSByZXZpc2lvbiA2MTQ2OCkgW3g4Nl82NC1saW51eF0iLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvcmFpbHMuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJybGFuZyI6eyJkaXNwbGF5TmFtZSI6IlIiLCJ0YWdsaW5lIjoiQSBwcm9ncmFtbWluZyBsYW5ndWFnZSBhbmQgZW52aXJvbm1lbnQgZm9yIHN0YXRpc3RpY2FsIGNvbXB1dGluZyBhbmQgZ3JhcGhpY3MiLCJrZXkiOiJybGFuZyIsImVudHJ5cG9pbnQiOiJtYWluLnIiLCJleHQiOiJyIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoidXNpbmcgR05VIFIgVmVyc2lvbiAzLjUuMCAoMjAxOC0wNC0yMykiLCJjYXRlZ29yeSI6IlByYWN0aWNhbCIsImljb24iOiJodHRwczovL2xvZ29zLnR1cmJpby5yZXBsLmNvL3JsYW5nLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwibmV4dGpzIjp7ImRpc3BsYXlOYW1lIjoiTmV4dC5qcyIsInRhZ2xpbmUiOiJBIGxpZ2h0d2VpZ2h0IGZyYW1ld29yayBmb3Igc3RhdGljIGFuZCBzZXJ2ZXJcdTIwMTFyZW5kZXJlZCBSZWFjdCBhcHBsaWNhdGlvbnMiLCJrZXkiOiJuZXh0anMiLCJlbnRyeXBvaW50IjoicGFnZXMvaW5kZXguanMiLCJleHQiOiJqcyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOnRydWUsImhhc1VQTSI6dHJ1ZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiTmV4dC5qcyA2LjAuMywgbm9kZSB2MTIuMTMuMCBsaW51eC9hbWQ2NCIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9ub2RlanMuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJnYXRzYnlqcyI6eyJkaXNwbGF5TmFtZSI6IkdhdHNieUpTIiwidGFnbGluZSI6IkJsYXppbmctZmFzdCBzdGF0aWMgc2l0ZSBnZW5lcmF0b3IgZm9yIFJlYWN0Iiwia2V5IjoiZ2F0c2J5anMiLCJlbnRyeXBvaW50Ijoic3JjL3BhZ2VzL2luZGV4LmpzIiwiZXh0IjoianMiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjp0cnVlLCJoYXNVUE0iOnRydWUsImhhc0dpdCI6ZmFsc2UsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJHYXRzYnlKUyAxLjkuMjQ3LCBub2RlIHY5LjcuMSBsaW51eC9hbWQ2NCIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vbG9nb3MtLXR1cmJpby5yZXBsLmNvL2dhdHNieWpzLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwicmVhY3RqcyI6eyJkaXNwbGF5TmFtZSI6IlJlYWN0IiwidGFnbGluZSI6IkEgSmF2YVNjcmlwdCBsaWJyYXJ5IGZvciBidWlsZGluZyB1c2VyIGludGVyZmFjZXMiLCJrZXkiOiJyZWFjdGpzIiwiZW50cnlwb2ludCI6InNyYy9BcHAuanMiLCJleHQiOiJqcyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOnRydWUsImhhc1VQTSI6dHJ1ZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiUmVhY3QgMTYuOC4yLCBub2RlIHYxMC4xIGxpbnV4L2FtZDY0IiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL3JlYWN0LnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwicmVhY3R0cyI6eyJkaXNwbGF5TmFtZSI6IlJlYWN0IFR5cGVzY3JpcHQiLCJ0YWdsaW5lIjoiQSBKYXZhU2NyaXB0IGxpYnJhcnkgZm9yIGJ1aWxkaW5nIHVzZXIgaW50ZXJmYWNlcyIsImtleSI6InJlYWN0dHMiLCJlbnRyeXBvaW50Ijoic3JjL0FwcC50c3giLCJleHQiOiJ0c3giLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjp0cnVlLCJoYXNVUE0iOnRydWUsImhhc0dpdCI6ZmFsc2UsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJSZWFjdCAxNi44LjIsIG5vZGUgdjkuNy4xIGxpbnV4L2FtZDY0IiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL3JlYWN0LnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwicmVhY3RyZSI6eyJkaXNwbGF5TmFtZSI6IlJlYWN0IFJlYXNvbiIsInRhZ2xpbmUiOiJSZWFzb24gYmluZGluZ3MgZm9yIFJlYWN0SlMiLCJrZXkiOiJyZWFjdHJlIiwiZW50cnlwb2ludCI6InNyYy9pbmRleC5yZSIsImV4dCI6InJlIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6ZmFsc2UsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJSZWFzb24gMy4xLjUsIG5vZGUgdjkuNy4xIGxpbnV4L2FtZDY0IiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9sb2dvcy0tdHVyYmlvLnJlcGwuY28vcmVhY3RyZS5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImZsb3ciOnsiZGlzcGxheU5hbWUiOiJGbG93IiwidGFnbGluZSI6IkEgc3RhdGljIHR5cGUgY2hlY2tlciBmb3IgSmF2YVNjcmlwdCIsImtleSI6ImZsb3ciLCJlbnRyeXBvaW50Ijoic3JjL2luZGV4LmpzIiwiZXh0IjoianMiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjp0cnVlLCJoYXNVUE0iOnRydWUsImhhc0dpdCI6ZmFsc2UsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJub2RlIHY5LjcuMSBsaW51eC9hbWQ2NCIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9mbG93LnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwiYmFzaCI6eyJkaXNwbGF5TmFtZSI6IkJhc2giLCJ0YWdsaW5lIjoiVGhlIGNsYXNzaWMgVW5peCBzaGVsbCIsImtleSI6ImJhc2giLCJlbnRyeXBvaW50IjoibWFpbi5zaCIsImV4dCI6InNoIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiR05VIGJhc2gsIHZlcnNpb24gNC40LjIwKDEpLXJlbGVhc2UgKHg4Nl82NC1wYy1saW51eC1nbnUpIiwiY2F0ZWdvcnkiOiJQcmFjdGljYWwiLCJpY29uIjoiaHR0cHM6Ly9pY29ucy51dGlsLnJlcGwuY28vYmFzaC5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInF1aWwiOnsiZGlzcGxheU5hbWUiOiJRdWlsIiwidGFnbGluZSI6IkEgcXVhbnR1bSBpbnN0cnVjdGlvbiBsYW5ndWFnZS4iLCJrZXkiOiJxdWlsIiwiZW50cnlwb2ludCI6Im1haW4ucXVpbCIsImV4dCI6InF1aWwiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOmZhbHNlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOmZhbHNlLCJoYXNFdmFsIjp0cnVlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiUHlxdWlsIDEuOS4wLCBQeXRob24gMy42LjEiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvY2xvanVyZS5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInBvbHlnb3R0Ijp7ImRpc3BsYXlOYW1lIjoicG9seWdvdHQiLCJ0YWdsaW5lIjoiQW4gZWxlZ2FudCBpbWFnZSBmb3IgYSBtb3JlIGNpdmlsaXplZCBhZ2UiLCJrZXkiOiJwb2x5Z290dCIsImVudHJ5cG9pbnQiOiJNYWtlZmlsZSIsImV4dCI6ImdvdHQiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJQb2x5Z290dCIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9sYW5ndWFnZS5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImNyeXN0YWwiOnsiZGlzcGxheU5hbWUiOiJDcnlzdGFsIiwidGFnbGluZSI6IkZhc3QgYXMgQywgc2xpY2sgYXMgUnVieSIsImtleSI6ImNyeXN0YWwiLCJlbnRyeXBvaW50IjoibWFpbi5jciIsImV4dCI6ImNyIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiQ3J5c3RhbCAwLjM0LjAgWzQ0MDFlOTBmMF0gKDIwMjAtMDQtMDYpXG5MTFZNOiA4LjAuMCIsImNhdGVnb3J5IjoiUHJhY3RpY2FsIiwiaWNvbiI6Imh0dHBzOi8vbG9nb3MudHVyYmlvLnJlcGwuY28vY3J5c3RhbC5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImp1bGlhIjp7ImRpc3BsYXlOYW1lIjoiSnVsaWEiLCJ0YWdsaW5lIjoiQSBsYW5ndWFnZSBmb3IgaGlnaC1wZXJmb3JtYW5jZSBudW1lcmljYWwgYW5hbHlzaXMgYW5kIGNvbXB1dGF0aW9uYWwgc2NpZW5jZS4iLCJrZXkiOiJqdWxpYSIsImVudHJ5cG9pbnQiOiJtYWluLmpsIiwiZXh0IjoiamwiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjp0cnVlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6Imp1bGlhIHZlcnNpb24gMS4zLjEiLCJjYXRlZ29yeSI6IlByYWN0aWNhbCIsImljb24iOiJodHRwczovL2xvZ29zLnR1cmJpby5yZXBsLmNvL2p1bGlhLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwicGVybDYiOnsiZGlzcGxheU5hbWUiOiJQZXJsIDYiLCJ0YWdsaW5lIjoiYSBoaWdobHkgY2FwYWJsZSwgZmVhdHVyZS1yaWNoIHByb2dyYW1taW5nIGxhbmd1YWdlIG1hZGUgZm9yIGF0IGxlYXN0IHRoZSBuZXh0IGh1bmRyZWQgeWVhcnMuIiwia2V5IjoicGVybDYiLCJlbnRyeXBvaW50IjoibWFpbi5wNiIsImV4dCI6InA2IiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOmZhbHNlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IlRoaXMgaXMgUmFrdWRvIHZlcnNpb24gMjAyMC4wNS4xIGJ1aWx0IG9uIE1vYXJWTSB2ZXJzaW9uIDIwMjAuMDUiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL2xvZ29zLnR1cmJpby5yZXBsLmNvL3Blcmw2LnBuZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwiZWxpeGlyIjp7ImRpc3BsYXlOYW1lIjoiRWxpeGlyIiwidGFnbGluZSI6IkEgZnVuY3Rpb25hbCwgY29uY3VycmVudCwgZ2VuZXJhbC1wdXJwb3NlIHByb2dyYW1taW5nIGxhbmd1YWdlIHRoYXQgcnVucyBvbiB0aGUgRXJsYW5nIFZNIiwia2V5IjoiZWxpeGlyIiwiZW50cnlwb2ludCI6Im1haW4uZXhzIiwiZXh0IjoiZXhzIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiRXJsYW5nL09UUCAyMy4wIiwiY2F0ZWdvcnkiOiJQcmFjdGljYWwiLCJpY29uIjoiaHR0cHM6Ly9sYW5nLWltYWdlcy0tdGltbXktaS1jaGVuLnJlcGwuY28vZWxpeGlyLnBuZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwibmltIjp7ImRpc3BsYXlOYW1lIjoiTmltIiwidGFnbGluZSI6IkFuIGltcGVyYXRpdmUsIG11bHRpLXBhcmFkaWdtLCBjb21waWxlZCBwcm9ncmFtbWluZyBsYW5ndWFnZSIsImtleSI6Im5pbSIsImVudHJ5cG9pbnQiOiJtYWluLm5pbSIsImV4dCI6Im5pbSIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6Ik5pbSBDb21waWxlciBWZXJzaW9uIDEuMi4wICgyMDIwLTA0LTAzKSBbTGludXg6IGFtZDY0XSIsImNhdGVnb3J5IjoiUHJhY3RpY2FsIiwiaWNvbiI6Imh0dHBzOi8vbGFuZy1pbWFnZXMtLXRpbW15LWktY2hlbi5yZXBsLmNvL25pbS5wbmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImRhcnQiOnsiZGlzcGxheU5hbWUiOiJEYXJ0IiwidGFnbGluZSI6IkEgZ2VuZXJhbC1wdXJwb3NlIHByb2dyYW1taW5nIGxhbmd1YWdlIHVzZWQgdG8gYnVpbGQgd2ViLCBzZXJ2ZXIsIGRlc2t0b3AsIGFuZCBtb2JpbGUgYXBwbGljYXRpb25zLiIsImtleSI6ImRhcnQiLCJlbnRyeXBvaW50IjoibWFpbi5kYXJ0IiwiZXh0IjoiZGFydCIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjp0cnVlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiRGFydCBWTSB2ZXJzaW9uOiAyLjYuMCIsImNhdGVnb3J5IjoiUHJhY3RpY2FsIiwiaWNvbiI6Imh0dHBzOi8vbG9nb3MudHVyYmlvLnJlcGwuY28vZGFydC5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImdhdHNieWpzdjIiOnsiZGlzcGxheU5hbWUiOiJHYXRzYnlKUyAyLjAiLCJ0YWdsaW5lIjoiQmxhemluZy1mYXN0IHN0YXRpYyBzaXRlIGdlbmVyYXRvciBmb3IgUmVhY3QiLCJrZXkiOiJnYXRzYnlqc3YyIiwiZW50cnlwb2ludCI6InNyYy9wYWdlcy9pbmRleC5qcyIsImV4dCI6ImpzIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6dHJ1ZSwiaGFzVVBNIjp0cnVlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJHYXRzYnlKUyAyLjAiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL2xvZ29zLS10dXJiaW8ucmVwbC5jby9nYXRzYnlqcy5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInJlYXNvbl9ub2RlanMiOnsiZGlzcGxheU5hbWUiOiJSZWFzb24gTm9kZS5qcyIsInRhZ2xpbmUiOiJSZWFzb24gY29tcGlsaW5nIHRvIE5vZGUuanMgKHZpYSBCdWNrbGVTY3JpcHQpIiwia2V5IjoicmVhc29uX25vZGVqcyIsImVudHJ5cG9pbnQiOiJzcmMvTWFpbi5yZSIsImV4dCI6InJlIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6dHJ1ZSwiaGFzVVBNIjp0cnVlLCJoYXNHaXQiOmZhbHNlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiUmVhc29uIDMuMy40LCBCdWNrbGVzY3JpcHQgNC4wLjE4LCBOb2RlIHYxMC4xNS4yIGxpbnV4L2FtZDY0IiwiY2F0ZWdvcnkiOiJQcmFjdGljYWwiLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL3JlYXNvbi5wbmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInRjbCI6eyJkaXNwbGF5TmFtZSI6IlRjbCIsInRhZ2xpbmUiOiJBIGhpZ2gtbGV2ZWwgbGFuZ3VhZ2UgZGVzaWduZWQgd2l0aCB0aGUgZ29hbCBvZiBiZWluZyB2ZXJ5IHNpbXBsZSBidXQgcG93ZXJmdWwiLCJrZXkiOiJ0Y2wiLCJlbnRyeXBvaW50IjoibWFpbi50Y2wiLCJleHQiOiJ0Y2wiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6ZmFsc2UsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6dHJ1ZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJ0Y2xzaCA4LjYiLCJjYXRlZ29yeSI6IlByYWN0aWNhbCIsImljb24iOiJodHRwczovL2xvZ29zLnR1cmJpby5yZXBsLmNvL3RjbC5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3Ijp0cnVlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwiZXJsYW5nIjp7ImRpc3BsYXlOYW1lIjoiRXJsYW5nIiwidGFnbGluZSI6IkEgZ2VuZXJhbC1wdXJwb3NlLCBjb25jdXJyZW50LCBmdW5jdGlvbmFsIHByb2dyYW1taW5nIGxhbmd1YWdlIiwia2V5IjoiZXJsYW5nIiwiZW50cnlwb2ludCI6Im1haW4uZXJsIiwiZXh0IjoiZXJsIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiRXJsYW5nL09UUCAyMy4wIiwiY2F0ZWdvcnkiOiJQcmFjdGljYWwiLCJpY29uIjoiaHR0cHM6Ly9sYW5nLWltYWdlcy0tdGltbXktaS1jaGVuLnJlcGwuY28vZXJsYW5nLnBuZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwidHlwZXNjcmlwdCI6eyJkaXNwbGF5TmFtZSI6IlR5cGVTY3JpcHQiLCJ0YWdsaW5lIjoiQSB0eXBlZCBzdXBlcnNldCBvZiBKYXZhU2NyaXB0LiIsImtleSI6InR5cGVzY3JpcHQiLCJlbnRyeXBvaW50IjoiaW5kZXgudHMiLCJleHQiOiJ0cyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOnRydWUsImhhc1VQTSI6dHJ1ZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjp0cnVlLCJoYXNJbnRlcnByZXRlciI6dHJ1ZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IlR5cGVTY3JpcHQgdjQuMS4zIE5vZGUuanMgdjEwLjIzLjEgbGludXgvYW1kNjQiLCJjYXRlZ29yeSI6IlByYWN0aWNhbCIsImljb24iOiJodHRwczovL3Rzbm9kZWxvZ28ubWFzZnJvc3QucmVwbC5jby90eXBlc2NyaXB0LnBuZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwib2NhbWwiOnsiZGlzcGxheU5hbWUiOiJPQ2FtbCIsInRhZ2xpbmUiOiJPQ2FtbCBpcyBhIGdlbmVyYWwgcHVycG9zZSBwcm9ncmFtbWluZyBsYW5ndWFnZSB3aXRoIGFuIGVtcGhhc2lzIG9uIGV4cHJlc3NpdmVuZXNzIGFuZCBzYWZldHkiLCJrZXkiOiJvY2FtbCIsImVudHJ5cG9pbnQiOiJtYWluLm1sIiwiZXh0IjoibWwiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0IjpmYWxzZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjp0cnVlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiT0NhbWwgdjQuMDcuMSBsaW51eC9hbWQ2NCIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vb3BhbS5vY2FtbC5vcmcvZXh0L2ltZy9vY2FtbC5wbmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInB5Z2FtZSI6eyJkaXNwbGF5TmFtZSI6IlB5Z2FtZSIsInRhZ2xpbmUiOiJBIGNyb3NzLXBsYXRmb3JtIHB5dGhvbiBncmFwaGljcyBsaWJyYXJ5Iiwia2V5IjoicHlnYW1lIiwiZW50cnlwb2ludCI6Im1haW4ucHkiLCJleHQiOiJweSIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjp0cnVlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJQeXRob24zIHdpdGggUHlnYW1lIiwiY2F0ZWdvcnkiOiJHYW1lIERldmVsb3BtZW50IiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9weXRob24uc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjp0cnVlfX0sImxvdmUyZCI6eyJkaXNwbGF5TmFtZSI6IkxvdmUyRCIsInRhZ2xpbmUiOiJBIGZyZWUsIG9wZW4tc291cmNlIEx1YSBmcmFtZXdvcmsgZm9yIDJEIGdhbWVzIiwia2V5IjoibG92ZTJkIiwiZW50cnlwb2ludCI6Im1haW4ubHVhIiwiZXh0IjoibHVhIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiTE9WRSAxMS4yIChNeXN0ZXJpb3VzIE15c3RlcmllcykiLCJjYXRlZ29yeSI6IkdhbWUgRGV2ZWxvcG1lbnQiLCJpY29uIjoiaHR0cHM6Ly9sYW5nLWltYWdlcy0tdGltbXktaS1jaGVuLnJlcGwuY28vbG92ZTJkLnBuZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6dHJ1ZX19LCJyZWFzb24iOnsiZGlzcGxheU5hbWUiOiJSZWFzb24iLCJ0YWdsaW5lIjoiQSBuZXcgc3ludGF4IGZvciBPQ2FtbCB0aGF0IGlzIHJlbW5pc2NpZW50IG9mIGxhbmd1YWdlcyBsaWtlIEphdmFTY3JpcHQiLCJrZXkiOiJyZWFzb24iLCJlbnRyeXBvaW50IjoibWFpbi5yZSIsImV4dCI6InJlIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6ZmFsc2UsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJSZWFzb24gMy40LjAgKE9DYW1sIHY0LjA3LjEpIGxpbnV4L2FtZDY0IiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL3JlYXNvbi5wbmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sIlRraW50ZXIiOnsiZGlzcGxheU5hbWUiOiJMb3ZlMkQiLCJ0YWdsaW5lIjoiUHl0aG9uJ3Mgc3RhbmRhcmQgR1VJIHRvb2tsaXQiLCJrZXkiOiJUa2ludGVyIiwiZW50cnlwb2ludCI6Im1haW4ucHkiLCJleHQiOiJweSIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoZWFkZXIiOiJQeXRob24zLjYgd2l0aCBUa2ludGVyIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsLml0L3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL3B5dGhvbi5zdmciLCJlbmdpbmUiOiJnb3ZhbCJ9LCJ0a2ludGVyIjp7ImRpc3BsYXlOYW1lIjoiVGtpbnRlciIsInRhZ2xpbmUiOiJQeXRob24ncyBzdGFuZGFyZCBHVUkgdG9va2xpdCIsImtleSI6InRraW50ZXIiLCJlbnRyeXBvaW50IjoibWFpbi5weSIsImV4dCI6InB5IiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOnRydWUsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJQeXRob24zLjYgd2l0aCBUa2ludGVyIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL3B5dGhvbi5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImphdmFfc3dpbmciOnsiZGlzcGxheU5hbWUiOiJKYXZhIFN3aW5nIiwidGFnbGluZSI6IkEgSmF2YSBHVUkgd2lkZ2V0IHRvb2xraXQiLCJrZXkiOiJqYXZhX3N3aW5nIiwiZW50cnlwb2ludCI6Ik1haW4uamF2YSIsImV4dCI6ImphdmEiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJKYXZhIFN3aW5nIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2phdmEuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJwaHBfc2VydmVyIjp7ImRpc3BsYXlOYW1lIjoiUEhQIFdlYiBTZXJ2ZXIiLCJ0YWdsaW5lIjoiQSBwb3B1bGFyIGdlbmVyYWwtcHVycG9zZSBzY3JpcHRpbmcgbGFuZ3VhZ2UuIiwia2V5IjoicGhwX3NlcnZlciIsImVudHJ5cG9pbnQiOiJpbmRleC5waHAiLCJleHQiOiJwaHAiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJQSFAgV2ViIFNlcnZlciA3LjIuMTctMHVidW50dTAuMTguMDQuMSAoY2xpKSAoYnVpbHQ6IEFwciAxOCAyMDE5IDE0OjEyOjM4KSAoIE5UUyApXG5Db3B5cmlnaHQgKGMpIDE5OTctMjAxOCBUaGUgUEhQIEdyb3VwXG5aZW5kIEVuZ2luZSB2My4yLjAsIENvcHlyaWdodCAoYykgMTk5OC0yMDE4IFplbmQgVGVjaG5vbG9naWVzIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL3BocC5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sIm5vZGVqc19wcnliYXIiOnsiZGlzcGxheU5hbWUiOiJOb2RlLmpzIiwidGFnbGluZSI6IkV2ZW50ZWQgSS9PIGZvciBWOCBKYXZhU2NyaXB0LiIsImtleSI6Im5vZGVqc19wcnliYXIiLCJlbnRyeXBvaW50IjoiaW5kZXguanMiLCJleHQiOiJqcyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOnRydWUsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6dHJ1ZSwiaGFzVVBNIjp0cnVlLCJoYXNHaXQiOmZhbHNlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOnRydWUsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJub2RlIHYxMC4xNS4yIGxpbnV4L2FtZDY0IiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL25vZGVqcy5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImVsaXNwIjp7ImRpc3BsYXlOYW1lIjoiRW1hY3MgTGlzcCAoRWxpc3ApIiwidGFnbGluZSI6IlNjcmlwdGluZyBsYW5ndWFnZSBmb3IgdGhlIGV4dGVuc2libGUgdGV4dCBlZGl0b3IuIiwia2V5IjoiZWxpc3AiLCJlbnRyeXBvaW50IjoibWFpbi5lbCIsImV4dCI6ImVsIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjp0cnVlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6dHJ1ZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJHTlUgRW1hY3MgMjYuMiIsImNhdGVnb3J5IjoiUHJhY3RpY2FsIiwiaWNvbiI6Imh0dHBzOi8vaWNvbnMtLXV0aWwucmVwbC5jby9lbWFjcy5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInBocDciOnsiZGlzcGxheU5hbWUiOiJQSFAgV2ViIFNlcnZlciIsInRhZ2xpbmUiOiJBIHBvcHVsYXIgZ2VuZXJhbC1wdXJwb3NlIHNjcmlwdGluZyBsYW5ndWFnZS4iLCJrZXkiOiJwaHA3IiwiZW50cnlwb2ludCI6ImluZGV4LnBocCIsImV4dCI6InBocCIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0IjpmYWxzZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJQSFAgNy4yLjE3LTB1YnVudHUwLjE4LjA0LjEgKGNsaSkgKGJ1aWx0OiBBcHIgMTggMjAxOSAxNDoxMjozOCkgKCBOVFMgKVxuQ29weXJpZ2h0IChjKSAxOTk3LTIwMTggVGhlIFBIUCBHcm91cFxuWmVuZCBFbmdpbmUgdjMuMi4wLCBDb3B5cmlnaHQgKGMpIDE5OTgtMjAxOCBaZW5kIFRlY2hub2xvZ2llcyIsImNhdGVnb3J5IjoiV2ViIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9waHAuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJzcWxpdGUiOnsiZGlzcGxheU5hbWUiOiJTUUxpdGUiLCJ0YWdsaW5lIjoiRW1iZWRkZWQgU1FMIGRhdGFiYXNlIGVuZ2luZS4iLCJrZXkiOiJzcWxpdGUiLCJlbnRyeXBvaW50IjoibWFpbi5zcWwiLCJleHQiOiJzcWwiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOmZhbHNlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6dHJ1ZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJTUUxpdGUgdmVyc2lvbiAzLjIyLjAiLCJjYXRlZ29yeSI6IlByYWN0aWNhbCIsImljb24iOiJodHRwczovL2ljb25zLS11dGlsLnJlcGwuY28vc3FsaXRlLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwiamF2YTEwIjp7ImRpc3BsYXlOYW1lIjoiSmF2YSIsInRhZ2xpbmUiOiJBIGNvbmN1cnJlbnQsIGNsYXNzLWJhc2VkLCBzdGF0aWNhbGx5IHR5cGVkIG9iamVjdC1vcmllbnRlZCBsYW5ndWFnZS4iLCJrZXkiOiJqYXZhMTAiLCJlbnRyeXBvaW50IjoiTWFpbi5qYXZhIiwiZXh0IjoiamF2YSIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjp0cnVlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOnRydWUsImhlYWRlciI6Ik9wZW5KREsgUnVudGltZSBFbnZpcm9ubWVudCAoYnVpbGQgMTEuMC42KzEwLXBvc3QtVWJ1bnR1LTF1YnVudHUxMTguMDQuMSkiLCJjYXRlZ29yeSI6IlByYWN0aWNhbCIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvamF2YS5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInBocF9jbGkiOnsiZGlzcGxheU5hbWUiOiJQSFAgQ0xJIiwidGFnbGluZSI6IkEgcG9wdWxhciBnZW5lcmFsLXB1cnBvc2Ugc2NyaXB0aW5nIGxhbmd1YWdlLiIsImtleSI6InBocF9jbGkiLCJlbnRyeXBvaW50IjoibWFpbi5waHAiLCJleHQiOiJwaHAiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJQSFAgQ0xJIDcuMi4xNy0wdWJ1bnR1MC4xOC4wNC4xIChjbGkpIChidWlsdDogQXByIDE4IDIwMTkgMTQ6MTI6MzgpICggTlRTIClcbkNvcHlyaWdodCAoYykgMTk5Ny0yMDE4IFRoZSBQSFAgR3JvdXBcblplbmQgRW5naW5lIHYzLjIuMCwgQ29weXJpZ2h0IChjKSAxOTk4LTIwMTggWmVuZCBUZWNobm9sb2dpZXMiLCJjYXRlZ29yeSI6IlByYWN0aWNhbCIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvcGhwLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwibm9kZWpzX2JldGEiOnsiZGlzcGxheU5hbWUiOiJOb2RlLmpzIiwidGFnbGluZSI6IkV2ZW50ZWQgSS9PIGZvciBWOCBKYXZhU2NyaXB0LiIsImtleSI6Im5vZGVqc19iZXRhIiwiZW50cnlwb2ludCI6ImluZGV4LmpzIiwiZXh0IjoianMiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjp0cnVlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOnRydWUsImhhc1VQTSI6dHJ1ZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjp0cnVlLCJoYXNJbnRlcnByZXRlciI6dHJ1ZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhhc0RBUCI6dHJ1ZSwiaGVhZGVyIjoibm9kZSB2MTIuMTYuMSIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9ub2RlanMuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJweXhlbCI6eyJkaXNwbGF5TmFtZSI6IlB5eGVsIiwidGFnbGluZSI6IkEgcmV0cm8gZ2FtZSBlbmdpbmUgZm9yIFB5dGhvbiIsImtleSI6InB5eGVsIiwiZW50cnlwb2ludCI6Im1haW4ucHkiLCJleHQiOiJweSIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiUHl0aG9uMyB3aXRoIFB5eGVsIiwiY2F0ZWdvcnkiOiJHYW1lIERldmVsb3BtZW50IiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9weXRob24uc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjp0cnVlfX0sInN0YXRpYyI6eyJkaXNwbGF5TmFtZSI6IlN0YXRpYyIsInRhZ2xpbmUiOiJBIGJhc2UgbGFuZ3VhZ2UgZm9yIGNsaWVudCBzaWRlIGxhbmd1YWdlcyIsImtleSI6InN0YXRpYyIsImVudHJ5cG9pbnQiOiJNYWtlZmlsZSIsImV4dCI6Imh0bWwiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOmZhbHNlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2xhbmd1YWdlLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwicmlkZGxlanMiOnsiZGlzcGxheU5hbWUiOiJOb2RlLmpzPyIsInRhZ2xpbmUiOiJobW1tbW0/Iiwia2V5IjoicmlkZGxlanMiLCJlbnRyeXBvaW50IjoiaW5kZXguanMiLCJleHQiOiJqcyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOnRydWUsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6dHJ1ZSwiaGFzVVBNIjp0cnVlLCJoYXNHaXQiOmZhbHNlLCJoYXNFdmFsIjp0cnVlLCJoYXNJbnRlcnByZXRlciI6dHJ1ZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6Im5vZGU/Pz8gdjEwLjE2LjA/IiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL25vZGVqcy5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sIndhc20iOnsiZGlzcGxheU5hbWUiOiJXZWJBc3NlbWJseSIsInRhZ2xpbmUiOiJBIGluc3RydWN0aW9uIGZvcm1hdCBmb3IgYSBzdGFjay1iYXNlZCB2aXJ0dWFsIG1hY2hpbmUiLCJrZXkiOiJ3YXNtIiwiZW50cnlwb2ludCI6Im1haW4ud2F0IiwiZXh0Ijoid2F0IiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoid2FzbWVyIHYwLjguMCBsaW51eCIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vaWNvbnMudXRpbC5yZXBsLmNvL3dhc20uc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJweXRob24zX2NsYXNzcm9vbSI6eyJkaXNwbGF5TmFtZSI6IlB5dGhvbiIsInRhZ2xpbmUiOiJBIGR5bmFtaWMgbGFuZ3VhZ2UgZW1waGFzaXppbmcgcmVhZGFiaWxpdHkuIiwia2V5IjoicHl0aG9uM19jbGFzc3Jvb20iLCJlbnRyeXBvaW50IjoibWFpbi5weSIsImV4dCI6InB5IiwiaGFzTGludCI6dHJ1ZSwiaGFzVW5pdFRlc3RzIjp0cnVlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOnRydWUsImhhc1VQTSI6dHJ1ZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjp0cnVlLCJoYXNJbnRlcnByZXRlciI6dHJ1ZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IlB5dGhvbiAzLjguMSAoZGVmYXVsdCwgRmViICAyIDIwMjAsIDA4OjM3OjM3KSIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9weXRob24uc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJ0ZXN0aiI6eyJkaXNwbGF5TmFtZSI6IlRlc3RKIiwidGFnbGluZSI6IkEgY29uY3VycmVudCwgY2xhc3MtYmFzZWQsIHN0YXRpY2FsbHkgdHlwZWQgb2JqZWN0LW9yaWVudGVkIGxhbmd1YWdlLiIsImtleSI6InRlc3RqIiwiZW50cnlwb2ludCI6Ik1haW4uamF2YSIsImV4dCI6ImphdmEiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6dHJ1ZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiVGVzdEoiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvamF2YS5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInRlc3RqX2JldGEiOnsiZGlzcGxheU5hbWUiOiJUZXN0SiIsInRhZ2xpbmUiOiJBIGNvbmN1cnJlbnQsIGNsYXNzLWJhc2VkLCBzdGF0aWNhbGx5IHR5cGVkIG9iamVjdC1vcmllbnRlZCBsYW5ndWFnZS4iLCJrZXkiOiJ0ZXN0al9iZXRhIiwiZW50cnlwb2ludCI6Ik1haW4uamF2YSIsImV4dCI6ImphdmEiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6dHJ1ZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiVGVzdEoiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvamF2YS5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInB5dGhvbl9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiUHl0aG9uIDIuNyIsInRhZ2xpbmUiOiJBIGR5bmFtaWMgbGFuZ3VhZ2UgZW1waGFzaXppbmcgcmVhZGFiaWxpdHkuIiwia2V5IjoicHl0aG9uX2JldGEiLCJlbnRyeXBvaW50IjoibWFpbi5weSIsImV4dCI6InB5IiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6dHJ1ZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjp0cnVlLCJoYXNVUE0iOnRydWUsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6dHJ1ZSwiaGFzSW50ZXJwcmV0ZXIiOnRydWUsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJQeXRob24gMi43LjE2IChkZWZhdWx0LCBKdWwgMTMgMjAxOSwgMTY6MDE6NTEpXG5bR0NDIDguMy4wXSBvbiBsaW51eDIiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvcHl0aG9uLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwicmFrdSI6eyJkaXNwbGF5TmFtZSI6IlJha3UiLCJ0YWdsaW5lIjoiQSBoaWdobHkgY2FwYWJsZSwgZmVhdHVyZS1yaWNoIHByb2dyYW1taW5nIGxhbmd1YWdlIG1hZGUgZm9yIGF0IGxlYXN0IHRoZSBuZXh0IGh1bmRyZWQgeWVhcnMuIiwia2V5IjoicmFrdSIsImVudHJ5cG9pbnQiOiJtYWluLnJha3UiLCJleHQiOiJyYWt1IiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOmZhbHNlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IlRoaXMgaXMgUmFrdWRvIHZlcnNpb24gMjAyMC4wNiBidWlsdCBvbiBNb2FyVk0gdmVyc2lvbiAyMDIwLjA2IiwiY2F0ZWdvcnkiOiJQcmFjdGljYWwiLCJpY29uIjoiaHR0cHM6Ly9sb2dvcy50dXJiaW8ucmVwbC5jby9wZXJsNi5wbmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3Ijp0cnVlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwiamF2YTEwX2JldGEiOnsiZGlzcGxheU5hbWUiOiJKYXZhIiwidGFnbGluZSI6IkEgY29uY3VycmVudCwgY2xhc3MtYmFzZWQsIHN0YXRpY2FsbHkgdHlwZWQgb2JqZWN0LW9yaWVudGVkIGxhbmd1YWdlLiIsImtleSI6ImphdmExMF9iZXRhIiwiZW50cnlwb2ludCI6Ik1haW4uamF2YSIsImV4dCI6ImphdmEiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6dHJ1ZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGFzREFQIjp0cnVlLCJoZWFkZXIiOiJPcGVuSkRLIFJ1bnRpbWUgRW52aXJvbm1lbnQgKGJ1aWxkIDExLjAuNisxMC1wb3N0LVVidW50dS0xdWJ1bnR1MTE4LjA0LjEpIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2phdmEuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJodG1sX2JldGEiOnsiZGlzcGxheU5hbWUiOiJIVE1MLCBDU1MsIEpTIiwidGFnbGluZSI6IlRoZSBsYW5ndWFnZXMgdGhhdCBtYWtlIHVwIHRoZSB3ZWIuIiwia2V5IjoiaHRtbF9iZXRhIiwiZW50cnlwb2ludCI6ImluZGV4Lmh0bWwiLCJleHQiOiJodG1sIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Ii9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy93ZWJfcHJvamVjdC5zdmciLCJlbmdpbmUiOiJyZXBsYm94IiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwicHl0aG9uM19iZXRhIjp7ImRpc3BsYXlOYW1lIjoiUHl0aG9uIiwidGFnbGluZSI6IkEgZHluYW1pYyBsYW5ndWFnZSBlbXBoYXNpemluZyByZWFkYWJpbGl0eS4iLCJrZXkiOiJweXRob24zX2JldGEiLCJlbnRyeXBvaW50IjoibWFpbi5weSIsImV4dCI6InB5IiwiaGFzTGludCI6dHJ1ZSwiaGFzVW5pdFRlc3RzIjp0cnVlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOnRydWUsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6dHJ1ZSwiaGFzSW50ZXJwcmV0ZXIiOnRydWUsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOnRydWUsImhlYWRlciI6IlB5dGhvbiAzLjguMiAoZGVmYXVsdCwgRmViIDI2IDIwMjAsIDAyOjU2OjEwKSIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9weXRob24uc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJnb19iZXRhIjp7ImRpc3BsYXlOYW1lIjoiR28iLCJ0YWdsaW5lIjoiU3RhdGljYWxseSB0eXBlZCB5ZXQgZXhwcmVzc2l2ZSBsYW5ndWFnZSB3aXRoIGEgZm9jdXMgb24gY29uY3VycmVuY3kuIiwia2V5IjoiZ29fYmV0YSIsImVudHJ5cG9pbnQiOiJtYWluLmdvIiwiZXh0IjoiZ28iLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiZ28gdmVyc2lvbiBnbzEuMTQgbGludXgvYW1kNjQiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvZ28uc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJqYXZhX21hdmVuIjp7ImRpc3BsYXlOYW1lIjoiSmF2YSAod2l0aCBNYXZlbikiLCJ0YWdsaW5lIjoiQSBjb25jdXJyZW50LCBjbGFzcy1iYXNlZCwgc3RhdGljYWxseSB0eXBlZCBvYmplY3Qtb3JpZW50ZWQgbGFuZ3VhZ2UuIiwia2V5IjoiamF2YV9tYXZlbiIsImVudHJ5cG9pbnQiOiJNYWluLmphdmEiLCJleHQiOiJqYXZhIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOnRydWUsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6Ik9wZW5KREsgUnVudGltZSBFbnZpcm9ubWVudCAoYnVpbGQgMTAuMC4yKzEzLVVidW50dS0xdWJ1bnR1MC4xOC4wNC40KSIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9qYXZhLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwic2NhbGEiOnsiZGlzcGxheU5hbWUiOiJTY2FsYSAoYmV0YSkiLCJ0YWdsaW5lIjoiU2NhbGEgY29tYmluZXMgb2JqZWN0LW9yaWVudGVkIGFuZCBmdW5jdGlvbmFsIHByb2dyYW1taW5nIGluIG9uZSBjb25jaXNlLCBoaWdoLWxldmVsIGxhbmd1YWdlIiwia2V5Ijoic2NhbGEiLCJlbnRyeXBvaW50IjoibWFpbi5zY2FsYSIsImV4dCI6InNjYWxhIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOmZhbHNlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IlNjYWxhIDIuMTMuMSIsImNhdGVnb3J5IjoiUHJhY3RpY2FsIiwiaWNvbiI6Imh0dHBzOi8vaWNvbnMtLXV0aWwucmVwbC5jby9zY2FsYS5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3Ijp0cnVlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwibm9kZWpzX3N0YXRpYyI6eyJkaXNwbGF5TmFtZSI6Im5vZGVqcyBzdGF0dWM6IHRoaXMgaXMganVzdCBhIHRlc3QuLi4gcGxzIGRvbid0IHVzZSIsInRhZ2xpbmUiOiJhemFhYWFhYWFhYWFhYWFhYWFhYWFhYSIsImtleSI6Im5vZGVqc19zdGF0aWMiLCJlbnRyeXBvaW50IjoiaW5kZXguanMiLCJleHQiOiJqcyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjp0cnVlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6dHJ1ZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6Im5vZGUgdjEwLjE2LjAiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvamF2YXNjcmlwdC5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImZvcnRoX2JldGEiOnsiZGlzcGxheU5hbWUiOiJGb3J0aCIsInRhZ2xpbmUiOiJBbiBpbnRlcmFjdGl2ZSBzdGFjay1vcmllbnRlZCBsYW5ndWFnZS4iLCJrZXkiOiJmb3J0aF9iZXRhIiwiZW50cnlwb2ludCI6Im1haW4uZnRoIiwiZXh0IjoiZnRoIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IkpTLUZvcnRoIDAuNTIwMDgwNDE3MTM0MlxuaHR0cDovL3d3dy5mb3J0aGZyZWFrLm5ldC9qc2ZvcnRoLmh0bWxcblRoaXMgcHJvZ3JhbSBpcyBwdWJsaXNoZWQgdW5kZXIgdGhlIEdQTC4iLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiIvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvbGFuZ3VhZ2Uuc3ZnIiwiZW5naW5lIjoicmVwbGJveCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImhhc2tlbGxfYmV0YSI6eyJkaXNwbGF5TmFtZSI6Ikhhc2tlbGwiLCJ0YWdsaW5lIjoiQW4gYWR2YW5jZWQsIHB1cmVseSBmdW5jdGlvbmFsIHByb2dyYW1taW5nIGxhbmd1YWdlIiwia2V5IjoiaGFza2VsbF9iZXRhIiwiZW50cnlwb2ludCI6Im1haW4uaHMiLCJleHQiOiJocyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjp0cnVlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiR0hDaSwgdmVyc2lvbiA4LjYuNSIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9oYXNrZWxsLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwicnVieV9jbGFzc3Jvb20iOnsiZGlzcGxheU5hbWUiOiJSdWJ5IiwidGFnbGluZSI6IkEgbmF0dXJhbCBkeW5hbWljIG9iamVjdC1vcmllbnRlZCBsYW5ndWFnZS4iLCJrZXkiOiJydWJ5X2NsYXNzcm9vbSIsImVudHJ5cG9pbnQiOiJtYWluLnJiIiwiZXh0IjoicmIiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjp0cnVlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOnRydWUsImhhc1VQTSI6dHJ1ZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjp0cnVlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJydWJ5IDIuNS41cDE1NyAoMjAxOS0wMy0xNSByZXZpc2lvbiA2NzI2MCkgW3g4Nl82NC1saW51eF0iLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvcnVieS5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInJsYW5nX2JldGEiOnsiZGlzcGxheU5hbWUiOiJSIiwidGFnbGluZSI6IkEgcHJvZ3JhbW1pbmcgbGFuZ3VhZ2UgYW5kIGVudmlyb25tZW50IGZvciBzdGF0aXN0aWNhbCBjb21wdXRpbmcgYW5kIGdyYXBoaWNzIiwia2V5IjoicmxhbmdfYmV0YSIsImVudHJ5cG9pbnQiOiJtYWluLnIiLCJleHQiOiJyIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoidXNpbmcgR05VIFIgVmVyc2lvbiAzLjUuMCAoMjAxOC0wNC0yMykiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL2xvZ29zLnR1cmJpby5yZXBsLmNvL3JsYW5nLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwicXVpbF9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiUXVpbCIsInRhZ2xpbmUiOiJBIHF1YW50dW0gaW5zdHJ1Y3Rpb24gbGFuZ3VhZ2UuIiwia2V5IjoicXVpbF9iZXRhIiwiZW50cnlwb2ludCI6Im1haW4ucXVpbCIsImV4dCI6InF1aWwiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOmZhbHNlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOmZhbHNlLCJoYXNFdmFsIjp0cnVlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiUHlxdWlsIDEuOS4wLCBQeXRob24gMy42LjEiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvY2xvanVyZS5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImtvdGxpbl9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiS290bGluIiwidGFnbGluZSI6IlN0YXRpY2FsbHkgdHlwZWQgcHJvZ3JhbW1pbmcgbGFuZ3VhZ2UgaW50ZXJvcGVyYWJsZSB3aXRoIEphdmEgYW5kIEFuZHJvaWQiLCJrZXkiOiJrb3RsaW5fYmV0YSIsImVudHJ5cG9pbnQiOiJtYWluLmt0IiwiZXh0Ijoia3QiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6ZmFsc2UsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoia290bGluYy1qdm0gMS4zLjcyIChKUkUgMTEuMC44KzEwLXBvc3QtVWJ1bnR1LTB1YnVudHUxMTguMDQuMSlcblxuSGludDogcnVuIFx1MDAxYlszMm1rb3RsaW5jLWp2bVx1MDAxYlswbSBmb3IgdGhlIGludGVyYWN0aXZlIHJlcGwiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMva290bGluLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwiY2xvanVyZV9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiQ2xvanVyZSIsInRhZ2xpbmUiOiJBIG1vZGVybiBKVk0tYmFzZWQgTGlzcCBkaWFsZWN0IHdpdGggYSBmb2N1cyBvbiBpbW11dGFiaWxpdHkiLCJrZXkiOiJjbG9qdXJlX2JldGEiLCJlbnRyeXBvaW50IjoibWFpbi5jbGoiLCJleHQiOiJjbGoiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOmZhbHNlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOnRydWUsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJDbG9qdXJlIDEuOC4wXG5KYXZhIEhvdFNwb3QoVE0pIDY0LUJpdCBTZXJ2ZXIgVk0gMS44LjBfOTEtYjE0IiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2Nsb2p1cmUuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJ0eXBlc2NyaXB0X2JldGEiOnsiZGlzcGxheU5hbWUiOiJUeXBlU2NyaXB0IiwidGFnbGluZSI6IkEgdHlwZWQgc3VwZXJzZXQgb2YgSmF2YVNjcmlwdC4iLCJrZXkiOiJ0eXBlc2NyaXB0X2JldGEiLCJlbnRyeXBvaW50IjoiaW5kZXgudHMiLCJleHQiOiJ0cyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOnRydWUsImhhc1VQTSI6dHJ1ZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjp0cnVlLCJoYXNJbnRlcnByZXRlciI6dHJ1ZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IlR5cGVTY3JpcHQgdjQuMS4zIE5vZGUuanMgdjEwLjIzLjEgbGludXgvYW1kNjQiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3Rzbm9kZWxvZ28ubWFzZnJvc3QucmVwbC5jby90eXBlc2NyaXB0LnBuZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwicnVieV9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiUnVieSIsInRhZ2xpbmUiOiJBIG5hdHVyYWwgZHluYW1pYyBvYmplY3Qtb3JpZW50ZWQgbGFuZ3VhZ2UuIiwia2V5IjoicnVieV9iZXRhIiwiZW50cnlwb2ludCI6Im1haW4ucmIiLCJleHQiOiJyYiIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOnRydWUsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6InJ1YnkgMi41LjVwMTU3ICgyMDE5LTAzLTE1IHJldmlzaW9uIDY3MjYwKSBbeDg2XzY0LWxpbnV4XVxuXG5IaW50OiBydW4gXHUwMDFiWzMybWlyYlx1MDAxYlswbSBmb3IgdGhlIGludGVyYWN0aXZlIHJlcGwiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvcnVieS5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sIm5peCI6eyJkaXNwbGF5TmFtZSI6Ik5peCAoYmV0YSkiLCJ0YWdsaW5lIjoiQSBiYXNlIHJlcGwgZm9yIGJ1aWxkaW5nIGFueXRoaW5nIHlvdSB3YW50IGluIGFueSBsYW5ndWFnZS4iLCJrZXkiOiJuaXgiLCJlbnRyeXBvaW50IjoiLnJlcGxpdCIsImV4dCI6InNoIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiY2F0ZWdvcnkiOiJQcmFjdGljYWwiLCJpY29uIjoiaHR0cHM6Ly9pY29ucy51dGlsLnJlcGwuY28vYmFzaC5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImxvbGNvZGVfYmV0YSI6eyJkaXNwbGF5TmFtZSI6IkxPTENPREUiLCJ0YWdsaW5lIjoiVGhlIGJhc2ljIGxhbmd1YWdlIG9mIGxvbGNhdHMuIiwia2V5IjoibG9sY29kZV9iZXRhIiwiZW50cnlwb2ludCI6Im1haW4ubG9sIiwiZXh0IjoibG9sIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IkxPTENPREUgdjEuMiAobG9sLWNvZmZlZSlcbkNvcHlyaWdodCAoYykgMjAxMSBNYXggU2hhd2Fia2VoIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2xvbGNvZGUuc3ZnIiwiZW5naW5lIjoicmVwbGJveCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImZzaGFycF9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiRiMiLCJ0YWdsaW5lIjoiQSBNaWNyb3NvZnQgLk5FVCBmdW5jdGlvbmFsIHByb2dyYW1taW5nIGxhbmd1YWdlLiIsImtleSI6ImZzaGFycF9iZXRhIiwiZW50cnlwb2ludCI6Im1haW4uZnMiLCJleHQiOiJmcyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IkYjIENvbXBpbGVyIGZvciBGIyA0LjUgKE9wZW4gU291cmNlIEVkaXRpb24pIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2ZzaGFycC5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImVsaXhpcl9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiRWxpeGlyIiwidGFnbGluZSI6IkEgZnVuY3Rpb25hbCwgY29uY3VycmVudCwgZ2VuZXJhbC1wdXJwb3NlIHByb2dyYW1taW5nIGxhbmd1YWdlIHRoYXQgcnVucyBvbiB0aGUgRXJsYW5nIFZNIiwia2V5IjoiZWxpeGlyX2JldGEiLCJlbnRyeXBvaW50IjoibWFpbi5leHMiLCJleHQiOiJleHMiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJFcmxhbmcvT1RQIDIzLjAiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL2xhbmctaW1hZ2VzLS10aW1teS1pLWNoZW4ucmVwbC5jby9lbGl4aXIucG5nIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJjcHBfYmV0YSI6eyJkaXNwbGF5TmFtZSI6IkMrKyIsInRhZ2xpbmUiOiJBIGdlbmVyYWwgcHVycG9zZSBzeXN0ZW0gcHJvZ3JhbW1pbmcgbGFuZ3VhZ2UuIiwia2V5IjoiY3BwX2JldGEiLCJlbnRyeXBvaW50IjoibWFpbi5jcHAiLCJleHQiOiJjcHAiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGFzREFQIjp0cnVlLCJoZWFkZXIiOiJjbGFuZyB2ZXJzaW9uIDcuMC4wLTN+dWJ1bnR1MC4xOC4wNC4xICh0YWdzL1JFTEVBU0VfNzAwL2ZpbmFsKSIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9jcHAuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJlbGlzcF9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiRW1hY3MgTGlzcCAoRWxpc3ApIiwidGFnbGluZSI6IlNjcmlwdGluZyBsYW5ndWFnZSBmb3IgdGhlIGV4dGVuc2libGUgdGV4dCBlZGl0b3IuIiwia2V5IjoiZWxpc3BfYmV0YSIsImVudHJ5cG9pbnQiOiJtYWluLmVsIiwiZXh0IjoiZWwiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOmZhbHNlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOnRydWUsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjp0cnVlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IkdOVSBFbWFjcyAyNi4yIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9pY29ucy0tdXRpbC5yZXBsLmNvL2VtYWNzLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwic2NhbGFfYmV0YSI6eyJkaXNwbGF5TmFtZSI6IlNjYWxhIChiZXRhKSIsInRhZ2xpbmUiOiJTY2FsYSBjb21iaW5lcyBvYmplY3Qtb3JpZW50ZWQgYW5kIGZ1bmN0aW9uYWwgcHJvZ3JhbW1pbmcgaW4gb25lIGNvbmNpc2UsIGhpZ2gtbGV2ZWwgbGFuZ3VhZ2UiLCJrZXkiOiJzY2FsYV9iZXRhIiwiZW50cnlwb2ludCI6Im1haW4uc2NhbGEiLCJleHQiOiJzY2FsYSIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0IjpmYWxzZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJTY2FsYSAyLjEzLjEiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL2ljb25zLS11dGlsLnJlcGwuY28vc2NhbGEuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJicmFpbmZ1Y2tfYmV0YSI6eyJkaXNwbGF5TmFtZSI6IkJyYWluRiIsInRhZ2xpbmUiOiJBIHB1cmUgVHVyaW5nIG1hY2hpbmUgY29udHJvbGxlci4iLCJrZXkiOiJicmFpbmZ1Y2tfYmV0YSIsImVudHJ5cG9pbnQiOiJtYWluLmJmIiwiZXh0IjoiYmYiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOmZhbHNlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiQnJhaW5GKioqLCBiZmpzXG5Db3B5cmlnaHQgKGMpIDIwMTEgQW1qYWQgTWFzYWQiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiIvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvYnJhaW5mdWNrLnN2ZyIsImVuZ2luZSI6InJlcGxib3giLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJzd2lmdF9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiU3dpZnQiLCJ0YWdsaW5lIjoiQSBtb2Rlcm4gZ2VuZXJhbC1wdXJwb3NlIHByb2dyYW1taW5nIGxhbmd1YWdlIGZyb20gQXBwbGUuIiwia2V5Ijoic3dpZnRfYmV0YSIsImVudHJ5cG9pbnQiOiJtYWluLnN3aWZ0IiwiZXh0Ijoic3dpZnQiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJTd2lmdCB2ZXJzaW9uIDUuMC4xIChzd2lmdC01LjAuMS1SRUxFQVNFKSIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9zd2lmdC5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sIm5pbV9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiTmltIiwidGFnbGluZSI6IkFuIGltcGVyYXRpdmUsIG11bHRpLXBhcmFkaWdtLCBjb21waWxlZCBwcm9ncmFtbWluZyBsYW5ndWFnZSIsImtleSI6Im5pbV9iZXRhIiwiZW50cnlwb2ludCI6Im1haW4ubmltIiwiZXh0IjoibmltIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiTmltIENvbXBpbGVyIFZlcnNpb24gMS4yLjAgKDIwMjAtMDQtMDMpIFtMaW51eDogYW1kNjRdIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9sYW5nLWltYWdlcy0tdGltbXktaS1jaGVuLnJlcGwuY28vbmltLnBuZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwianVsaWFfYmV0YSI6eyJkaXNwbGF5TmFtZSI6Ikp1bGlhIiwidGFnbGluZSI6IkEgbGFuZ3VhZ2UgZm9yIGhpZ2gtcGVyZm9ybWFuY2UgbnVtZXJpY2FsIGFuYWx5c2lzIGFuZCBjb21wdXRhdGlvbmFsIHNjaWVuY2UuIiwia2V5IjoianVsaWFfYmV0YSIsImVudHJ5cG9pbnQiOiJtYWluLmpsIiwiZXh0IjoiamwiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjp0cnVlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6Imp1bGlhIHZlcnNpb24gMS4zLjEiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL2xvZ29zLnR1cmJpby5yZXBsLmNvL2p1bGlhLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwiYmFzaF9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiQmFzaCIsInRhZ2xpbmUiOiJUaGUgY2xhc3NpYyBVbml4IHNoZWxsIiwia2V5IjoiYmFzaF9iZXRhIiwiZW50cnlwb2ludCI6Im1haW4uc2giLCJleHQiOiJzaCIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IkdOVSBiYXNoLCB2ZXJzaW9uIDQuNC4yMCgxKS1yZWxlYXNlICh4ODZfNjQtcGMtbGludXgtZ251KSIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vaWNvbnMudXRpbC5yZXBsLmNvL2Jhc2guc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJkZW5vX2JldGEiOnsiZGlzcGxheU5hbWUiOiJEZW5vIChiZXRhKSIsInRhZ2xpbmUiOiJBIHNlY3VyZSBydW50aW1lIGZvciBKYXZhU2NyaXB0IGFuZCBUeXBlU2NyaXB0Iiwia2V5IjoiZGVub19iZXRhIiwiZW50cnlwb2ludCI6ImluZGV4LnRzIiwiZXh0IjoidHMiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiRGVubyAxLjcuMFxuXG5IaW50OiBydW4gXHUwMDFiWzMybWRlbm9cdTAwMWJbMG0gZm9yIHRoZSBpbnRlcmFjdGl2ZSByZXBsIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9pY29ucy51dGlsLnJlcGwuY28vZGVuby1uby10cmFuc3BhcmVudC5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInB5Z2FtZV9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiUHlnYW1lIiwidGFnbGluZSI6IkEgY3Jvc3MtcGxhdGZvcm0gcHl0aG9uIGdyYXBoaWNzIGxpYnJhcnkiLCJrZXkiOiJweWdhbWVfYmV0YSIsImVudHJ5cG9pbnQiOiJtYWluLnB5IiwiZXh0IjoicHkiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6dHJ1ZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiUHl0aG9uMyB3aXRoIFB5Z2FtZSIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9weXRob24uc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJweXRob25fdHVydGxlX2JldGEiOnsiZGlzcGxheU5hbWUiOiJQeXRob24gKHdpdGggVHVydGxlKSIsInRhZ2xpbmUiOiJBIHNpbXBsZSB2ZXJzaW9uIG9mIFB5dGhvbiB0aGF0IHN1cHBvcnRzIFR1cnRsZS4iLCJrZXkiOiJweXRob25fdHVydGxlX2JldGEiLCJlbnRyeXBvaW50IjoibWFpbi5weSIsImV4dCI6InB5IiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbC5pdC9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9weXRob25fdHVydGxlLnN2ZyIsImVuZ2luZSI6InJlcGxib3giLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJyb3lfYmV0YSI6eyJkaXNwbGF5TmFtZSI6IlJveSIsInRhZ2xpbmUiOiJTbWFsbCBmdW5jdGlvbmFsIGxhbmd1YWdlIHRoYXQgY29tcGlsZXMgdG8gSmF2YVNjcmlwdC4iLCJrZXkiOiJyb3lfYmV0YSIsImVudHJ5cG9pbnQiOiJtYWluLnJveSIsImV4dCI6InJveSIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6ZmFsc2UsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJSb3kgMC4xLjNcbkNvcHlyaWdodCAoQykgMjAxMSBCcmlhbiBNY0tlbm5hIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL3JveS5zdmciLCJlbmdpbmUiOiJyZXBsYm94IiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwiYmFzaWNfYmV0YSI6eyJkaXNwbGF5TmFtZSI6IkJhc2ljIChiZXRhKSIsInRhZ2xpbmUiOiJBIGZ1biBhbmQgc2ltcGxlIHByb2dyYW1taW5nIGxhbmd1YWdlIGZvciBiZWdpbm5lcnMiLCJrZXkiOiJiYXNpY19iZXRhIiwiZW50cnlwb2ludCI6InByb2dyYW0uYmFzIiwiZXh0IjoiYmFzIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhlYWRlciI6InBnLWJhc2ljIHYwLjEgXG4oYykgMjAyMCBBbWphZCAmIEZhcmlzIE1hc2FkIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9pY29ucy0tdXRpbC5yZXBsLmNvL2Jhc2ljLnN2ZyIsImRvY3MiOiJodHRwczovL2RvY3MucmVwbC5pdC9taXNjL2Jhc2ljIiwiZW5naW5lIjoicmVwbGJveCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImNzaGFycF9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiQyMiLCJ0YWdsaW5lIjoiQSBNaWNyb3NvZnQgLk5FVCBwcm9ncmFtbWluZyBsYW5ndWFnZS4iLCJrZXkiOiJjc2hhcnBfYmV0YSIsImVudHJ5cG9pbnQiOiJtYWluLmNzIiwiZXh0IjoiY3MiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJNb25vIEMjIGNvbXBpbGVyIHZlcnNpb24gNi44LjAuMTIzIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2NzaGFycC5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImx1YV9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiTHVhIiwidGFnbGluZSI6IkEgbGlnaHR3ZWlnaHQgbXVsdGktcGFyYWRpZ20gc2NyaXB0aW5nIGxhbmd1YWdlLiIsImtleSI6Imx1YV9iZXRhIiwiZW50cnlwb2ludCI6Im1haW4ubHVhIiwiZXh0IjoibHVhIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjp0cnVlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6Ikx1YSA1LjEuNSIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9sdWEuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJjb2ZmZWVzY3JpcHRfYmV0YSI6eyJkaXNwbGF5TmFtZSI6IkNvZmZlZVNjcmlwdCIsInRhZ2xpbmUiOiJVbmZhbmN5IEphdmFTY3JpcHQuIiwia2V5IjoiY29mZmVlc2NyaXB0X2JldGEiLCJlbnRyeXBvaW50IjoibWFpbi5jb2ZmZWUiLCJleHQiOiJjb2ZmZWUiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOmZhbHNlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiQ29mZmVlU2NyaXB0IHYxLjEwXG5Db3B5cmlnaHQgKGMpIDIwMTYsIEplcmVteSBBc2hrZW5hcyIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Ii9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9jb2ZmZWVzY3JpcHQuc3ZnIiwiZW5naW5lIjoicmVwbGJveCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImxvdmUyZF9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiTG92ZTJEIiwidGFnbGluZSI6IkEgZnJlZSwgb3Blbi1zb3VyY2UgTHVhIGZyYW1ld29yayBmb3IgMkQgZ2FtZXMiLCJrZXkiOiJsb3ZlMmRfYmV0YSIsImVudHJ5cG9pbnQiOiJtYWluLmx1YSIsImV4dCI6Imx1YSIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IkxPVkUgMTEuMiAoTXlzdGVyaW91cyBNeXN0ZXJpZXMpIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9sYW5nLWltYWdlcy0tdGltbXktaS1jaGVuLnJlcGwuY28vbG92ZTJkLnBuZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwiamF2YXNjcmlwdF9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiSmF2YVNjcmlwdCIsInRhZ2xpbmUiOiJUaGUgZGUgZmFjdG8gbGFuZ3VhZ2Ugb2YgdGhlIFdlYi4iLCJrZXkiOiJqYXZhc2NyaXB0X2JldGEiLCJlbnRyeXBvaW50IjoibWFpbi5qcyIsImV4dCI6ImpzIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6Ik5hdGl2ZSBCcm93c2VyIEphdmFTY3JpcHQiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiIvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvamF2YXNjcmlwdC5zdmciLCJlbmdpbmUiOiJyZXBsYm94IiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwiYXBsX2JldGEiOnsiZGlzcGxheU5hbWUiOiJBUEwiLCJ0YWdsaW5lIjoiQW4gYXJyYXktb3JpZW50ZWQgbGFuZ3VhZ2UgdXNpbmcgZnVubnkgY2hhcmFjdGVycy4iLCJrZXkiOiJhcGxfYmV0YSIsImVudHJ5cG9pbnQiOiJtYWluLmFwbCIsImV4dCI6ImFwbCIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6ZmFsc2UsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJuZ24vYXBsIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2xhbmd1YWdlLnN2ZyIsImVuZ2luZSI6InJlcGxib3giLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJwaHBfY2xpX2JldGEiOnsiZGlzcGxheU5hbWUiOiJQSFAgQ0xJIiwidGFnbGluZSI6IkEgcG9wdWxhciBnZW5lcmFsLXB1cnBvc2Ugc2NyaXB0aW5nIGxhbmd1YWdlLiIsImtleSI6InBocF9jbGlfYmV0YSIsImVudHJ5cG9pbnQiOiJtYWluLnBocCIsImV4dCI6InBocCIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IlBIUCBDTEkgNy4yLjE3LTB1YnVudHUwLjE4LjA0LjEgKGNsaSkgKGJ1aWx0OiBBcHIgMTggMjAxOSAxNDoxMjozOCkgKCBOVFMgKVxuQ29weXJpZ2h0IChjKSAxOTk3LTIwMTggVGhlIFBIUCBHcm91cFxuWmVuZCBFbmdpbmUgdjMuMi4wLCBDb3B5cmlnaHQgKGMpIDE5OTgtMjAxOCBaZW5kIFRlY2hub2xvZ2llcyIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9waHAuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJweXhlbF9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiUHl4ZWwiLCJ0YWdsaW5lIjoiQSByZXRybyBnYW1lIGVuZ2luZSBmb3IgUHl0aG9uIiwia2V5IjoicHl4ZWxfYmV0YSIsImVudHJ5cG9pbnQiOiJtYWluLnB5IiwiZXh0IjoicHkiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IlB5dGhvbjMgd2l0aCBQeXhlbCIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9weXRob24uc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJqYXZhX3N3aW5nX2JldGEiOnsiZGlzcGxheU5hbWUiOiJKYXZhIFN3aW5nIiwidGFnbGluZSI6IkEgSmF2YSBHVUkgd2lkZ2V0IHRvb2xraXQiLCJrZXkiOiJqYXZhX3N3aW5nX2JldGEiLCJlbnRyeXBvaW50IjoiTWFpbi5qYXZhIiwiZXh0IjoiamF2YSIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IkphdmEgU3dpbmciLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvamF2YS5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInNjaGVtZV9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiU2NoZW1lIiwidGFnbGluZSI6IkFuIGVsZWdhbnQgZHluYW1pYyBkaWFsZWN0IG9mIExpc3AuIiwia2V5Ijoic2NoZW1lX2JldGEiLCJlbnRyeXBvaW50IjoibWFpbi5zY20iLCJleHQiOiJzY20iLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOmZhbHNlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiQml3YVNjaGVtZSBJbnRlcnByZXRlciB2ZXJzaW9uIDAuNi40XG5Db3B5cmlnaHQgKEMpIDIwMDctMjAxNCBZdXRha2EgSEFSQSBhbmQgdGhlIEJpd2FTY2hlbWUgdGVhbSIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Ii9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9zY2hlbWUuc3ZnIiwiZW5naW5lIjoicmVwbGJveCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImVtb3RpY29uX2JldGEiOnsiZGlzcGxheU5hbWUiOiJFbW90aWNvbiIsInRhZ2xpbmUiOiJQcm9ncmFtbWluZyB3aXRoIGFuIGV4dHJhIGRvc2Ugb2Ygc21pbGUuIiwia2V5IjoiZW1vdGljb25fYmV0YSIsImVudHJ5cG9pbnQiOiJtYWluLmVtb3RpY29uIiwiZXh0IjoiZW1vdGljb24iLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOmZhbHNlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiRW1vdGljb24gdjEuNSAoZW1vdGljb2ZmZWUpXG5Db3B5cmlnaHQgKGMpIDIwMTEgQW1qYWQgTWFzYWQiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiIvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvbGFuZ3VhZ2Uuc3ZnIiwiZW5naW5lIjoicmVwbGJveCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImVybGFuZ19iZXRhIjp7ImRpc3BsYXlOYW1lIjoiRXJsYW5nIiwidGFnbGluZSI6IkEgZ2VuZXJhbC1wdXJwb3NlLCBjb25jdXJyZW50LCBmdW5jdGlvbmFsIHByb2dyYW1taW5nIGxhbmd1YWdlIiwia2V5IjoiZXJsYW5nX2JldGEiLCJlbnRyeXBvaW50IjoibWFpbi5lcmwiLCJleHQiOiJlcmwiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJFcmxhbmcvT1RQIDIzLjAiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL2xhbmctaW1hZ2VzLS10aW1teS1pLWNoZW4ucmVwbC5jby9lcmxhbmcucG5nIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJzcWxpdGVfYmV0YSI6eyJkaXNwbGF5TmFtZSI6IlNRTGl0ZSIsInRhZ2xpbmUiOiJFbWJlZGRlZCBTUUwgZGF0YWJhc2UgZW5naW5lLiIsImtleSI6InNxbGl0ZV9iZXRhIiwiZW50cnlwb2ludCI6Im1haW4uc3FsIiwiZXh0Ijoic3FsIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOnRydWUsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiU1FMaXRlIHZlcnNpb24gMy4yMi4wIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9pY29ucy0tdXRpbC5yZXBsLmNvL3NxbGl0ZS5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInJ1c3RfYmV0YSI6eyJkaXNwbGF5TmFtZSI6IlJ1c3QiLCJ0YWdsaW5lIjoiQSBmYXN0IGFuZCBzYWZlIHN5c3RlbXMgcHJvZ3JhbW1pbmcgbGFuZ3VhZ2UuIiwia2V5IjoicnVzdF9iZXRhIiwiZW50cnlwb2ludCI6Im1haW4ucnMiLCJleHQiOiJycyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6InJ1c3RjIDEuNDQuMCAoNDljYWU1NTc2IDIwMjAtMDYtMDEpIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL3J1c3Quc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJjcnlzdGFsX2JldGEiOnsiZGlzcGxheU5hbWUiOiJDcnlzdGFsIiwidGFnbGluZSI6IkZhc3QgYXMgQywgc2xpY2sgYXMgUnVieSIsImtleSI6ImNyeXN0YWxfYmV0YSIsImVudHJ5cG9pbnQiOiJtYWluLmNyIiwiZXh0IjoiY3IiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJDcnlzdGFsIDAuMzQuMCBbNDQwMWU5MGYwXSAoMjAyMC0wNC0wNilcbkxMVk06IDguMC4wIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9sb2dvcy50dXJiaW8ucmVwbC5jby9jcnlzdGFsLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwicWJhc2ljX2JldGEiOnsiZGlzcGxheU5hbWUiOiJRQmFzaWMiLCJ0YWdsaW5lIjoiU3RydWN0dXJlZCBwcm9ncmFtbWluZyBmb3IgYmVnaW5uZXJzLiIsImtleSI6InFiYXNpY19iZXRhIiwiZW50cnlwb2ludCI6Im1haW4uYmFzIiwiZXh0IjoiYmFzIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IlFCYXNpYyAocWIuanMpXG5Db3B5cmlnaHQgKGMpIDIwMTAgU3RldmUgSGFub3YiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiIvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvbGFuZ3VhZ2Uuc3ZnIiwiZW5naW5lIjoicmVwbGJveCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImJsb29wX2JldGEiOnsiZGlzcGxheU5hbWUiOiJCbG9vcCIsInRhZ2xpbmUiOiJOb3RoaW5nIGJ1dCBib3VuZGVkIGxvb3BzLiIsImtleSI6ImJsb29wX2JldGEiLCJlbnRyeXBvaW50IjoibWFpbi5ibG9vcCIsImV4dCI6ImJsb29wIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IkJsb29QanNcbkNvcHlyaWdodCAoYykgMjAwNSBUaW0gQ2FtZXJvbiBSeWFuXG5CYXNlZCBvbiBQZXJsIGNvZGUgYnkgSm9obiBDb3dhbiwgMTk5NCIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Ii9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9sYW5ndWFnZS5zdmciLCJlbmdpbmUiOiJyZXBsYm94IiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwicG9seWdvdHRfYmV0YSI6eyJkaXNwbGF5TmFtZSI6InBvbHlnb3R0IiwidGFnbGluZSI6IkFuIGVsZWdhbnQgaW1hZ2UgZm9yIGEgbW9yZSBjaXZpbGl6ZWQgYWdlIiwia2V5IjoicG9seWdvdHRfYmV0YSIsImVudHJ5cG9pbnQiOiJNYWtlZmlsZSIsImV4dCI6ImdvdHQiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJQb2x5Z290dCIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9sYW5ndWFnZS5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInRjbF9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiVGNsIiwidGFnbGluZSI6IkEgaGlnaC1sZXZlbCBsYW5ndWFnZSBkZXNpZ25lZCB3aXRoIHRoZSBnb2FsIG9mIGJlaW5nIHZlcnkgc2ltcGxlIGJ1dCBwb3dlcmZ1bCIsImtleSI6InRjbF9iZXRhIiwiZW50cnlwb2ludCI6Im1haW4udGNsIiwiZXh0IjoidGNsIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOmZhbHNlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOnRydWUsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoidGNsc2ggOC42IiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9sb2dvcy50dXJiaW8ucmVwbC5jby90Y2wuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJrYWJvb21fYmV0YSI6eyJkaXNwbGF5TmFtZSI6IkthYm9vbSAoYmV0YSkiLCJ0YWdsaW5lIjoiS2Fib29tIEdhbWUgUHJvZ3JhbW1pbmcgRW52aXJvbm1lbnQiLCJrZXkiOiJrYWJvb21fYmV0YSIsImVudHJ5cG9pbnQiOiJzY2VuZXMvbWFpbi5qcyIsImV4dCI6ImpzIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Ii9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9rYWJvb20uc3ZnIiwiZW5naW5lIjoicmVwbGJveCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImRhcnRfYmV0YSI6eyJkaXNwbGF5TmFtZSI6IkRhcnQiLCJ0YWdsaW5lIjoiQSBnZW5lcmFsLXB1cnBvc2UgcHJvZ3JhbW1pbmcgbGFuZ3VhZ2UgdXNlZCB0byBidWlsZCB3ZWIsIHNlcnZlciwgZGVza3RvcCwgYW5kIG1vYmlsZSBhcHBsaWNhdGlvbnMuIiwia2V5IjoiZGFydF9iZXRhIiwiZW50cnlwb2ludCI6Im1haW4uZGFydCIsImV4dCI6ImRhcnQiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6dHJ1ZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IkRhcnQgVk0gdmVyc2lvbjogMi42LjAiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL2xvZ29zLnR1cmJpby5yZXBsLmNvL2RhcnQuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJ0a2ludGVyX2JldGEiOnsiZGlzcGxheU5hbWUiOiJUa2ludGVyIiwidGFnbGluZSI6IlB5dGhvbidzIHN0YW5kYXJkIEdVSSB0b29rbGl0Iiwia2V5IjoidGtpbnRlcl9iZXRhIiwiZW50cnlwb2ludCI6Im1haW4ucHkiLCJleHQiOiJweSIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjp0cnVlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiUHl0aG9uMy42IHdpdGggVGtpbnRlciIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9weXRob24uc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJ1bmxhbWJkYV9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiVW5sYW1iZGEiLCJ0YWdsaW5lIjoiRnVuY3Rpb25hbCBwdXJpdHkgZ2l2ZW4gZm9ybS4iLCJrZXkiOiJ1bmxhbWJkYV9iZXRhIiwiZW50cnlwb2ludCI6Im1haW4udW5sIiwiZXh0IjoidW5sIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IlVubGFtYmRhIHYyLjAgKHVubGFtYmRhLWNvZmZlZSlcbkNvcHlyaWdodCAoYykgMjAxMSBNYXggU2hhd2Fia2VoIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2xhbmd1YWdlLnN2ZyIsImVuZ2luZSI6InJlcGxib3giLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJjX2JldGEiOnsiZGlzcGxheU5hbWUiOiJDIiwidGFnbGluZSI6Ikxvdy1sZXZlbCBhbmQgY3Jvc3MtcGxhdGZvcm0gaW1wZXJhdGl2ZSBsYW5ndWFnZS4iLCJrZXkiOiJjX2JldGEiLCJlbnRyeXBvaW50IjoibWFpbi5jIiwiZXh0IjoiYyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOnRydWUsImhlYWRlciI6ImNsYW5nIHZlcnNpb24gNy4wLjAtM351YnVudHUwLjE4LjA0LjEgKHRhZ3MvUkVMRUFTRV83MDAvZmluYWwpIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2Muc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJyYWt1X2JldGEiOnsiZGlzcGxheU5hbWUiOiJSYWt1IiwidGFnbGluZSI6IkEgaGlnaGx5IGNhcGFibGUsIGZlYXR1cmUtcmljaCBwcm9ncmFtbWluZyBsYW5ndWFnZSBtYWRlIGZvciBhdCBsZWFzdCB0aGUgbmV4dCBodW5kcmVkIHllYXJzLiIsImtleSI6InJha3VfYmV0YSIsImVudHJ5cG9pbnQiOiJtYWluLnJha3UiLCJleHQiOiJyYWt1IiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOmZhbHNlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOmZhbHNlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IlRoaXMgaXMgUmFrdWRvIHZlcnNpb24gMjAyMC4wNiBidWlsdCBvbiBNb2FyVk0gdmVyc2lvbiAyMDIwLjA2IiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9sb2dvcy50dXJiaW8ucmVwbC5jby9wZXJsNi5wbmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInBocDdfYmV0YSI6eyJkaXNwbGF5TmFtZSI6IlBIUCBXZWIgU2VydmVyIiwidGFnbGluZSI6IkEgcG9wdWxhciBnZW5lcmFsLXB1cnBvc2Ugc2NyaXB0aW5nIGxhbmd1YWdlLiIsImtleSI6InBocDdfYmV0YSIsImVudHJ5cG9pbnQiOiJpbmRleC5waHAiLCJleHQiOiJwaHAiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6ZmFsc2UsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiUEhQIDcuMi4xNy0wdWJ1bnR1MC4xOC4wNC4xIChjbGkpIChidWlsdDogQXByIDE4IDIwMTkgMTQ6MTI6MzgpICggTlRTIClcbkNvcHlyaWdodCAoYykgMTk5Ny0yMDE4IFRoZSBQSFAgR3JvdXBcblplbmQgRW5naW5lIHYzLjIuMCwgQ29weXJpZ2h0IChjKSAxOTk4LTIwMTggWmVuZCBUZWNobm9sb2dpZXMiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvcGhwLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwia2Fib29tIjp7ImRpc3BsYXlOYW1lIjoiS2Fib29tIChiZXRhKSIsInRhZ2xpbmUiOiJLYWJvb20gR2FtZSBQcm9ncmFtbWluZyBFbnZpcm9ubWVudCIsImtleSI6ImthYm9vbSIsImVudHJ5cG9pbnQiOiJzY2VuZXMvbWFpbi5qcyIsImV4dCI6ImpzIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImNhdGVnb3J5IjoiR2FtZSBEZXZlbG9wbWVudCIsImljb24iOiIvcHVibGljL2ltYWdlcy9sYW5ndWFnZXMva2Fib29tLnN2ZyIsImVuZ2luZSI6InJlcGxib3giLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJnYXRzYnlqc19iZXRhIjp7ImRpc3BsYXlOYW1lIjoiR2F0c2J5SlMiLCJ0YWdsaW5lIjoiQmxhemluZy1mYXN0IHN0YXRpYyBzaXRlIGdlbmVyYXRvciBmb3IgUmVhY3QiLCJrZXkiOiJnYXRzYnlqc19iZXRhIiwiZW50cnlwb2ludCI6InNyYy9wYWdlcy9pbmRleC5qcyIsImV4dCI6ImpzIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6dHJ1ZSwiaGFzVVBNIjp0cnVlLCJoYXNHaXQiOmZhbHNlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiR2F0c2J5SlMgMS45LjI0Nywgbm9kZSB2OS43LjEgbGludXgvYW1kNjQiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL2xvZ29zLS10dXJiaW8ucmVwbC5jby9nYXRzYnlqcy5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInBocF9zZXJ2ZXJfYmV0YSI6eyJkaXNwbGF5TmFtZSI6IlBIUCBXZWIgU2VydmVyIiwidGFnbGluZSI6IkEgcG9wdWxhciBnZW5lcmFsLXB1cnBvc2Ugc2NyaXB0aW5nIGxhbmd1YWdlLiIsImtleSI6InBocF9zZXJ2ZXJfYmV0YSIsImVudHJ5cG9pbnQiOiJpbmRleC5waHAiLCJleHQiOiJwaHAiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJQSFAgV2ViIFNlcnZlciA3LjIuMTctMHVidW50dTAuMTguMDQuMSAoY2xpKSAoYnVpbHQ6IEFwciAxOCAyMDE5IDE0OjEyOjM4KSAoIE5UUyApXG5Db3B5cmlnaHQgKGMpIDE5OTctMjAxOCBUaGUgUEhQIEdyb3VwXG5aZW5kIEVuZ2luZSB2My4yLjAsIENvcHlyaWdodCAoYykgMTk5OC0yMDE4IFplbmQgVGVjaG5vbG9naWVzIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL3BocC5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImNwcDExX2JldGEiOnsiZGlzcGxheU5hbWUiOiJDKysxMSIsInRhZ2xpbmUiOiJBIGdlbmVyYWwgcHVycG9zZSBzeXN0ZW0gcHJvZ3JhbW1pbmcgbGFuZ3VhZ2UuIiwia2V5IjoiY3BwMTFfYmV0YSIsImVudHJ5cG9pbnQiOiJtYWluLmNwcCIsImV4dCI6ImNwcCIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJjbGFuZyB2ZXJzaW9uIDcuMC4wLTN+dWJ1bnR1MC4xOC4wNC4xICh0YWdzL1JFTEVBU0VfNzAwL2ZpbmFsKSIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9jcHAuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJiYWJlbF9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiRVM2IiwidGFnbGluZSI6Ik5leHQgZ2VuZXJhdGlvbiBKYXZhU2NyaXB0LiIsImtleSI6ImJhYmVsX2JldGEiLCJlbnRyeXBvaW50IjoibWFpbi5qcyIsImV4dCI6ImpzIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6ZmFsc2UsImhhc1Byb2plY3RNb2RlIjpmYWxzZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IkJhYmVsIENvbXBpbGVyIHY2LjQuNFxuQ29weXJpZ2h0IChjKSAyMDE0LTIwMTUgU2ViYXN0aWFuIE1jS2VuemllIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2phdmFzY3JpcHQuc3ZnIiwiZW5naW5lIjoicmVwbGJveCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInJlYXNvbl9ub2RlanNfYmV0YSI6eyJkaXNwbGF5TmFtZSI6IlJlYXNvbiBOb2RlLmpzIiwidGFnbGluZSI6IlJlYXNvbiBjb21waWxpbmcgdG8gTm9kZS5qcyAodmlhIEJ1Y2tsZVNjcmlwdCkiLCJrZXkiOiJyZWFzb25fbm9kZWpzX2JldGEiLCJlbnRyeXBvaW50Ijoic3JjL01haW4ucmUiLCJleHQiOiJyZSIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOnRydWUsImhhc1VQTSI6dHJ1ZSwiaGFzR2l0IjpmYWxzZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IlJlYXNvbiAzLjMuNCwgQnVja2xlc2NyaXB0IDQuMC4xOCwgTm9kZSB2MTAuMTUuMiBsaW51eC9hbWQ2NCIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9yZWFzb24ucG5nIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJyZWFjdGpzX2JldGEiOnsiZGlzcGxheU5hbWUiOiJSZWFjdCIsInRhZ2xpbmUiOiJBIEphdmFTY3JpcHQgbGlicmFyeSBmb3IgYnVpbGRpbmcgdXNlciBpbnRlcmZhY2VzIiwia2V5IjoicmVhY3Rqc19iZXRhIiwiZW50cnlwb2ludCI6InNyYy9BcHAuanMiLCJleHQiOiJqcyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOnRydWUsImhhc1VQTSI6dHJ1ZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiUmVhY3QgMTYuOC4yLCBub2RlIHYxMC4xIGxpbnV4L2FtZDY0IiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL3JlYWN0LnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwicmFpbHNfYmV0YSI6eyJkaXNwbGF5TmFtZSI6IlJ1Ynkgb24gUmFpbHMiLCJ0YWdsaW5lIjoiQSB3ZWItYXBwbGljYXRpb24gZnJhbWV3b3JrIHRoYXQgaW5jbHVkZXMgZXZlcnl0aGluZyBuZWVkZWQgdG8gY3JlYXRlIHdlYiBhcHBsaWNhdGlvbnMiLCJrZXkiOiJyYWlsc19iZXRhIiwiZW50cnlwb2ludCI6ImNvbmZpZy9yb3V0ZXMucmIiLCJleHQiOiJyYiIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOnRydWUsImhhc1VQTSI6dHJ1ZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6InJ1YnkgMi41LjBwMCAoMjAxNy0xMi0yNSByZXZpc2lvbiA2MTQ2OCkgW3g4Nl82NC1saW51eF0iLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvcmFpbHMuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJweXRob24zX2NsYXNzcm9vbV9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiUHl0aG9uIiwidGFnbGluZSI6IkEgZHluYW1pYyBsYW5ndWFnZSBlbXBoYXNpemluZyByZWFkYWJpbGl0eS4iLCJrZXkiOiJweXRob24zX2NsYXNzcm9vbV9iZXRhIiwiZW50cnlwb2ludCI6Im1haW4ucHkiLCJleHQiOiJweSIsImhhc0xpbnQiOnRydWUsImhhc1VuaXRUZXN0cyI6dHJ1ZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjp0cnVlLCJoYXNVUE0iOnRydWUsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6dHJ1ZSwiaGFzSW50ZXJwcmV0ZXIiOnRydWUsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJQeXRob24gMy44LjEgKGRlZmF1bHQsIEZlYiAgMiAyMDIwLCAwODozNzozNykiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvcHl0aG9uLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwicmVhc29uX2JldGEiOnsiZGlzcGxheU5hbWUiOiJSZWFzb24iLCJ0YWdsaW5lIjoiQSBuZXcgc3ludGF4IGZvciBPQ2FtbCB0aGF0IGlzIHJlbW5pc2NpZW50IG9mIGxhbmd1YWdlcyBsaWtlIEphdmFTY3JpcHQiLCJrZXkiOiJyZWFzb25fYmV0YSIsImVudHJ5cG9pbnQiOiJtYWluLnJlIiwiZXh0IjoicmUiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0IjpmYWxzZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IlJlYXNvbiAzLjQuMCAoT0NhbWwgdjQuMDcuMSkgbGludXgvYW1kNjQiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvcmVhc29uLnBuZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwiamF2YV9tYXZlbl9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiSmF2YSAod2l0aCBNYXZlbikiLCJ0YWdsaW5lIjoiQSBjb25jdXJyZW50LCBjbGFzcy1iYXNlZCwgc3RhdGljYWxseSB0eXBlZCBvYmplY3Qtb3JpZW50ZWQgbGFuZ3VhZ2UuIiwia2V5IjoiamF2YV9tYXZlbl9iZXRhIiwiZW50cnlwb2ludCI6Ik1haW4uamF2YSIsImV4dCI6ImphdmEiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6dHJ1ZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiT3BlbkpESyBSdW50aW1lIEVudmlyb25tZW50IChidWlsZCAxMC4wLjIrMTMtVWJ1bnR1LTF1YnVudHUwLjE4LjA0LjQpIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2phdmEuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJwaHBfYmV0YSI6eyJkaXNwbGF5TmFtZSI6IlBIUCAoTGVnYWN5KSIsInRhZ2xpbmUiOiJBIHBvcHVsYXIgZ2VuZXJhbC1wdXJwb3NlIHNjcmlwdGluZyBsYW5ndWFnZS4iLCJrZXkiOiJwaHBfYmV0YSIsImVudHJ5cG9pbnQiOiJtYWluLnBocCIsImV4dCI6InBocCIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6ZmFsc2UsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6dHJ1ZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IlBIUCA3LjAuOCAoTGVnYWN5OiB1c2UgdGhlIGZvbGxvd2luZyBmb3IgbmV3IGZlYXR1cmVzOlxuQ29tbWFuZC1saW5lIFBIUDogaHR0cHM6Ly9yZXBsaXQuY29tL2xhbmd1YWdlcy9waHBfY2xpXG5QSFAgV2ViIFNlcnZlcjogaHR0cHM6Ly9yZXBsaXQuY29tL2xhbmd1YWdlcy9waHA3IiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL3BocC5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInJlYWN0dHNfYmV0YSI6eyJkaXNwbGF5TmFtZSI6IlJlYWN0IFR5cGVzY3JpcHQiLCJ0YWdsaW5lIjoiQSBKYXZhU2NyaXB0IGxpYnJhcnkgZm9yIGJ1aWxkaW5nIHVzZXIgaW50ZXJmYWNlcyIsImtleSI6InJlYWN0dHNfYmV0YSIsImVudHJ5cG9pbnQiOiJzcmMvQXBwLnRzeCIsImV4dCI6InRzeCIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOnRydWUsImhhc1VQTSI6dHJ1ZSwiaGFzR2l0IjpmYWxzZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IlJlYWN0IDE2LjguMiwgbm9kZSB2OS43LjEgbGludXgvYW1kNjQiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvcmVhY3Quc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJzdGF0aWNfYmV0YSI6eyJkaXNwbGF5TmFtZSI6IlN0YXRpYyIsInRhZ2xpbmUiOiJBIGJhc2UgbGFuZ3VhZ2UgZm9yIGNsaWVudCBzaWRlIGxhbmd1YWdlcyIsImtleSI6InN0YXRpY19iZXRhIiwiZW50cnlwb2ludCI6Ik1ha2VmaWxlIiwiZXh0IjoiaHRtbCIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6ZmFsc2UsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvbGFuZ3VhZ2Uuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJuZXh0anNfYmV0YSI6eyJkaXNwbGF5TmFtZSI6Ik5leHQuanMiLCJ0YWdsaW5lIjoiQSBsaWdodHdlaWdodCBmcmFtZXdvcmsgZm9yIHN0YXRpYyBhbmQgc2VydmVyXHUyMDExcmVuZGVyZWQgUmVhY3QgYXBwbGljYXRpb25zIiwia2V5IjoibmV4dGpzX2JldGEiLCJlbnRyeXBvaW50IjoicGFnZXMvaW5kZXguanMiLCJleHQiOiJqcyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOnRydWUsImhhc1VQTSI6dHJ1ZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6dHJ1ZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiTmV4dC5qcyA2LjAuMywgbm9kZSB2MTIuMTMuMCBsaW51eC9hbWQ2NCIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9ub2RlanMuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJleHByZXNzX2JldGEiOnsiZGlzcGxheU5hbWUiOiJFeHByZXNzIiwidGFnbGluZSI6IkphdmFTY3JpcHQgZnJhbWV3b3JrIGRlc2lnbmVkIGZvciBidWlsZGluZyB3ZWIgYXBwbGljYXRpb25zIGFuZCBBUElzLiIsImtleSI6ImV4cHJlc3NfYmV0YSIsImVudHJ5cG9pbnQiOiJpbmRleC5qcyIsImV4dCI6ImpzIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6dHJ1ZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjp0cnVlLCJoYXNVUE0iOnRydWUsImhhc0dpdCI6ZmFsc2UsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoibm9kZSB2OS43LjEgbGludXgvYW1kNjQiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvZXhwcmVzcy5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sIm9jYW1sX2JldGEiOnsiZGlzcGxheU5hbWUiOiJPQ2FtbCIsInRhZ2xpbmUiOiJPQ2FtbCBpcyBhIGdlbmVyYWwgcHVycG9zZSBwcm9ncmFtbWluZyBsYW5ndWFnZSB3aXRoIGFuIGVtcGhhc2lzIG9uIGV4cHJlc3NpdmVuZXNzIGFuZCBzYWZldHkiLCJrZXkiOiJvY2FtbF9iZXRhIiwiZW50cnlwb2ludCI6Im1haW4ubWwiLCJleHQiOiJtbCIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOmZhbHNlLCJoYXNVUE0iOmZhbHNlLCJoYXNHaXQiOmZhbHNlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOnRydWUsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJPQ2FtbCB2NC4wNy4xIGxpbnV4L2FtZDY0IiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9vcGFtLm9jYW1sLm9yZy9leHQvaW1nL29jYW1sLnBuZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwiZGphbmdvX2JldGEiOnsiZGlzcGxheU5hbWUiOiJEamFuZ28iLCJ0YWdsaW5lIjoiUHl0aG9uIGZyYW1ld29yayB0aGF0IGVuY291cmFnZXMgcmFwaWQgZGV2ZWxvcG1lbnQuIiwia2V5IjoiZGphbmdvX2JldGEiLCJlbnRyeXBvaW50IjoibWFpbi92aWV3cy5weSIsImV4dCI6InB5IiwiaGFzTGludCI6dHJ1ZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjp0cnVlLCJoYXNVUE0iOnRydWUsImhhc0dpdCI6ZmFsc2UsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJQeXRob24gMy42LjEgKGRlZmF1bHQsIEp1biAyMSAyMDE3LCAxODo0ODozNSlcbltHQ0MgNC45LjJdIG9uIGxpbnV4IiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2RqYW5nby5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInJ1YnlfY2xhc3Nyb29tX2JldGEiOnsiZGlzcGxheU5hbWUiOiJSdWJ5IiwidGFnbGluZSI6IkEgbmF0dXJhbCBkeW5hbWljIG9iamVjdC1vcmllbnRlZCBsYW5ndWFnZS4iLCJrZXkiOiJydWJ5X2NsYXNzcm9vbV9iZXRhIiwiZW50cnlwb2ludCI6Im1haW4ucmIiLCJleHQiOiJyYiIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOnRydWUsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6dHJ1ZSwiaGFzVVBNIjp0cnVlLCJoYXNHaXQiOnRydWUsImhhc0V2YWwiOnRydWUsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6InJ1YnkgMi41LjVwMTU3ICgyMDE5LTAzLTE1IHJldmlzaW9uIDY3MjYwKSBbeDg2XzY0LWxpbnV4XSIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9ydWJ5LnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwiamVzdF9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiSmVzdCIsInRhZ2xpbmUiOiJQYWlubGVzcyBKYXZhU2NyaXB0IFRlc3RpbmcuIiwia2V5IjoiamVzdF9iZXRhIiwiZW50cnlwb2ludCI6ImNvbmZpZy5qc29uIiwiZXh0IjoianMiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6ZmFsc2UsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiSmVzdCB2MjQuOS4wIG5vZGUgdjEwLjE2LjMgbGludXgvYW1kNjQiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvamVzdC5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInBlcmw2X2JldGEiOnsiZGlzcGxheU5hbWUiOiJQZXJsIDYiLCJ0YWdsaW5lIjoiYSBoaWdobHkgY2FwYWJsZSwgZmVhdHVyZS1yaWNoIHByb2dyYW1taW5nIGxhbmd1YWdlIG1hZGUgZm9yIGF0IGxlYXN0IHRoZSBuZXh0IGh1bmRyZWQgeWVhcnMuIiwia2V5IjoicGVybDZfYmV0YSIsImVudHJ5cG9pbnQiOiJtYWluLnA2IiwiZXh0IjoicDYiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6ZmFsc2UsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjpmYWxzZSwiaGFzREFQIjpmYWxzZSwiaGVhZGVyIjoiVGhpcyBpcyBSYWt1ZG8gdmVyc2lvbiAyMDIwLjA1LjEgYnVpbHQgb24gTW9hclZNIHZlcnNpb24gMjAyMC4wNSIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vbG9nb3MudHVyYmlvLnJlcGwuY28vcGVybDYucG5nIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJqYXZhX2JldGEiOnsiZGlzcGxheU5hbWUiOiJKYXZhIiwidGFnbGluZSI6IkEgY29uY3VycmVudCwgY2xhc3MtYmFzZWQsIHN0YXRpY2FsbHkgdHlwZWQgb2JqZWN0LW9yaWVudGVkIGxhbmd1YWdlLiIsImtleSI6ImphdmFfYmV0YSIsImVudHJ5cG9pbnQiOiJNYWluLmphdmEiLCJleHQiOiJqYXZhIiwiaGFzTGludCI6ZmFsc2UsImhhc1VuaXRUZXN0cyI6dHJ1ZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6ZmFsc2UsImhhc0V2YWwiOmZhbHNlLCJoYXNJbnRlcnByZXRlciI6ZmFsc2UsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJqYXZhIHZlcnNpb24gXCIxLjguMF8zMVwiXG5KYXZhKFRNKSBTRSBSdW50aW1lIEVudmlyb25tZW50IChidWlsZCAxLjguMF8zMS1iMTMpXG5KYXZhIEhvdFNwb3QoVE0pIDY0LUJpdCBTZXJ2ZXIgVk0gKGJ1aWxkIDI1LjMxLWIwNywgbWl4ZWQgbW9kZSkiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvamF2YS5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInNpbmF0cmFfYmV0YSI6eyJkaXNwbGF5TmFtZSI6IlNpbmF0cmEiLCJ0YWdsaW5lIjoiRFNMIGZvciBxdWlja2x5IGNyZWF0aW5nIHdlYiBhcHBsaWNhdGlvbnMgaW4gUnVieSB3aXRoIG1pbmltYWwgZWZmb3J0Iiwia2V5Ijoic2luYXRyYV9iZXRhIiwiZW50cnlwb2ludCI6Im1haW4ucmIiLCJleHQiOiJyYiIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOnRydWUsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6dHJ1ZSwiaGFzVVBNIjp0cnVlLCJoYXNHaXQiOmZhbHNlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOmZhbHNlLCJoYXNMYW5ndWFnZVNlcnZlciI6ZmFsc2UsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6InJ1YnkgMi41LjBwMCAoMjAxNy0xMi0yNSByZXZpc2lvbiA2MTQ2OCkgW3g4Nl82NC1saW51eF0iLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvc2luYXRyYS5wbmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInJlYWN0cmVfYmV0YSI6eyJkaXNwbGF5TmFtZSI6IlJlYWN0IFJlYXNvbiIsInRhZ2xpbmUiOiJSZWFzb24gYmluZGluZ3MgZm9yIFJlYWN0SlMiLCJrZXkiOiJyZWFjdHJlX2JldGEiLCJlbnRyeXBvaW50Ijoic3JjL2luZGV4LnJlIiwiZXh0IjoicmUiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0IjpmYWxzZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IlJlYXNvbiAzLjEuNSwgbm9kZSB2OS43LjEgbGludXgvYW1kNjQiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL2xvZ29zLS10dXJiaW8ucmVwbC5jby9yZWFjdHJlLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwicmlkZGxlanNfYmV0YSI6eyJkaXNwbGF5TmFtZSI6Ik5vZGUuanM/IiwidGFnbGluZSI6ImhtbW1tbT8iLCJrZXkiOiJyaWRkbGVqc19iZXRhIiwiZW50cnlwb2ludCI6ImluZGV4LmpzIiwiZXh0IjoianMiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjp0cnVlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOnRydWUsImhhc1VQTSI6dHJ1ZSwiaGFzR2l0IjpmYWxzZSwiaGFzRXZhbCI6dHJ1ZSwiaGFzSW50ZXJwcmV0ZXIiOnRydWUsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJub2RlPz8/IHYxMC4xNi4wPyIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vcmVwbGl0LmNvbS9wdWJsaWMvaW1hZ2VzL2xhbmd1YWdlcy9ub2RlanMuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJmbG93X2JldGEiOnsiZGlzcGxheU5hbWUiOiJGbG93IiwidGFnbGluZSI6IkEgc3RhdGljIHR5cGUgY2hlY2tlciBmb3IgSmF2YVNjcmlwdCIsImtleSI6ImZsb3dfYmV0YSIsImVudHJ5cG9pbnQiOiJzcmMvaW5kZXguanMiLCJleHQiOiJqcyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0Ijp0cnVlLCJoYXNMaWJyYXJpZXMiOnRydWUsImhhc1VQTSI6dHJ1ZSwiaGFzR2l0IjpmYWxzZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6Im5vZGUgdjkuNy4xIGxpbnV4L2FtZDY0IiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2Zsb3cuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJ3YXNtX2JldGEiOnsiZGlzcGxheU5hbWUiOiJXZWJBc3NlbWJseSIsInRhZ2xpbmUiOiJBIGluc3RydWN0aW9uIGZvcm1hdCBmb3IgYSBzdGFjay1iYXNlZCB2aXJ0dWFsIG1hY2hpbmUiLCJrZXkiOiJ3YXNtX2JldGEiLCJlbnRyeXBvaW50IjoibWFpbi53YXQiLCJleHQiOiJ3YXQiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJ3YXNtZXIgdjAuOC4wIGxpbnV4IiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9pY29ucy51dGlsLnJlcGwuY28vd2FzbS5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sImVuenltZV9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiRW56eW1lIiwidGFnbGluZSI6IkEgSmF2YVNjcmlwdCBUZXN0aW5nIHV0aWxpdHkgZm9yIFJlYWN0Iiwia2V5IjoiZW56eW1lX2JldGEiLCJlbnRyeXBvaW50IjoiaW5kZXguanMiLCJleHQiOiJqcyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOmZhbHNlLCJoYXNQcm9qZWN0TW9kZSI6ZmFsc2UsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6ZmFsc2UsImhhc0V2YWwiOnRydWUsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJub2RlIHY3LjQgbGludXgvYW1kNjQiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvcmVhY3Quc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJuaXhfYmV0YSI6eyJkaXNwbGF5TmFtZSI6Ik5peCAoYmV0YSkiLCJ0YWdsaW5lIjoiQSBiYXNlIHJlcGwgZm9yIGJ1aWxkaW5nIGFueXRoaW5nIHlvdSB3YW50IGluIGFueSBsYW5ndWFnZS4iLCJrZXkiOiJuaXhfYmV0YSIsImVudHJ5cG9pbnQiOiIucmVwbGl0IiwiZXh0Ijoic2giLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6ZmFsc2UsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL2ljb25zLnV0aWwucmVwbC5jby9iYXNoLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwibm9kZWpzX3ByeWJhcl9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiTm9kZS5qcyIsInRhZ2xpbmUiOiJFdmVudGVkIEkvTyBmb3IgVjggSmF2YVNjcmlwdC4iLCJrZXkiOiJub2RlanNfcHJ5YmFyX2JldGEiLCJlbnRyeXBvaW50IjoiaW5kZXguanMiLCJleHQiOiJqcyIsImhhc0xpbnQiOmZhbHNlLCJoYXNVbml0VGVzdHMiOnRydWUsImhhc1Byb2plY3RNb2RlIjp0cnVlLCJoYXNGb3JtYXQiOnRydWUsImhhc0xpYnJhcmllcyI6dHJ1ZSwiaGFzVVBNIjp0cnVlLCJoYXNHaXQiOmZhbHNlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOnRydWUsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJub2RlIHYxMC4xNS4yIGxpbnV4L2FtZDY0IiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL25vZGVqcy5zdmciLCJlbmdpbmUiOiJnb3ZhbCIsImlzTmV3IjpmYWxzZSwiY29uZmlnIjp7ImlzU2VydmVyIjpmYWxzZSwiaXNWbmMiOmZhbHNlfX0sInJlYWN0X25hdGl2ZV9iZXRhIjp7ImRpc3BsYXlOYW1lIjoiUmVhY3QgTmF0aXZlIiwidGFnbGluZSI6IkNyZWF0ZSBtb2JpbGUgYXBwcyB3aXRoIFJlYWN0IE5hdGl2ZSBhbmQgRXhwbyIsImtleSI6InJlYWN0X25hdGl2ZV9iZXRhIiwiZW50cnlwb2ludCI6ImluZGV4LmpzIiwiZXh0IjoianMiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjp0cnVlLCJoYXNQcm9qZWN0TW9kZSI6dHJ1ZSwiaGFzRm9ybWF0IjpmYWxzZSwiaGFzTGlicmFyaWVzIjpmYWxzZSwiaGFzVVBNIjpmYWxzZSwiaGFzR2l0IjpmYWxzZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOmZhbHNlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJSZWFjdCBOYXRpdmUiLCJjYXRlZ29yeSI6IkhpZGRlbiIsImljb24iOiJodHRwczovL3JlcGxpdC5jb20vcHVibGljL2ltYWdlcy9sYW5ndWFnZXMvcmVhY3Quc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19LCJnYXRzYnlqc3YyX2JldGEiOnsiZGlzcGxheU5hbWUiOiJHYXRzYnlKUyAyLjAiLCJ0YWdsaW5lIjoiQmxhemluZy1mYXN0IHN0YXRpYyBzaXRlIGdlbmVyYXRvciBmb3IgUmVhY3QiLCJrZXkiOiJnYXRzYnlqc3YyX2JldGEiLCJlbnRyeXBvaW50Ijoic3JjL3BhZ2VzL2luZGV4LmpzIiwiZXh0IjoianMiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6dHJ1ZSwiaGFzTGlicmFyaWVzIjp0cnVlLCJoYXNVUE0iOnRydWUsImhhc0dpdCI6dHJ1ZSwiaGFzRXZhbCI6ZmFsc2UsImhhc0ludGVycHJldGVyIjpmYWxzZSwiaGFzTGFuZ3VhZ2VTZXJ2ZXIiOnRydWUsImhhc0RBUCI6ZmFsc2UsImhlYWRlciI6IkdhdHNieUpTIDIuMCIsImNhdGVnb3J5IjoiSGlkZGVuIiwiaWNvbiI6Imh0dHBzOi8vbG9nb3MtLXR1cmJpby5yZXBsLmNvL2dhdHNieWpzLnN2ZyIsImVuZ2luZSI6ImdvdmFsIiwiaXNOZXciOmZhbHNlLCJjb25maWciOnsiaXNTZXJ2ZXIiOmZhbHNlLCJpc1ZuYyI6ZmFsc2V9fSwibm9kZWpzX3N0YXRpY19iZXRhIjp7ImRpc3BsYXlOYW1lIjoibm9kZWpzIHN0YXR1YzogdGhpcyBpcyBqdXN0IGEgdGVzdC4uLiBwbHMgZG9uJ3QgdXNlIiwidGFnbGluZSI6ImF6YWFhYWFhYWFhYWFhYWFhYWFhYWFhIiwia2V5Ijoibm9kZWpzX3N0YXRpY19iZXRhIiwiZW50cnlwb2ludCI6ImluZGV4LmpzIiwiZXh0IjoianMiLCJoYXNMaW50IjpmYWxzZSwiaGFzVW5pdFRlc3RzIjpmYWxzZSwiaGFzUHJvamVjdE1vZGUiOnRydWUsImhhc0Zvcm1hdCI6ZmFsc2UsImhhc0xpYnJhcmllcyI6ZmFsc2UsImhhc1VQTSI6dHJ1ZSwiaGFzR2l0Ijp0cnVlLCJoYXNFdmFsIjpmYWxzZSwiaGFzSW50ZXJwcmV0ZXIiOnRydWUsImhhc0xhbmd1YWdlU2VydmVyIjp0cnVlLCJoYXNEQVAiOmZhbHNlLCJoZWFkZXIiOiJub2RlIHYxMC4xNi4wIiwiY2F0ZWdvcnkiOiJIaWRkZW4iLCJpY29uIjoiaHR0cHM6Ly9yZXBsaXQuY29tL3B1YmxpYy9pbWFnZXMvbGFuZ3VhZ2VzL2phdmFzY3JpcHQuc3ZnIiwiZW5naW5lIjoiZ292YWwiLCJpc05ldyI6ZmFsc2UsImNvbmZpZyI6eyJpc1NlcnZlciI6ZmFsc2UsImlzVm5jIjpmYWxzZX19fQ=='))</script><script type="text/javascript">CLIENT_IP = JSON.parse(atob('IjgwLjIzNC43Mi4xNjAi'))</script><script>
              !function() {var analytics = window.analytics = window.analytics || [];if (!analytics.initialize)if (analytics.invoked) window.console && console.error && console.error("Segment snippet included twice.");else {analytics.invoked = !0;analytics.methods = ["trackSubmit", "trackClick", "trackLink", "trackForm", "pageview", "identify", "reset", "group", "track", "ready", "alias", "debug", "page", "once", "off", "on"];analytics.factory = function(e) {return function() {var t = Array.prototype.slice.call(arguments);t.unshift(e);analytics.push(t);return analytics}};for (var e = 0; e < analytics.methods.length; e++) {var key = analytics.methods[e];analytics[key] = analytics.factory(key)}analytics.load = function(key, e) {var t = document.createElement("script");t.type = "text/javascript";t.async = !0;t.src = "https://sp.replit.com/sdk.js/v1/" + key + "/sdk.min.js";var n = document.getElementsByTagName("script")[0];n.parentNode.insertBefore(t, n);analytics._loadOptions = e};analytics.SNIPPET_VERSION = "4.15.3";
                  analytics.load('dMePKGC4BqfBivpe0Hvl8IoPpzSHgjdX', {integrations: {'Segment.io': { apiHost: 'sp.replit.com/v1' }}});
              }}();</script><script>
    (function (isTouchDevice) {
      if (!isTouchDevice) return;
      var isTouchClass = 'is-touch-device';
      var docElement = document.documentElement;
      docElement.className = docElement.className ? [docElement.className, isTouchClass].join(' ') : isTouchClass;
    })(('ontouchstart' in window) || window.DocumentTouch && document instanceof DocumentTouch);
            </script><script async="" src="./tren_files/saved_resource"></script><link rel="preload" href="./tren_files/77b7f3004e062aed.css" as="style"><link rel="stylesheet" href="./tren_files/77b7f3004e062aed.css" data-n-g=""><noscript data-n-css=""></noscript><style data-n-href="https://cdn.replit.com/_next/static/css/57e552a359783ea8.css">.keen-slider{display:flex;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-touch-callout:none;-khtml-user-select:none;touch-action:pan-y;-webkit-tap-highlight-color:transparent}.keen-slider,.keen-slider__slide{overflow:hidden;position:relative}.keen-slider__slide{width:100%;min-height:100%}.keen-slider[data-keen-slider-v]{flex-wrap:wrap}.keen-slider[data-keen-slider-v] .keen-slider__slide{width:100%}.keen-slider[data-keen-slider-moves] *{pointer-events:none}
/*# sourceMappingURL=57e552a359783ea8.css.map*/</style><script defer="" nomodule="" src="./tren_files/polyfills-5cd94c89d3acac5f.js"></script><script src="./tren_files/webpack-461c4825d7415197.js" defer=""></script><script src="./tren_files/framework-2ff0b62030a2cbdb.js" defer=""></script><script src="./tren_files/main-665a7dc0d65cde62.js" defer=""></script><script src="./tren_files/_app-4a608e8217300bf4.js" defer=""></script><script src="./tren_files/4ad82c5e-ef378423eddd5184.js" defer=""></script><script src="./tren_files/fbb05e6d-1df1e71d761da6ad.js" defer=""></script><script src="./tren_files/7848-b6f8218a8b3a6658.js" defer=""></script><script src="./tren_files/6764-353388d9b36b9c69.js" defer=""></script><script src="./tren_files/new-ccf702ab29fe9e29.js" defer=""></script><script src="./tren_files/_buildManifest.js" defer=""></script><script src="./tren_files/_ssgManifest.js" defer=""></script><script src="./tren_files/_middlewareManifest.js" defer=""></script><style id="__jsx-af55e82ad7f8389a">*{margin:0;padding:0;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}:root{--column-number:12}@media screen and (max-width:768px){:root{--column-number:8}}@media screen and (max-width:480px){:root{--column-number:4}}html,body{min-height:100%}body{background-color:var(--background-root);font-family:var(--font-family-default);font-size:var(--font-size-default);color:var(--foreground-default);--interactive-background:var(--background-default);--interactive-background--active:var(--background-higher);--interactive-border:var(--outline-dimmer);--interactive-border--hover:var(--outline-default)}button{font-family:inherit;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}input{font-family:inherit}a{font-family:inherit;cursor:pointer;text-decoration:none;color:var(--accent-primary-stronger)}ul{list-style:none}table{border-collapse:collapse;border-spacing:0}</style><style id="__jsx-24bb9f919596b067">[aria-label][role~="tooltip"]{position:relative;font-family:var(--font-family-default)}[aria-label][role~="tooltip"]::before,[aria-label][role~="tooltip"]::after{-webkit-transform:translate3d(0,0,0);-moz-transform:translate3d(0,0,0);transform:translate3d(0,0,0);-webkit-backface-visibility:hidden;-moz-backface-visibility:hidden;backface-visibility:hidden;will-change:transform;opacity:0;pointer-events:none;-webkit-transition:all var(--microtip-transition-duration,.18s)var(--microtip-transition-easing,ease-in-out)var(--microtip-transition-delay,0s);-moz-transition:all var(--microtip-transition-duration,.18s)var(--microtip-transition-easing,ease-in-out)var(--microtip-transition-delay,0s);-o-transition:all var(--microtip-transition-duration,.18s)var(--microtip-transition-easing,ease-in-out)var(--microtip-transition-delay,0s);transition:all var(--microtip-transition-duration,.18s)var(--microtip-transition-easing,ease-in-out)var(--microtip-transition-delay,0s);position:absolute;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;z-index:10;-webkit-transform-origin:top;-moz-transform-origin:top;-ms-transform-origin:top;-o-transform-origin:top;transform-origin:top}[aria-label][role~="tooltip"]::before{-webkit-background-size:100%auto!important;-moz-background-size:100%auto!important;-o-background-size:100%auto!important;background-size:100%auto!important;content:""}[aria-label][role~="tooltip"]::after{background:var(--background-highest);border:1px solid var(--outline-dimmest);color:var(--foreground-default);-webkit-box-shadow:var(--shadow-1);-moz-box-shadow:var(--shadow-1);box-shadow:var(--shadow-1);-webkit-border-radius:var(--border-radius-8);-moz-border-radius:var(--border-radius-8);border-radius:var(--border-radius-8);content:attr(aria-label);line-height:var(--line-height-default);font-size:var(--font-size-default);padding:var(--space-4)var(--space-8);white-space:nowrap;-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box}[aria-label][role~="tooltip"]:hover::before,[aria-label][role~="tooltip"]:hover::after,[aria-label][role~="tooltip"]:focus::before,[aria-label][role~="tooltip"]:focus::after{opacity:1;pointer-events:auto}[role~="tooltip"][data-microtip-position|="top"]::after{margin-bottom:8px}[role~="tooltip"][data-microtip-position|="top"]::before{-webkit-transform:translate3d(-50%,0,0);-moz-transform:translate3d(-50%,0,0);transform:translate3d(-50%,0,0);bottom:100%;left:50%}[role~="tooltip"][data-microtip-position|="top"]:hover::before{-webkit-transform:translate3d(-50%,-5px,0);-moz-transform:translate3d(-50%,-5px,0);transform:translate3d(-50%,-5px,0)}[role~="tooltip"][data-microtip-position|="top"]::after{-webkit-transform:translate3d(-50%,0,0);-moz-transform:translate3d(-50%,0,0);transform:translate3d(-50%,0,0);bottom:100%;left:50%}[role~="tooltip"][data-microtip-position="top"]:hover::after{-webkit-transform:translate3d(-50%,-5px,0);-moz-transform:translate3d(-50%,-5px,0);transform:translate3d(-50%,-5px,0)}[role~="tooltip"][data-microtip-position="top-left"]::after{-webkit-transform:translate3d(-webkit-calc(-100% + 16px),0,0);-moz-transform:translate3d(-moz-calc(-100% + 16px),0,0);transform:translate3d(-webkit-calc(-100% + 16px),0,0);transform:translate3d(-moz-calc(-100% + 16px),0,0);transform:translate3d(calc(-100% + 16px),0,0);bottom:100%}[role~="tooltip"][data-microtip-position="top-left"]:hover::after{-webkit-transform:translate3d(-webkit-calc(-100% + 16px),-5px,0);-moz-transform:translate3d(-moz-calc(-100% + 16px),-5px,0);transform:translate3d(-webkit-calc(-100% + 16px),-5px,0);transform:translate3d(-moz-calc(-100% + 16px),-5px,0);transform:translate3d(calc(-100% + 16px),-5px,0)}[role~="tooltip"][data-microtip-position="top-right"]::after{-webkit-transform:translate3d(-webkit-calc(0% + -16px),0,0);-moz-transform:translate3d(-moz-calc(0% + -16px),0,0);transform:translate3d(-webkit-calc(0% + -16px),0,0);transform:translate3d(-moz-calc(0% + -16px),0,0);transform:translate3d(calc(0% + -16px),0,0);bottom:100%}[role~="tooltip"][data-microtip-position="top-right"]:hover::after{-webkit-transform:translate3d(-webkit-calc(0% + -16px),-5px,0);-moz-transform:translate3d(-moz-calc(0% + -16px),-5px,0);transform:translate3d(-webkit-calc(0% + -16px),-5px,0);transform:translate3d(-moz-calc(0% + -16px),-5px,0);transform:translate3d(calc(0% + -16px),-5px,0)}[role~="tooltip"][data-microtip-position|="bottom"]::after{margin-top:8px}[role~="tooltip"][data-microtip-position|="bottom"]::before{-webkit-transform:translate3d(-50%,-10px,0);-moz-transform:translate3d(-50%,-10px,0);transform:translate3d(-50%,-10px,0);bottom:auto;left:50%;top:100%}[role~="tooltip"][data-microtip-position|="bottom"]:hover::before{-webkit-transform:translate3d(-50%,0,0);-moz-transform:translate3d(-50%,0,0);transform:translate3d(-50%,0,0)}[role~="tooltip"][data-microtip-position|="bottom"]::after{-webkit-transform:translate3d(-50%,-10px,0);-moz-transform:translate3d(-50%,-10px,0);transform:translate3d(-50%,-10px,0);top:100%;left:50%}[role~="tooltip"][data-microtip-position="bottom"]:hover::after{-webkit-transform:translate3d(-50%,0,0);-moz-transform:translate3d(-50%,0,0);transform:translate3d(-50%,0,0)}[role~="tooltip"][data-microtip-position="bottom-left"]::after{-webkit-transform:translate3d(-webkit-calc(-100% + 16px),-10px,0);-moz-transform:translate3d(-moz-calc(-100% + 16px),-10px,0);transform:translate3d(-webkit-calc(-100% + 16px),-10px,0);transform:translate3d(-moz-calc(-100% + 16px),-10px,0);transform:translate3d(calc(-100% + 16px),-10px,0);top:100%}[role~="tooltip"][data-microtip-position="bottom-left"]:hover::after{-webkit-transform:translate3d(-webkit-calc(-100% + 16px),0,0);-moz-transform:translate3d(-moz-calc(-100% + 16px),0,0);transform:translate3d(-webkit-calc(-100% + 16px),0,0);transform:translate3d(-moz-calc(-100% + 16px),0,0);transform:translate3d(calc(-100% + 16px),0,0)}[role~="tooltip"][data-microtip-position="bottom-right"]::after{-webkit-transform:translate3d(-webkit-calc(0% + -16px),-10px,0);-moz-transform:translate3d(-moz-calc(0% + -16px),-10px,0);transform:translate3d(-webkit-calc(0% + -16px),-10px,0);transform:translate3d(-moz-calc(0% + -16px),-10px,0);transform:translate3d(calc(0% + -16px),-10px,0);top:100%}[role~="tooltip"][data-microtip-position="bottom-right"]:hover::after{-webkit-transform:translate3d(-webkit-calc(0% + -16px),0,0);-moz-transform:translate3d(-moz-calc(0% + -16px),0,0);transform:translate3d(-webkit-calc(0% + -16px),0,0);transform:translate3d(-moz-calc(0% + -16px),0,0);transform:translate3d(calc(0% + -16px),0,0)}[role~="tooltip"][data-microtip-position="left"]::before,[role~="tooltip"][data-microtip-position="left"]::after{bottom:auto;left:auto;right:100%;top:50%;-webkit-transform:translate3d(10px,-50%,0);-moz-transform:translate3d(10px,-50%,0);transform:translate3d(10px,-50%,0)}[role~="tooltip"][data-microtip-position="left"]::after{margin-right:8px}[role~="tooltip"][data-microtip-position="left"]:hover::before,[role~="tooltip"][data-microtip-position="left"]:hover::after{-webkit-transform:translate3d(0,-50%,0);-moz-transform:translate3d(0,-50%,0);transform:translate3d(0,-50%,0)}[role~="tooltip"][data-microtip-position="right"]::before,[role~="tooltip"][data-microtip-position="right"]::after{bottom:auto;left:100%;top:50%;-webkit-transform:translate3d(-10px,-50%,0);-moz-transform:translate3d(-10px,-50%,0);transform:translate3d(-10px,-50%,0)}[role~="tooltip"][data-microtip-position="right"]::after{margin-left:8px}[role~="tooltip"][data-microtip-position="right"]:hover::before,[role~="tooltip"][data-microtip-position="right"]:hover::after{-webkit-transform:translate3d(0,-50%,0);-moz-transform:translate3d(0,-50%,0);transform:translate3d(0,-50%,0)}[role~="tooltip"][data-microtip-size="small"]::after{white-space:initial;width:80px}[role~="tooltip"][data-microtip-size="medium"]::after{white-space:initial;width:150px}[role~="tooltip"][data-microtip-size="large"]::after{white-space:initial;width:260px}</style><style id="__jsx-f83c26ef365e6ab">.ReactModal__Overlay--after-open{-webkit-animation:ReactModal-enter 100ms forwards;-moz-animation:ReactModal-enter 100ms forwards;-o-animation:ReactModal-enter 100ms forwards;animation:ReactModal-enter 100ms forwards}.ReactModal__Overlay--before-close{-webkit-animation:ReactModal-exit 100ms forwards;-moz-animation:ReactModal-exit 100ms forwards;-o-animation:ReactModal-exit 100ms forwards;animation:ReactModal-exit 100ms forwards}@-webkit-keyframes ReactModal-enter{0%{opacity:0}100%{opacity:1}}@-moz-keyframes ReactModal-enter{0%{opacity:0}100%{opacity:1}}@-o-keyframes ReactModal-enter{0%{opacity:0}100%{opacity:1}}@keyframes ReactModal-enter{0%{opacity:0}100%{opacity:1}}@-webkit-keyframes ReactModal-exit{0%{opacity:1}100%{opacity:0}}@-moz-keyframes ReactModal-exit{0%{opacity:1}100%{opacity:0}}@-o-keyframes ReactModal-exit{0%{opacity:1}100%{opacity:0}}@keyframes ReactModal-exit{0%{opacity:1}100%{opacity:0}}</style><style data-emotion="css-global" data-s="">.replit-ui-theme-root,:root{--border-radius-1:1px;--border-radius-2:2px;--border-radius-4:4px;--border-radius-8:8px;--border-radius-16:16px;--border-radius-default:var(--border-radius-8);--border-radius-round:1028px;--space-2:2px;--space-4:4px;--space-8:8px;--space-12:12px;--space-16:16px;--space-24:24px;--space-32:32px;--space-48:48px;--space-64:64px;--space-128:128px;--space-256:256px;--space-default:var(--space-8);--shadow-1:0px 4px 8px 0px rgba(2, 2, 3, 0.16);--shadow-2:0px 8px 16px 0px rgba(2, 2, 3, 0.32);--shadow-3:0px 16px 32px 0px rgba(2, 2, 3, 0.48);--shadow-default:var(--shadow-1);--font-family-default:'IBM Plex Sans',sans-serif;--font-family-code:'ReplitHack','IBM Plex Mono',monospace;--font-size-small:12px;--line-height-small:1.5;--font-size-default:14px;--line-height-default:1.6;--font-size-subhead-default:16px;--line-height-subhead-default:1.375;--font-size-subhead-big:20px;--line-height-subhead-big:1.2;--font-size-header-default:24px;--line-height-header-default:1;--font-size-header-big:32px;--line-height-header-big:1;--font-weight-regular:400;--font-weight-medium:500;--font-weight-bold:600;--border-width-default:1px;--single-line:1;--black:#0E1525;--white:#FCFCFC;}.replit-ui-theme-root.dark{--background-root:#0E1525;--background-default:#1C2333;--background-higher:#2B3245;--background-highest:#3C445C;--background-overlay:#0e1525A0;--foreground-default:#F5F9FC;--foreground-dimmer:#C2C8CC;--foreground-dimmest:#9DA2A6;--outline-strongest:#9195A1;--outline-stronger:#828899;--outline-default:#70788C;--outline-dimmer:#5F677A;--outline-dimmest:#4E5569;-webkit---accent-primary-dimmest:#004182;--accent-primary-dimmest:#004182;--accent-primary-dimmer:#0053A6;-webkit---accent-primary-default:#0079F2;--accent-primary-default:#0079F2;--accent-primary-stronger:#57ABFF;--accent-primary-strongest:#B2D9FF;--accent-positive-dimmest:#044A10;-webkit---accent-positive-dimmer:#046113;--accent-positive-dimmer:#046113;--accent-positive-default:#009118;--accent-positive-stronger:#6CD97E;--accent-positive-strongest:#BFFFCA;--accent-negative-dimmest:#660000;-webkit---accent-negative-dimmer:#A60808;--accent-negative-dimmer:#A60808;--accent-negative-default:#E52222;--accent-negative-stronger:#FF6666;--accent-negative-strongest:#FFCFCF;--accent-red-dimmest:#660000;--accent-red-dimmer:#A60808;--accent-red-default:#E52222;--accent-red-stronger:#FF6666;--accent-red-strongest:#FFCFCF;--accent-orange-dimmest:#542A00;--accent-orange-dimmer:#703800;--accent-orange-default:#AD5700;-webkit---accent-orange-stronger:#D4781C;--accent-orange-stronger:#D4781C;--accent-orange-strongest:#FFBD7A;--accent-yellow-dimmest:#4D4000;--accent-yellow-dimmer:#635300;--accent-yellow-default:#967D00;-webkit---accent-yellow-stronger:#BFA730;--accent-yellow-stronger:#BFA730;--accent-yellow-strongest:#F2E088;--accent-lime-dimmest:#314A00;--accent-lime-dimmer:#3D5C00;--accent-lime-default:#5A8700;--accent-lime-stronger:#87B825;--accent-lime-strongest:#C4E581;--accent-green-dimmest:#044A10;--accent-green-dimmer:#046113;--accent-green-default:#009118;--accent-green-stronger:#6CD97E;-webkit---accent-green-strongest:#7AEB8D;--accent-green-strongest:#7AEB8D;--accent-teal-dimmest:#004452;--accent-teal-dimmer:#006073;--accent-teal-default:#0093B0;--accent-teal-stronger:#27B9D6;--accent-teal-strongest:#69D9F0;--accent-blue-dimmest:#004182;--accent-blue-dimmer:#0053A6;--accent-blue-default:#0079F2;--accent-blue-stronger:#57ABFF;--accent-blue-strongest:#B2D9FF;-webkit---accent-blurple-dimmest:#39298A;--accent-blurple-dimmest:#39298A;--accent-blurple-dimmer:#5239CC;-webkit---accent-blurple-default:#795EFF;--accent-blurple-default:#795EFF;--accent-blurple-stronger:#A694FF;--accent-blurple-strongest:#CEC4FF;--accent-purple-dimmest:#582987;--accent-purple-dimmer:#7633B8;--accent-purple-default:#A64DFF;-webkit---accent-purple-stronger:#C78FFF;--accent-purple-stronger:#C78FFF;--accent-purple-strongest:#E2C4FF;-webkit---accent-magenta-dimmest:#6B1A6B;--accent-magenta-dimmest:#6B1A6B;--accent-magenta-dimmer:#8A218A;-webkit---accent-magenta-default:#C73AC7;--accent-magenta-default:#C73AC7;--accent-magenta-stronger:#F562F5;--accent-magenta-strongest:#FFBFFF;--accent-pink-dimmest:#6E1B52;--accent-pink-dimmer:#8F226B;--accent-pink-default:#D4359F;--accent-pink-stronger:#FF70CF;--accent-pink-strongest:#FFBAE8;--accent-grey-dimmest:#404040;--accent-grey-dimmer:#545454;--accent-grey-default:#808080;--accent-grey-stronger:#A6A6A6;--accent-grey-strongest:#D4D4D4;--accent-brown-dimmest:#594031;--accent-brown-dimmer:#75503B;--accent-brown-default:#A3765C;--accent-brown-stronger:#D49877;-webkit---accent-brown-strongest:#FFC8A8;--accent-brown-strongest:#FFC8A8;}.replit-ui-theme-root.light{--background-root:#EBECED;--background-default:#FCFCFC;--background-higher:#F0F1F2;--background-highest:#E4E5E6;--background-overlay:#F0F1F2A0;--foreground-default:#07080A;--foreground-dimmer:#3D4047;--foreground-dimmest:#5C5F66;--outline-strongest:#74767A;--outline-stronger:#98999C;--outline-default:#AFB1B3;--outline-dimmer:#C0C3C4;--outline-dimmest:#D2D4D6;-webkit---accent-primary-dimmest:#B2D9FF;--accent-primary-dimmest:#B2D9FF;--accent-primary-dimmer:#6BB5FF;-webkit---accent-primary-default:#0F87FF;--accent-primary-default:#0F87FF;--accent-primary-stronger:#005CB8;--accent-primary-strongest:#004182;--accent-positive-dimmest:#7AEB8D;-webkit---accent-positive-dimmer:#3CC954;--accent-positive-dimmer:#3CC954;--accent-positive-default:#00A11B;--accent-positive-stronger:#036E15;--accent-positive-strongest:#004D0D;--accent-negative-dimmest:#FFC7C7;-webkit---accent-negative-dimmer:#FF9494;--accent-negative-dimmer:#FF9494;--accent-negative-default:#FA4B4B;--accent-negative-stronger:#C20A0A;--accent-negative-strongest:#8A0000;--accent-red-dimmest:#FFC7C7;--accent-red-dimmer:#FF9494;--accent-red-default:#FA4B4B;--accent-red-stronger:#C20A0A;--accent-red-strongest:#8A0000;--accent-orange-dimmest:#FFCC99;--accent-orange-dimmer:#FF9933;--accent-orange-default:#D96D00;-webkit---accent-orange-stronger:#964B00;--accent-orange-stronger:#964B00;--accent-orange-strongest:#693400;--accent-yellow-dimmest:#EBD66E;--accent-yellow-dimmer:#CFB015;--accent-yellow-default:#A68A00;-webkit---accent-yellow-stronger:#736000;--accent-yellow-stronger:#736000;--accent-yellow-strongest:#4F4200;--accent-lime-dimmest:#C0E378;--accent-lime-dimmer:#93C926;--accent-lime-default:#639400;--accent-lime-stronger:#466900;--accent-lime-strongest:#3A5700;--accent-green-dimmest:#7AEB8D;--accent-green-dimmer:#3CC954;--accent-green-default:#00A11B;--accent-green-stronger:#036E15;-webkit---accent-green-strongest:#004D0D;--accent-green-strongest:#004D0D;--accent-teal-dimmest:#6FE5FC;--accent-teal-dimmer:#22C1E0;--accent-teal-default:#0093B0;--accent-teal-stronger:#00687D;--accent-teal-strongest:#004857;--accent-blue-dimmest:#B2D9FF;--accent-blue-dimmer:#6BB5FF;--accent-blue-default:#0F87FF;--accent-blue-stronger:#005CB8;--accent-blue-strongest:#004182;-webkit---accent-blurple-dimmest:#D7CFFF;--accent-blurple-dimmest:#D7CFFF;--accent-blurple-dimmer:#B2A3FF;-webkit---accent-blurple-default:#8E78FF;--accent-blurple-default:#8E78FF;--accent-blurple-stronger:#5B40E3;--accent-blurple-strongest:#412F9C;--accent-purple-dimmest:#E6CCFF;--accent-purple-dimmer:#D0A1FF;--accent-purple-default:#B266FF;-webkit---accent-purple-stronger:#7F38C7;--accent-purple-stronger:#7F38C7;--accent-purple-strongest:#5B278F;-webkit---accent-magenta-dimmest:#FFBFFF;--accent-magenta-dimmest:#FFBFFF;--accent-magenta-dimmer:#FF82FF;-webkit---accent-magenta-default:#EB3BEB;--accent-magenta-default:#EB3BEB;--accent-magenta-stronger:#A321A3;--accent-magenta-strongest:#731C73;--accent-pink-dimmest:#FFC7EC;--accent-pink-dimmer:#FF87D7;--accent-pink-default:#F545BA;--accent-pink-stronger:#AB2980;--accent-pink-strongest:#781E5A;--accent-grey-dimmest:#D5D5D5;--accent-grey-dimmer:#B0B0B0;--accent-grey-default:#898989;--accent-grey-stronger:#616161;--accent-grey-strongest:#454545;--accent-brown-dimmest:#FFC9AB;--accent-brown-dimmer:#DEA483;--accent-brown-default:#B07F63;--accent-brown-stronger:#805740;-webkit---accent-brown-strongest:#573E30;--accent-brown-strongest:#573E30;}.replit-ui-theme-root.spooky{--background-root:#020203;--background-default:#292C33;--background-higher:#383B42;--background-highest:#474A52;--background-overlay:#F0F1F2A0;--foreground-default:#F5F9FC;--foreground-dimmer:#C2C8CC;--foreground-dimmest:#9DA2A6;--outline-strongest:#9195A1;--outline-stronger:#828899;--outline-default:#70788C;--outline-dimmer:#5F677A;--outline-dimmest:#4E5569;-webkit---accent-primary-dimmest:var(--accent-orange-dimmest);--accent-primary-dimmest:var(--accent-orange-dimmest);--accent-primary-dimmer:var(--accent-orange-dimmer);-webkit---accent-primary-default:var(--accent-orange-default);--accent-primary-default:var(--accent-orange-default);--accent-primary-stronger:var(--accent-orange-stronger);--accent-primary-strongest:var(--accent-orange-strongest);--accent-positive-dimmest:var(--accent-orange-dimmest);-webkit---accent-positive-dimmer:var(--accent-orange-dimmer);--accent-positive-dimmer:var(--accent-orange-dimmer);--accent-positive-default:var(--accent-orange-default);--accent-positive-stronger:var(--accent-orange-stronger);--accent-positive-strongest:var(--accent-orange-strongest);--accent-negative-dimmest:#573A3A;-webkit---accent-negative-dimmer:#8F2828;--accent-negative-dimmer:#8F2828;--accent-negative-default:#F23F3F;--accent-negative-stronger:#FF8585;--accent-negative-strongest:#FFBFBF;--accent-red-dimmest:#6E0000;--accent-red-dimmer:#A60000;--accent-red-default:#E50000;--accent-red-stronger:#FF8585;--accent-red-strongest:#FFC7C7;--accent-orange-dimmest:#753B00;--accent-orange-dimmer:#9C4E00;--accent-orange-default:#D96D00;-webkit---accent-orange-stronger:#FFC285;--accent-orange-stronger:#FFC285;--accent-orange-strongest:#FFD9B2;--accent-yellow-dimmest:#756200;--accent-yellow-dimmer:#A68A00;--accent-yellow-default:#CCAD14;-webkit---accent-yellow-stronger:#FFEA7F;--accent-yellow-stronger:#FFEA7F;--accent-yellow-strongest:#FFF2B2;--accent-lime-dimmest:#314A00;--accent-lime-dimmer:#3D5C00;--accent-lime-default:#5A8700;--accent-lime-stronger:#87B825;--accent-lime-strongest:#C4E581;--accent-green-dimmest:#00540E;--accent-green-dimmer:#007814;--accent-green-default:#36B24A;--accent-green-stronger:#66FF7F;-webkit---accent-green-strongest:#B2FFBF;--accent-green-strongest:#B2FFBF;--accent-teal-dimmest:#005B6E;--accent-teal-dimmer:#007F99;--accent-teal-default:#3DB4CC;--accent-teal-stronger:#7FEAFF;--accent-teal-strongest:#BFF4FF;--accent-blue-dimmest:#004D99;--accent-blue-dimmer:#005EBD;--accent-blue-default:#2E8AE5;--accent-blue-stronger:#7FBFFF;--accent-blue-strongest:#B2D9FF;-webkit---accent-blurple-dimmest:#422F9E;--accent-blurple-dimmest:#422F9E;--accent-blurple-dimmer:#563CD6;-webkit---accent-blurple-default:#7559FF;--accent-blurple-default:#7559FF;--accent-blurple-stronger:#A18FFF;--accent-blurple-strongest:#CEC4FF;--accent-purple-dimmest:#6C32A6;--accent-purple-dimmer:#9140E3;--accent-purple-default:#A64DFF;-webkit---accent-purple-stronger:#C78FFF;--accent-purple-stronger:#C78FFF;--accent-purple-strongest:#E2C4FF;-webkit---accent-magenta-dimmest:#802680;--accent-magenta-dimmest:#802680;--accent-magenta-dimmer:#B031B0;-webkit---accent-magenta-default:#E55AE5;--accent-magenta-default:#E55AE5;--accent-magenta-stronger:#FF8AFF;--accent-magenta-strongest:#FFC2FF;--accent-pink-dimmest:#802662;--accent-pink-dimmer:#B03186;--accent-pink-default:#E545B0;--accent-pink-stronger:#FF8AD8;--accent-pink-strongest:#FFC2EB;--accent-grey-dimmest:#595959;--accent-grey-dimmer:#666666;--accent-grey-default:#808080;--accent-grey-stronger:#999999;--accent-grey-strongest:#BFBFBF;--accent-brown-dimmest:#594031;--accent-brown-dimmer:#75503B;--accent-brown-default:#A3765C;--accent-brown-stronger:#D49877;-webkit---accent-brown-strongest:#FFC8A8;--accent-brown-strongest:#FFC8A8;}</style><style data-emotion="css 1gczmi5" data-s="">.css-1gczmi5{transition-property:border-color,box-shadow;transition-duration:120ms;transition-timing-function:ease-out;border-radius:var(--border-radius-8);background-color:var(--interactive-background);border-width:1px;border-style:solid;border-color:transparent;padding:var(--space-4);border-radius:0 0 var(--border-radius-4) var(--border-radius-4);font-size:var(--font-size-subhead-big);position:fixed;top:0;left:4px;-webkit-transform:translateY(-100%);-moz-transform:translateY(-100%);-ms-transform:translateY(-100%);transform:translateY(-100%);z-index:5000;}.css-1gczmi5:not([disabled]){cursor:pointer;}.css-1gczmi5:not([disabled]):hover{border-color:var(--interactive-border--hover);}.css-1gczmi5:not([disabled]):focus{box-shadow:0 0 0 2px var(--accent-primary-default);}.css-1gczmi5:not([disabled]):focus:not(:focus-visible){box-shadow:none;}.css-1gczmi5:not([disabled]):active{background-color:var(--interactive-background--active);border-color:var(--accent-primary-default);}.css-1gczmi5:focus{-webkit-transform:translateY(0);-moz-transform:translateY(0);-ms-transform:translateY(0);transform:translateY(0);}</style><style data-emotion="css 3nkjrn" data-s="">.css-3nkjrn{-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;height:100%;background-color:transparent;}</style><style data-emotion="css 5papiq" data-s="">.css-5papiq{background-color:var(--background-default);--interactive-background:var(--background-higher);--interactive-background--active:var(--background-highest);--interactive-border:var(--outline-dimmest);--interactive-border--hover:var(--outline-default);-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;height:100%;background-color:transparent;}</style><style data-emotion="css d6exn6" data-s="">.css-d6exn6{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;background-color:var(--background-default);--interactive-background:var(--background-higher);--interactive-background--active:var(--background-highest);--interactive-border:var(--outline-dimmest);--interactive-border--hover:var(--outline-default);-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;height:100%;background-color:transparent;}</style><style data-emotion="css 36v8q4" data-s="">.css-36v8q4{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;}</style><style data-emotion="css qlcqm5" data-s="">.css-qlcqm5{border:none;background:transparent;color:inherit;font:inherit;line-height:normal;transition-property:background-color,box-shadow;transition-duration:120ms;transition-timing-function:ease-out;border-width:1px;border-style:solid;border-color:transparent;border-radius:var(--border-radius-8);-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;width:28px;height:28px;}.css-qlcqm5:not([disabled]){cursor:pointer;}.css-qlcqm5:not([disabled]):hover{background-color:var(--interactive-background);}.css-qlcqm5:not([disabled]):focus{box-shadow:0 0 0 2px var(--accent-primary-default);}.css-qlcqm5:not([disabled]):focus:not(:focus-visible){box-shadow:none;}.css-qlcqm5:not([disabled]):active{background-color:var(--interactive-background--active);border-color:var(--accent-primary-default);}</style><style data-emotion="css 1cpig0h" data-s="">.css-1cpig0h{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;border:none;background:transparent;color:inherit;font:inherit;line-height:normal;transition-property:background-color,box-shadow;transition-duration:120ms;transition-timing-function:ease-out;border-width:1px;border-style:solid;border-color:transparent;border-radius:var(--border-radius-8);-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;width:28px;height:28px;}.css-1cpig0h:not([disabled]){cursor:pointer;}.css-1cpig0h:not([disabled]):hover{background-color:var(--interactive-background);}.css-1cpig0h:not([disabled]):focus{box-shadow:0 0 0 2px var(--accent-primary-default);}.css-1cpig0h:not([disabled]):focus:not(:focus-visible){box-shadow:none;}.css-1cpig0h:not([disabled]):active{background-color:var(--interactive-background--active);border-color:var(--accent-primary-default);}</style><style data-emotion="css 39pr92" data-s="">.css-39pr92{position:fixed;height:100%;max-height:100vh;top:0;left:0;width:240px;-webkit-transform:translateX(-100%);-moz-transform:translateX(-100%);-ms-transform:translateX(-100%);transform:translateX(-100%);z-index:1002;display:grid;grid-template-rows:auto 1fr;background-color:var(--background-default);border-right:.5px solid var(--background-highest);-webkit-transition:-webkit-transform 0.2s;transition:transform 0.2s;box-shadow:var(--shadow-2);border-right:0;-webkit-transform:translateX(0);-moz-transform:translateX(0);-ms-transform:translateX(0);transform:translateX(0);opacity:1;transition-delay:100ms;}@media(min-width: 768px){.css-39pr92{transition-duration:0s;}}@media(max-width: 480px){.css-39pr92{min-height:-webkit-fill-available;}}</style><style data-emotion="css yjss5g" data-s="">.css-yjss5g{background-color:var(--background-default);--interactive-background:var(--background-higher);--interactive-background--active:var(--background-highest);--interactive-border:var(--outline-dimmest);--interactive-border--hover:var(--outline-default);position:fixed;height:100%;max-height:100vh;top:0;left:0;width:240px;-webkit-transform:translateX(-100%);-moz-transform:translateX(-100%);-ms-transform:translateX(-100%);transform:translateX(-100%);z-index:1002;display:grid;grid-template-rows:auto 1fr;background-color:var(--background-default);border-right:.5px solid var(--background-highest);-webkit-transition:-webkit-transform 0.2s;transition:transform 0.2s;box-shadow:var(--shadow-2);border-right:0;-webkit-transform:translateX(0);-moz-transform:translateX(0);-ms-transform:translateX(0);transform:translateX(0);opacity:1;transition-delay:100ms;}@media(min-width: 768px){.css-yjss5g{transition-duration:0s;}}@media(max-width: 480px){.css-yjss5g{min-height:-webkit-fill-available;}}</style><style data-emotion="css qx8iom" data-s="">.css-qx8iom{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;background-color:var(--background-default);--interactive-background:var(--background-higher);--interactive-background--active:var(--background-highest);--interactive-border:var(--outline-dimmest);--interactive-border--hover:var(--outline-default);position:fixed;height:100%;max-height:100vh;top:0;left:0;width:240px;-webkit-transform:translateX(-100%);-moz-transform:translateX(-100%);-ms-transform:translateX(-100%);transform:translateX(-100%);z-index:1002;display:grid;grid-template-rows:auto 1fr;background-color:var(--background-default);border-right:.5px solid var(--background-highest);-webkit-transition:-webkit-transform 0.2s;transition:transform 0.2s;box-shadow:var(--shadow-2);border-right:0;-webkit-transform:translateX(0);-moz-transform:translateX(0);-ms-transform:translateX(0);transform:translateX(0);opacity:1;transition-delay:100ms;}@media(min-width: 768px){.css-qx8iom{transition-duration:0s;}}@media(max-width: 480px){.css-qx8iom{min-height:-webkit-fill-available;}}</style><style data-emotion="css 36v8q4" data-s="">.css-36v8q4{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;}</style><style data-emotion="css qlcqm5" data-s="">.css-qlcqm5{border:none;background:transparent;color:inherit;font:inherit;line-height:normal;transition-property:background-color,box-shadow;transition-duration:120ms;transition-timing-function:ease-out;border-width:1px;border-style:solid;border-color:transparent;border-radius:var(--border-radius-8);-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;width:28px;height:28px;}.css-qlcqm5:not([disabled]){cursor:pointer;}.css-qlcqm5:not([disabled]):hover{background-color:var(--interactive-background);}.css-qlcqm5:not([disabled]):focus{box-shadow:0 0 0 2px var(--accent-primary-default);}.css-qlcqm5:not([disabled]):focus:not(:focus-visible){box-shadow:none;}.css-qlcqm5:not([disabled]):active{background-color:var(--interactive-background--active);border-color:var(--accent-primary-default);}</style><style data-emotion="css 1cpig0h" data-s="">.css-1cpig0h{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;border:none;background:transparent;color:inherit;font:inherit;line-height:normal;transition-property:background-color,box-shadow;transition-duration:120ms;transition-timing-function:ease-out;border-width:1px;border-style:solid;border-color:transparent;border-radius:var(--border-radius-8);-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;width:28px;height:28px;}.css-1cpig0h:not([disabled]){cursor:pointer;}.css-1cpig0h:not([disabled]):hover{background-color:var(--interactive-background);}.css-1cpig0h:not([disabled]):focus{box-shadow:0 0 0 2px var(--accent-primary-default);}.css-1cpig0h:not([disabled]):focus:not(:focus-visible){box-shadow:none;}.css-1cpig0h:not([disabled]):active{background-color:var(--interactive-background--active);border-color:var(--accent-primary-default);}</style><style data-emotion="css 1xlwzok" data-s="">.css-1xlwzok{-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;border:none;background:transparent;color:inherit;font:inherit;line-height:normal;transition-property:border-color,box-shadow;transition-duration:120ms;transition-timing-function:ease-out;border-radius:var(--border-radius-8);background-color:var(--interactive-background);border-width:1px;border-style:solid;border-color:transparent;padding:var(--space-8);border-radius:var(--border-radius-8);transition-property:border-color,box-shadow;transition-duration:120ms;transition-timing-function:ease-out;border-style:solid;border-width:1px;border-color:transparent;height:32px;}.css-1xlwzok>*{margin-right:var(--space-8);}.css-1xlwzok>*:last-child{margin-right:0;}.css-1xlwzok:not([disabled]){cursor:pointer;}.css-1xlwzok:not([disabled]):hover{border-color:var(--interactive-border--hover);}.css-1xlwzok:not([disabled]):focus{box-shadow:0 0 0 2px var(--accent-primary-default);}.css-1xlwzok:not([disabled]):focus:not(:focus-visible){box-shadow:none;}.css-1xlwzok:not([disabled]):active{background-color:var(--interactive-background--active);border-color:var(--accent-primary-default);}.css-1xlwzok{color:var(--foreground-default);background-color:var(--accent-primary-dimmer);box-shadow:none;}.css-1xlwzok:disabled{background-color:var(--accent-primary-dimmest);color:var(--accent-primary-default);}.css-1xlwzok:not([disabled]):hover{border-color:var(--accent-primary-stronger);}.css-1xlwzok:not([disabled]):focus{box-shadow:0 0 0 2px var(--accent-primary-stronger);}.css-1xlwzok:not([disabled]):focus:not(:focus-visible){box-shadow:none;}.css-1xlwzok:not([disabled]):active{background-color:var(--accent-primary-dimmest);border-color:var(--accent-primary-default);}</style><style data-emotion="css 17qxwok" data-s="">.css-17qxwok{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;border:none;background:transparent;color:inherit;font:inherit;line-height:normal;transition-property:border-color,box-shadow;transition-duration:120ms;transition-timing-function:ease-out;border-radius:var(--border-radius-8);background-color:var(--interactive-background);border-width:1px;border-style:solid;border-color:transparent;padding:var(--space-8);border-radius:var(--border-radius-8);transition-property:border-color,box-shadow;transition-duration:120ms;transition-timing-function:ease-out;border-style:solid;border-width:1px;border-color:transparent;height:32px;}.css-17qxwok>*{margin-right:var(--space-8);}.css-17qxwok>*:last-child{margin-right:0;}.css-17qxwok:not([disabled]){cursor:pointer;}.css-17qxwok:not([disabled]):hover{border-color:var(--interactive-border--hover);}.css-17qxwok:not([disabled]):focus{box-shadow:0 0 0 2px var(--accent-primary-default);}.css-17qxwok:not([disabled]):focus:not(:focus-visible){box-shadow:none;}.css-17qxwok:not([disabled]):active{background-color:var(--interactive-background--active);border-color:var(--accent-primary-default);}.css-17qxwok{color:var(--foreground-default);background-color:var(--accent-primary-dimmer);box-shadow:none;}.css-17qxwok:disabled{background-color:var(--accent-primary-dimmest);color:var(--accent-primary-default);}.css-17qxwok:not([disabled]):hover{border-color:var(--accent-primary-stronger);}.css-17qxwok:not([disabled]):focus{box-shadow:0 0 0 2px var(--accent-primary-stronger);}.css-17qxwok:not([disabled]):focus:not(:focus-visible){box-shadow:none;}.css-17qxwok:not([disabled]):active{background-color:var(--accent-primary-dimmest);border-color:var(--accent-primary-default);}</style><style data-emotion="css 19fi8pz" data-s="">.css-19fi8pz{-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;-webkit-flex-shrink:1;-ms-flex-negative:1;flex-shrink:1;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;}.css-19fi8pz>*{margin-right:var(--space-8);}.css-19fi8pz>*:last-child{margin-right:0;}</style><style data-emotion="css 52jvb2" data-s="">.css-52jvb2{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;-webkit-flex-shrink:1;-ms-flex-negative:1;flex-shrink:1;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;}.css-52jvb2>*{margin-right:var(--space-8);}.css-52jvb2>*:last-child{margin-right:0;}</style><style data-emotion="css cyokpp" data-s="">.css-cyokpp{display:inline;overflow-wrap:break-word;font-size:var(--font-size-default);line-height:var(--line-height-default);display:inline-block;line-height:1.2;max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}</style><style data-emotion="css o4584k" data-s="">.css-o4584k{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;display:inline;overflow-wrap:break-word;font-size:var(--font-size-default);line-height:var(--line-height-default);display:inline-block;line-height:1.2;max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}</style><style data-emotion="css 1kweg0a" data-s="">.css-1kweg0a{-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;border:none;background:transparent;color:inherit;font:inherit;line-height:normal;transition-property:border-color,background-color,box-shadow;transition-duration:120ms;transition-timing-function:ease-out;border-radius:var(--border-radius-8);background-color:transparent;border-width:1px;border-style:solid;border-color:var(--interactive-border);padding:var(--space-8);border-radius:var(--border-radius-8);height:32px;}.css-1kweg0a>*{margin-right:var(--space-8);}.css-1kweg0a>*:last-child{margin-right:0;}.css-1kweg0a:not([disabled]){cursor:pointer;}.css-1kweg0a:not([disabled]):hover{border-color:var(--interactive-border--hover);background-color:var(--interactive-background);}.css-1kweg0a:not([disabled]):focus{box-shadow:0 0 0 2px var(--accent-primary-default);}.css-1kweg0a:not([disabled]):focus:not(:focus-visible){box-shadow:none;}.css-1kweg0a:not([disabled]):active{background-color:var(--interactive-background--active);border-color:var(--accent-primary-default);}</style><style data-emotion="css 1dm3o0s" data-s="">.css-1dm3o0s{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;border:none;background:transparent;color:inherit;font:inherit;line-height:normal;transition-property:border-color,background-color,box-shadow;transition-duration:120ms;transition-timing-function:ease-out;border-radius:var(--border-radius-8);background-color:transparent;border-width:1px;border-style:solid;border-color:var(--interactive-border);padding:var(--space-8);border-radius:var(--border-radius-8);height:32px;}.css-1dm3o0s>*{margin-right:var(--space-8);}.css-1dm3o0s>*:last-child{margin-right:0;}.css-1dm3o0s:not([disabled]){cursor:pointer;}.css-1dm3o0s:not([disabled]):hover{border-color:var(--interactive-border--hover);background-color:var(--interactive-background);}.css-1dm3o0s:not([disabled]):focus{box-shadow:0 0 0 2px var(--accent-primary-default);}.css-1dm3o0s:not([disabled]):focus:not(:focus-visible){box-shadow:none;}.css-1dm3o0s:not([disabled]):active{background-color:var(--interactive-background--active);border-color:var(--accent-primary-default);}</style><style data-emotion="css uodor8" data-s="">.css-uodor8{border-radius:50%;}</style><style data-emotion="css 1l3h8o6" data-s="">.css-1l3h8o6{border:none;background:transparent;color:inherit;font:inherit;line-height:normal;transition-property:background-color,box-shadow;transition-duration:120ms;transition-timing-function:ease-out;border-width:1px;border-style:solid;border-color:transparent;border-radius:var(--border-radius-8);-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;width:28px;height:28px;border-radius:50%;}.css-1l3h8o6:not([disabled]){cursor:pointer;}.css-1l3h8o6:not([disabled]):hover{background-color:var(--interactive-background);}.css-1l3h8o6:not([disabled]):focus{box-shadow:0 0 0 2px var(--accent-primary-default);}.css-1l3h8o6:not([disabled]):focus:not(:focus-visible){box-shadow:none;}.css-1l3h8o6:not([disabled]):active{background-color:var(--interactive-background--active);border-color:var(--accent-primary-default);}</style><style data-emotion="css 8weqdd" data-s="">.css-8weqdd{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;border:none;background:transparent;color:inherit;font:inherit;line-height:normal;transition-property:background-color,box-shadow;transition-duration:120ms;transition-timing-function:ease-out;border-width:1px;border-style:solid;border-color:transparent;border-radius:var(--border-radius-8);-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;width:28px;height:28px;border-radius:50%;}.css-8weqdd:not([disabled]){cursor:pointer;}.css-8weqdd:not([disabled]):hover{background-color:var(--interactive-background);}.css-8weqdd:not([disabled]):focus{box-shadow:0 0 0 2px var(--accent-primary-default);}.css-8weqdd:not([disabled]):focus:not(:focus-visible){box-shadow:none;}.css-8weqdd:not([disabled]):active{background-color:var(--interactive-background--active);border-color:var(--accent-primary-default);}</style><style data-emotion="css b1epo2" data-s="">.css-b1epo2{-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;}.css-b1epo2>*{margin-right:var(--space-12);}.css-b1epo2>*:last-child{margin-right:0;}</style><style data-emotion="css 123hrlt" data-s="">.css-123hrlt{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;}.css-123hrlt>*{margin-right:var(--space-12);}.css-123hrlt>*:last-child{margin-right:0;}</style><style data-emotion="css bnuc6w" data-s="">.css-bnuc6w{position:relative;height:42px;}</style><style data-emotion="css qalru5" data-s="">.css-qalru5{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;position:relative;height:42px;}</style><style data-emotion="css ccbya9" data-s="">.css-ccbya9{border-radius:var(--border-radius-8);border:1px solid transparent;position:absolute;top:0;left:0;width:100%;}.css-ccbya9:focus-within{box-shadow:var(--shadow-2);border-color:var(--outline-dimmest);}</style><style data-emotion="css 1of2mve" data-s="">.css-1of2mve{background-color:var(--background-higher);--interactive-background:var(--background-highest);--interactive-background--active:var(--outline-dimmer);--interactive-border:var(--outline-dimmer);--interactive-border--hover:var(--outline-default);border-radius:var(--border-radius-8);border:1px solid transparent;position:absolute;top:0;left:0;width:100%;}.css-1of2mve:focus-within{box-shadow:var(--shadow-2);border-color:var(--outline-dimmest);}</style><style data-emotion="css 1k461zs" data-s="">.css-1k461zs{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;background-color:var(--background-higher);--interactive-background:var(--background-highest);--interactive-background--active:var(--outline-dimmer);--interactive-border:var(--outline-dimmer);--interactive-border--hover:var(--outline-default);border-radius:var(--border-radius-8);border:1px solid transparent;position:absolute;top:0;left:0;width:100%;}.css-1k461zs:focus-within{box-shadow:var(--shadow-2);border-color:var(--outline-dimmest);}</style><style data-emotion="css 36v8q4" data-s="">.css-36v8q4{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;}</style><style data-emotion="css 1uurvo4" data-s="">.css-1uurvo4{-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;padding:var(--space-4);padding-left:var(--space-8);}.css-1uurvo4>*{margin-right:var(--space-4);}.css-1uurvo4>*:last-child{margin-right:0;}</style><style data-emotion="css z6uel0" data-s="">.css-z6uel0{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;padding:var(--space-4);padding-left:var(--space-8);}.css-z6uel0>*{margin-right:var(--space-4);}.css-z6uel0>*:last-child{margin-right:0;}</style><style data-emotion="css 180cs1a" data-s="">.css-180cs1a{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;-webkit-flex-shrink:1;-ms-flex-negative:1;flex-shrink:1;}</style><style data-emotion="css 1qvjv55" data-s="">.css-1qvjv55{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;-webkit-flex-shrink:1;-ms-flex-negative:1;flex-shrink:1;}</style><style data-emotion="css 1prgmfa" data-s="">.css-1prgmfa{-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;margin-left:var(--space-4);width:var(--space-24);height:100%;color:var(--accent-primary-default);}</style><style data-emotion="css yjf9hv" data-s="">.css-yjf9hv{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;margin-left:var(--space-4);width:var(--space-24);height:100%;color:var(--accent-primary-default);}</style><style data-emotion="css 1236ua0" data-s="">.css-1236ua0{background-color:transparent;border-color:transparent;color:var(--foreground-default);font-size:var(--font-size-subhead-default);padding-right:var(--space-4);padding-top:var(--space-4);padding-bottom:var(--space-4);display:block;width:100%;line-height:1.4;}.css-1236ua0::-webkit-input-placeholder{color:var(--foreground-dimmest);}.css-1236ua0::-moz-placeholder{color:var(--foreground-dimmest);}.css-1236ua0:-ms-input-placeholder{color:var(--foreground-dimmest);}.css-1236ua0::placeholder{color:var(--foreground-dimmest);}.css-1236ua0:focus{outline:0 none;}.css-1236ua0:focus::-webkit-input-placeholder{color:var(--foreground-dimmer);}.css-1236ua0:focus::-moz-placeholder{color:var(--foreground-dimmer);}.css-1236ua0:focus:-ms-input-placeholder{color:var(--foreground-dimmer);}.css-1236ua0:focus::placeholder{color:var(--foreground-dimmer);}.css-1236ua0:hover::-webkit-input-placeholder{color:var(--foreground-dimmer);}.css-1236ua0:hover::-moz-placeholder{color:var(--foreground-dimmer);}.css-1236ua0:hover:-ms-input-placeholder{color:var(--foreground-dimmer);}.css-1236ua0:hover::placeholder{color:var(--foreground-dimmer);}</style><style data-emotion="css bymsuc" data-s="">.css-bymsuc{background-color:var(--accent-primary-dimmest);}</style><style data-emotion="css 36v8q4" data-s="">.css-36v8q4{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;}</style><style data-emotion="css tn8uhb" data-s="">.css-tn8uhb{border:none;background:transparent;color:inherit;font:inherit;line-height:normal;transition-property:background-color,box-shadow;transition-duration:120ms;transition-timing-function:ease-out;border-width:1px;border-style:solid;border-color:transparent;border-radius:var(--border-radius-8);-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;width:28px;height:28px;transition-property:color,background-color,box-shadow;transition-duration:120ms;transition-timing-function:ease-out;border-style:solid;border-color:transparent;border-width:1px;background-color:var(--accent-primary-dimmest);}.css-tn8uhb:not([disabled]){cursor:pointer;}.css-tn8uhb:not([disabled]):hover{background-color:var(--interactive-background);}.css-tn8uhb:not([disabled]):focus{box-shadow:0 0 0 2px var(--accent-primary-default);}.css-tn8uhb:not([disabled]):focus:not(:focus-visible){box-shadow:none;}.css-tn8uhb:not([disabled]):active{background-color:var(--interactive-background--active);border-color:var(--accent-primary-default);}.css-tn8uhb{color:var(--accent-primary-stronger);}.css-tn8uhb:disabled{color:var(--accent-primary-dimmer);}.css-tn8uhb:not([disabled]):hover{color:var(--accent-primary-strongest);background-color:var(--accent-primary-dimmer);}.css-tn8uhb:not([disabled]):focus{color:var(--accent-primary-strongest);box-shadow:0 0 0 2px var(--accent-primary-strongest);}.css-tn8uhb:not([disabled]):focus:not(:focus-visible){box-shadow:none;}.css-tn8uhb:not([disabled]):active{color:var(--accent-primary-strongest);background-color:var(--accent-primary-dimmest);border-color:var(--accent-primary-strongest);}</style><style data-emotion="css 114t1do" data-s="">.css-114t1do{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;border:none;background:transparent;color:inherit;font:inherit;line-height:normal;transition-property:background-color,box-shadow;transition-duration:120ms;transition-timing-function:ease-out;border-width:1px;border-style:solid;border-color:transparent;border-radius:var(--border-radius-8);-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;width:28px;height:28px;transition-property:color,background-color,box-shadow;transition-duration:120ms;transition-timing-function:ease-out;border-style:solid;border-color:transparent;border-width:1px;background-color:var(--accent-primary-dimmest);}.css-114t1do:not([disabled]){cursor:pointer;}.css-114t1do:not([disabled]):hover{background-color:var(--interactive-background);}.css-114t1do:not([disabled]):focus{box-shadow:0 0 0 2px var(--accent-primary-default);}.css-114t1do:not([disabled]):focus:not(:focus-visible){box-shadow:none;}.css-114t1do:not([disabled]):active{background-color:var(--interactive-background--active);border-color:var(--accent-primary-default);}.css-114t1do{color:var(--accent-primary-stronger);}.css-114t1do:disabled{color:var(--accent-primary-dimmer);}.css-114t1do:not([disabled]):hover{color:var(--accent-primary-strongest);background-color:var(--accent-primary-dimmer);}.css-114t1do:not([disabled]):focus{color:var(--accent-primary-strongest);box-shadow:0 0 0 2px var(--accent-primary-strongest);}.css-114t1do:not([disabled]):focus:not(:focus-visible){box-shadow:none;}.css-114t1do:not([disabled]):active{color:var(--accent-primary-strongest);background-color:var(--accent-primary-dimmest);border-color:var(--accent-primary-strongest);}</style><style data-emotion="css 1nhxm5u" data-s="">.css-1nhxm5u{-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;min-height:calc(100vh - 60px);}</style><style data-emotion="css 1qzkf4g" data-s="">.css-1qzkf4g{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;min-height:calc(100vh - 60px);}</style><style data-emotion="css vj4l6w" data-s="">.css-vj4l6w{width:100%;max-width:700px;}</style><style data-emotion="css u0t0j" data-s="">.css-u0t0j{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;width:100%;max-width:700px;}</style><style data-emotion="css va6gxj" data-s="">.css-va6gxj{border-radius:var(--border-radius-16);padding:var(--space-16);-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;color:var(--foreground-default);}.css-va6gxj>*{margin-bottom:var(--space-16);}.css-va6gxj>*:last-child{margin-bottom:0;}</style><style data-emotion="css 1tcovtt" data-s="">.css-1tcovtt{background-color:var(--background-default);--interactive-background:var(--background-higher);--interactive-background--active:var(--background-highest);--interactive-border:var(--outline-dimmest);--interactive-border--hover:var(--outline-default);border-radius:var(--border-radius-16);padding:var(--space-16);-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;color:var(--foreground-default);}.css-1tcovtt>*{margin-bottom:var(--space-16);}.css-1tcovtt>*:last-child{margin-bottom:0;}</style><style data-emotion="css itzwbr" data-s="">.css-itzwbr{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;background-color:var(--background-default);--interactive-background:var(--background-higher);--interactive-background--active:var(--background-highest);--interactive-border:var(--outline-dimmest);--interactive-border--hover:var(--outline-default);border-radius:var(--border-radius-16);padding:var(--space-16);-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;color:var(--foreground-default);}.css-itzwbr>*{margin-bottom:var(--space-16);}.css-itzwbr>*:last-child{margin-bottom:0;}</style><style data-emotion="css 1cpk62j" data-s="">.css-1cpk62j{-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}.css-1cpk62j>*{margin-right:var(--space-8);}.css-1cpk62j>*:last-child{margin-right:0;}</style><style data-emotion="css cg4is2" data-s="">.css-cg4is2{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}.css-cg4is2>*{margin-right:var(--space-8);}.css-cg4is2>*:last-child{margin-right:0;}</style><style data-emotion="css tqeoyf" data-s="">.css-tqeoyf{-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;-webkit-flex-shrink:1;-ms-flex-negative:1;flex-shrink:1;}</style><style data-emotion="css 1bxhz61" data-s="">.css-1bxhz61{display:inline;overflow-wrap:break-word;font-size:var(--font-size-header-default);font-weight:var(--font-weight-medium);line-height:var(--line-height-header-default);-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;-webkit-flex-shrink:1;-ms-flex-negative:1;flex-shrink:1;}</style><style data-emotion="css k0n9iu" data-s="">.css-k0n9iu{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;display:inline;overflow-wrap:break-word;font-size:var(--font-size-header-default);font-weight:var(--font-weight-medium);line-height:var(--line-height-header-default);-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;-webkit-flex-shrink:1;-ms-flex-negative:1;flex-shrink:1;}</style><style data-emotion="css 187h60n" data-s="">.css-187h60n{-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;border:none;background:transparent;color:inherit;font:inherit;line-height:normal;transition-property:border-color,box-shadow;transition-duration:120ms;transition-timing-function:ease-out;border-radius:var(--border-radius-8);background-color:var(--interactive-background);border-width:1px;border-style:solid;border-color:transparent;padding:var(--space-8);border-radius:var(--border-radius-8);height:28px;}.css-187h60n>*{margin-right:var(--space-8);}.css-187h60n>*:last-child{margin-right:0;}.css-187h60n:not([disabled]){cursor:pointer;}.css-187h60n:not([disabled]):hover{border-color:var(--interactive-border--hover);}.css-187h60n:not([disabled]):focus{box-shadow:0 0 0 2px var(--accent-primary-default);}.css-187h60n:not([disabled]):focus:not(:focus-visible){box-shadow:none;}.css-187h60n:not([disabled]):active{background-color:var(--interactive-background--active);border-color:var(--accent-primary-default);}</style><style data-emotion="css 4jgsh0" data-s="">.css-4jgsh0{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center;border:none;background:transparent;color:inherit;font:inherit;line-height:normal;transition-property:border-color,box-shadow;transition-duration:120ms;transition-timing-function:ease-out;border-radius:var(--border-radius-8);background-color:var(--interactive-background);border-width:1px;border-style:solid;border-color:transparent;padding:var(--space-8);border-radius:var(--border-radius-8);height:28px;}.css-4jgsh0>*{margin-right:var(--space-8);}.css-4jgsh0>*:last-child{margin-right:0;}.css-4jgsh0:not([disabled]){cursor:pointer;}.css-4jgsh0:not([disabled]):hover{border-color:var(--interactive-border--hover);}.css-4jgsh0:not([disabled]):focus{box-shadow:0 0 0 2px var(--accent-primary-default);}.css-4jgsh0:not([disabled]):focus:not(:focus-visible){box-shadow:none;}.css-4jgsh0:not([disabled]):active{background-color:var(--interactive-background--active);border-color:var(--accent-primary-default);}</style><style data-emotion="css 37dka1" data-s="">.css-37dka1{display:inline;overflow-wrap:break-word;font-size:var(--font-size-small);line-height:var(--line-height-small);display:inline-block;line-height:1.2;max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}</style><style data-emotion="css 1jkwd0r" data-s="">.css-1jkwd0r{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;display:inline;overflow-wrap:break-word;font-size:var(--font-size-small);line-height:var(--line-height-small);display:inline-block;line-height:1.2;max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}</style><style data-emotion="css ot3nnn" data-s="">.css-ot3nnn{display:inline;overflow-wrap:break-word;font-size:var(--font-size-default);line-height:var(--line-height-default);color:var(--foreground-dimmer);display:inline-block;line-height:1.2;max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}</style><style data-emotion="css 1oxl2rf" data-s="">.css-1oxl2rf{-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;border-width:0;border-style:solid;box-sizing:border-box;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-basis:auto;-ms-flex-preferred-size:auto;flex-basis:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;outline:none;min-height:0;min-width:0;display:inline;overflow-wrap:break-word;font-size:var(--font-size-default);line-height:var(--line-height-default);color:var(--foreground-dimmer);display:inline-block;line-height:1.2;max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}</style><style data-emotion="css" data-s=""></style><style type="text/css" data-styled-jsx="">::-webkit-scrollbar{background-color:var(--background-default);width:12px}::-webkit-scrollbar-track{background-color:var(--background-default)}::-webkit-scrollbar-thumb{background-color:var(--background-highest)}*{scrollbar-color:var(--background-highest)var(--background-default)}</style><link as="script" rel="prefetch" href="./tren_files/about-70c6f2fb2d88000d.js"><link as="script" rel="prefetch" href="./tren_files/478a99c2-02159fed064aeeca.js"><link as="script" rel="prefetch" href="./tren_files/9998-d4e30fee25372672.js"><link as="script" rel="prefetch" href="./tren_files/8944-aed391bc0667f316.js"><link as="script" rel="prefetch" href="./tren_files/9838-bacb7b265d12df33.js"><link as="script" rel="prefetch" href="./tren_files/3827-bdad34917f2692ba.js"><link as="script" rel="prefetch" href="./tren_files/careers-68dbdc4f7cf82bd4.js"><link as="script" rel="prefetch" href="./tren_files/pricing-a26550c41acb98dd.js"><link as="script" rel="prefetch" href="./tren_files/57e613a8-3ed1371a918db159.js"><link as="script" rel="prefetch" href="./tren_files/3f2dd09b-bfaa032fa490e8e6.js"><link as="script" rel="prefetch" href="./tren_files/4778-cecee814d89c42b0.js"><link as="script" rel="prefetch" href="./tren_files/4969-54c212da5ac9ac53.js"><link as="script" rel="prefetch" href="./tren_files/8966-2b1dbb45e840d999.js"><link as="script" rel="prefetch" href="./tren_files/6354-fc89656571f27b2b.js"><link as="script" rel="prefetch" href="./tren_files/9710-216e9a268a3533fc.js"><link as="script" rel="prefetch" href="./tren_files/8754-73bd34ec23ba1630.js"><link as="script" rel="prefetch" href="./tren_files/3220-3a5f8291109e291b.js"><link as="script" rel="prefetch" href="./tren_files/40-9b0a34711cb1f54c.js"><link as="script" rel="prefetch" href="./tren_files/4837-b1bc3e3354da413c.js"><link as="script" rel="prefetch" href="./tren_files/5225-5db815d4e7eb6860.js"><link as="script" rel="prefetch" href="./tren_files/9231-e7d77e40da11ce62.js"><link as="script" rel="prefetch" href="./tren_files/4072-d10e775c3062b050.js"><link as="script" rel="prefetch" href="./tren_files/9907-88c23590c99cd942.js"><link as="script" rel="prefetch" href="./tren_files/4798-280992e4a348cd62.js"><link as="script" rel="prefetch" href="./tren_files/1-8e8e573a4e791b02.js"><link as="script" rel="prefetch" href="./tren_files/2911-580399270cfd1a8b.js"><link as="script" rel="prefetch" href="./tren_files/8418-341365a33c5c951d.js"><link as="script" rel="prefetch" href="./tren_files/2791-d36670285a4ea0f7.js"><link as="script" rel="prefetch" href="./tren_files/4625-8086e7ddf12cc447.js"><link as="script" rel="prefetch" href="./tren_files/490-44b4143e4699f720.js"><link as="script" rel="prefetch" href="./tren_files/3358-415e53e976de0da9.js"><link as="script" rel="prefetch" href="./tren_files/3875-e27316a90a96003e.js"><link as="script" rel="prefetch" href="./tren_files/6658-2edceb3e26f267a8.js"><link as="script" rel="prefetch" href="./tren_files/7913-1e6a0d833e9d20d1.js"><link as="script" rel="prefetch" href="./tren_files/8561-d6ef177eb7b21b84.js"><link as="script" rel="prefetch" href="./tren_files/5685-771fa0052cb7258c.js"><link as="script" rel="prefetch" href="./tren_files/5556-2e2d9c13f2bac141.js"><link as="script" rel="prefetch" href="./tren_files/profile2-79bea7df5bf9e5eb.js"><script src="./tren_files/api.js"></script><style type="text/css" data-styled-jsx="">svg.jsx-439304857{min-width:20px;min-height:20px;
            
          }</style><style type="text/css" data-styled-jsx="">.toggle-bars-wrapper.jsx-3885735894{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;height:100%;width:48px;position:relative}.toggle-bar.jsx-3885735894{height:2px;width:18px;background-color:var(--foreground-dimmer);-webkit-transition:.1s background-color;-moz-transition:.1s background-color;-o-transition:.1s background-color;transition:.1s background-color}.toggle-bars-wrapper.jsx-3885735894:hover .toggle-bar.jsx-3885735894{background-color:var(--foreground-default)}.sidebar-layout-header-toggle-alert.jsx-3885735894{background-color:var(--accent-negative-default);width:8px;height:8px;position:absolute;top:19px;right:11px;-webkit-border-radius:50%;-moz-border-radius:50%;border-radius:50%}.workspace-wrapper.lite button{display:none}</style><style type="text/css" data-styled-jsx="">.profile-icon.jsx-e5cf02fb0196d98c{display:block;-webkit-background-size:cover;-moz-background-size:cover;-o-background-size:cover;background-size:cover;-webkit-border-radius:100%;-moz-border-radius:100%;border-radius:100%;background-color:#fff;background-position:center;position:relative;border:1px solid var(--outline-dimmest)}.profile-icon-xxs.jsx-e5cf02fb0196d98c{width:12px;min-width:12px;height:12px;min-height:12px}.profile-icon-xs.jsx-e5cf02fb0196d98c{width:14px;min-width:14px;height:14px;min-height:14px}.profile-icon-s.jsx-e5cf02fb0196d98c{width:16px;min-width:16px;height:16px;min-height:16px}.profile-icon-m.jsx-e5cf02fb0196d98c{width:24px;min-width:24px;height:24px;min-height:24px}.profile-icon-l.jsx-e5cf02fb0196d98c{width:64px;min-width:64px;height:64px;min-height:64px}.profile-icon-xl.jsx-e5cf02fb0196d98c{width:128px;min-width:128px;height:128px;min-height:128px}.profile-icon-inherit.jsx-e5cf02fb0196d98c{width:100%}.profile-icon-inherit.jsx-e5cf02fb0196d98c img.jsx-e5cf02fb0196d98c{display:block;width:100%;height:100%}.profile-icon.jsx-e5cf02fb0196d98c>span.jsx-e5cf02fb0196d98c{position:absolute;right:0;bottom:0}</style><style type="text/css" data-styled-jsx="">.avatar-dropdown.jsx-b0dcf9530d423282{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center}.user-image.jsx-b0dcf9530d423282{-webkit-box-flex:0;-webkit-flex:0 0 auto;-moz-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto;width:var(--space-32);height:var(--space-32);margin-right:var(--space-8)}.menu-container.jsx-b0dcf9530d423282{width:164px}button.jsx-b0dcf9530d423282{position:relative;outline:0 none;border:0 none;cursor:pointer;background-color:transparent;color:var(--foreground-dimmest)}button.jsx-b0dcf9530d423282:hover{color:var(--foreground-default)}.button-content.jsx-b0dcf9530d423282{display:grid;grid-template-columns:1fr auto;grid-column-gap:var(--space-4)}.username.jsx-b0dcf9530d423282{font-size:14px;text-align:left;overflow:hidden;-o-text-overflow:ellipsis;text-overflow:ellipsis;white-space:nowrap;color:var(--foreground-default)}.dropdown-carat.jsx-b0dcf9530d423282{width:8px;-webkit-box-flex:0;-webkit-flex:0 0 auto;-moz-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto;color:var(--foreground-default)}.dropdown-carat.jsx-b0dcf9530d423282 svg.jsx-b0dcf9530d423282{width:100%;height:auto}</style><style type="text/css" data-styled-jsx="">.notifications-menu.jsx-5116699e4c242317{position:relative;height:100%;display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;color:var(--foreground-default)}button.jsx-5116699e4c242317:active,button.jsx-5116699e4c242317:focus{outline:0 none}button.jsx-5116699e4c242317{position:relative;cursor:pointer;padding:0;margin:0;background-color:transparent;border:0 none;padding-left:var(--space-8);padding-right:var(--space-8);height:100%;color:inherit}.icon-wrap.jsx-5116699e4c242317{color:var(--foreground-dimmer);-webkit-transition:color.2s;-moz-transition:color.2s;-o-transition:color.2s;transition:color.2s}.icon-wrap.jsx-5116699e4c242317:hover,.icon-wrap.jsx-5116699e4c242317:active{color:var(--foreground-default)}.menu-header.jsx-5116699e4c242317{padding:var(--space-8)var(--space-16);display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex}.menu-header.jsx-5116699e4c242317 a.jsx-5116699e4c242317{margin-left:auto;color:var(--accent-primary-default);font-size:var(--font-size-default);padding:1px 2px;-webkit-border-radius:var(--border-radius-4);-moz-border-radius:var(--border-radius-4);border-radius:var(--border-radius-4);-webkit-transition:.2s background-color;-moz-transition:.2s background-color;-o-transition:.2s background-color;transition:.2s background-color;text-decoration:none!important;font-weight:var(--font-weight-medium)}.menu-header.jsx-5116699e4c242317 a.jsx-5116699e4c242317:hover{background-color:var(--background-higher)}.menu-list.jsx-5116699e4c242317{overflow-y:auto;max-height:50vh}.unread-count.jsx-5116699e4c242317{position:absolute;pointer-events:none;color:var(--accent-negative-strongest);-webkit-border-radius:var(--border-radius-round);-moz-border-radius:var(--border-radius-round);border-radius:var(--border-radius-round);padding:var(--space-2)var(--space-4);background-color:var(--accent-negative-dimmer);margin-left:auto;min-width:16px;text-align:center;-webkit-box-flex:0;-webkit-flex:0 0 auto;-moz-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto;top:-6px;right:0px;font-size:var(--font-size-small)}</style><style type="text/css" data-styled-jsx="">svg.jsx-3164811897{min-width:16px;min-height:16px;
            
          }</style><style type="text/css" data-styled-jsx="">div.jsx-1533201384{width:var(--space-8);height:var(--space-8);-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;pointer-events:none}</style><style type="text/css" data-styled-jsx="">a.jsx-2901067024{display:block;padding:var(--space-8);display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;font-size:var(--font-size-subhead-default);color:var(--foreground-default);-webkit-border-radius:var(--border-radius-4);-moz-border-radius:var(--border-radius-4);border-radius:var(--border-radius-4);margin-bottom:var(--space-4)}a.jsx-2901067024:hover{text-decoration:none;background-color:var(--background-higher);text-decoration:none;-webkit-transition:color.1s;-moz-transition:color.1s;-o-transition:color.1s;transition:color.1s}a.jsx-2901067024:focus,a.jsx-2901067024:active{background-color:var(--background-higher);text-decoration:none}a.sidebar-layout-nav-item-active.jsx-2901067024{text-decoration:none;background-color:var(--accent-primary-dimmest)}.sidebar-layout-nav-item-icon.jsx-2901067024{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;width:var(--space-16);height:var(--space-16);margin-right:var(--space-8);-webkit-box-flex:0;-webkit-flex:0 0 auto;-moz-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto;opacity:0.75;color:var(--foreground-default)}.sidebar-layout-nav-item-active.jsx-2901067024 .sidebar-layout-nav-item-icon.jsx-2901067024{color:var(--accent-primary-strongest)}a.jsx-2901067024 svg{width:100%;height:auto}a.secondary.jsx-2901067024{opacity:1}.beta-label.jsx-2901067024{margin-left:auto}@media screen and (min-width:700px){a.secondary.jsx-2901067024{padding-top:0px;padding-bottom:0px;font-size:13px;height:25px}}</style><style type="text/css" data-styled-jsx="">.app-sidebar-blanket.jsx-4231112091{position:absolute;top:0;left:0;background-color:var(--background-default);opacity:.8;width:100%;height:100%;z-index:10;pointer-events:none;display:none}.new-repl-cta.jsx-4231112091{padding-bottom:var(--space-8);display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;-moz-box-orient:vertical;-moz-box-direction:normal;-ms-flex-direction:column;flex-direction:column;-webkit-box-align:stretch;-webkit-align-items:stretch;-moz-box-align:stretch;-ms-flex-align:stretch;align-items:stretch}.header.jsx-4231112091{padding-left:48px;height:60px;width:240px}.header-content.jsx-4231112091{height:100%;display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;position:relative;padding-right:var(--space-8);opacity:0;-webkit-transition:opacity 200ms;-moz-transition:opacity 200ms;-o-transition:opacity 200ms;transition:opacity 200ms;-webkit-transition-delay:0s;-moz-transition-delay:0s;-o-transition-delay:0s;transition-delay:0s}.header-content.is-open.jsx-4231112091{opacity:1;-webkit-transition-delay:100ms;-moz-transition-delay:100ms;-o-transition-delay:100ms;transition-delay:100ms}.notifications.jsx-4231112091{margin-left:auto;-webkit-box-flex:0;-webkit-flex:0 0 auto;-moz-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto}.scroll-container.jsx-4231112091{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;-moz-box-orient:vertical;-moz-box-direction:normal;-ms-flex-direction:column;flex-direction:column;overflow-y:auto}.sidebar-layout-nav-top.jsx-4231112091{padding:var(--space-2)var(--space-8)var(--space-8)var(--space-8);display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;-moz-box-orient:vertical;-moz-box-direction:normal;-ms-flex-direction:column;flex-direction:column}.sidebar-bottom.jsx-4231112091{margin-top:auto;display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-pack:justify;-webkit-justify-content:space-between;-moz-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between;-webkit-box-align:end;-webkit-align-items:flex-end;-moz-box-align:end;-ms-flex-align:end;align-items:flex-end;padding:0 var(--space-16)var(--space-24)}.sidebar-bottom.jsx-4231112091>ul.jsx-4231112091{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;-moz-box-orient:vertical;-moz-box-direction:normal;-ms-flex-direction:column;flex-direction:column;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap}.sidebar-bottom.jsx-4231112091>ul.jsx-4231112091{padding-top:var(--space-8)}.sidebar-bottom.jsx-4231112091>ul.jsx-4231112091 a.jsx-4231112091{margin-right:var(--space-8);margin-top:var(--space-4);font-size:var(--font-size-default);text-transform:capitalize;color:var(--foreground-dimmest)}.sidebar-bottom.jsx-4231112091>ul.jsx-4231112091 a.jsx-4231112091:hover{color:var(--accent-primary-stronger)}.help-and-themes.jsx-4231112091{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;-moz-box-orient:vertical;-moz-box-direction:normal;-ms-flex-direction:column;flex-direction:column;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center}.theme-switcher.jsx-4231112091{padding-bottom:var(--space-8)}.help-resources.jsx-4231112091{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;text-decoration:none;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;padding:var(--space-8);color:var(--foreground-default);-webkit-border-radius:var(--border-radius-4);-moz-border-radius:var(--border-radius-4);border-radius:var(--border-radius-4);margin-top:var(--space-16);cursor:pointer}.help-icon-wrapper.jsx-4231112091{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;height:var(--space-16);width:var(--space-16);opacity:.75}.help-resources.jsx-4231112091>span.jsx-4231112091{margin-left:var(--space-8)}.help-resources.jsx-4231112091:hover{text-decoration:none;background-color:var(--background-higher);-webkit-transition:color.1s;-moz-transition:color.1s;-o-transition:color.1s;transition:color.1s}.help-resources.jsx-4231112091:hover.help-icon-wrapper{opacity:1}.help-button.jsx-4231112091{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;width:var(--space-24);height:var(--space-24);-webkit-box-flex:0;-webkit-flex:0 0 auto;-moz-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto;font-size:20px}.explore-link.jsx-4231112091{position:relative;padding:var(--space-8)}</style><style type="text/css" data-styled-jsx="">.floating-messages.jsx-cf05928fd4789ae{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;position:fixed;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;-moz-box-orient:vertical;-moz-box-direction:normal;-ms-flex-direction:column;flex-direction:column;-webkit-box-align:end;-webkit-align-items:flex-end;-moz-box-align:end;-ms-flex-align:end;align-items:flex-end;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;z-index:1000000;bottom:var(--space-24);right:var(--space-24);margin:0}.floating-message.jsx-cf05928fd4789ae{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;text-align:center;font-size:var(--font-size-subhead-default);padding:var(--space-16);margin-top:var(--space-4);-webkit-font-smoothing:antialiased;-webkit-border-radius:var(--border-radius-4);-moz-border-radius:var(--border-radius-4);border-radius:var(--border-radius-4);color:var(--white);font-weight:var(--font-weight-medium)}.floating-message.floating-message-error.jsx-cf05928fd4789ae{background-color:var(--accent-negative-dimmer)}.floating-message.floating-message-confirm.jsx-cf05928fd4789ae{background-color:var(--accent-positive-dimmer)}.floating-message.floating-message-notice.jsx-cf05928fd4789ae{background-color:var(--accent-negative-dimmer)}</style><style type="text/css" data-styled-jsx="">html,body{scrollbar-width:none}</style><style type="text/css" data-styled-jsx="">.workspace-page-wrapper.jsx-849e56f81ae5af67{height:100%;width:100%;position:fixed;left:0px;right:0px;top:0;bottom:0px;background-color:var(--background-root)}.workspace-page-wrapper.desktop.jsx-849e56f81ae5af67{padding:var(--space-8);padding-top:0}.banner+.content>.workspace-page-wrapper.jsx-849e56f81ae5af67{height:-webkit-calc(100% - 36px);height:-moz-calc(100% - 36px);height:calc(100% - 36px);top:36px}</style><style type="text/css" data-styled-jsx="">#nprogress{pointer-events:none}.nprogress-bar{background:var(--accent-primary-default);position:fixed;z-index:400001;top:0;left:0;width:100%;height:2px}.nprogress-static-css-bar{width:0;-webkit-animation:10s ease-out 750ms 1 normal both running nprogress-widen;-moz-animation:10s ease-out 750ms 1 normal both running nprogress-widen;-o-animation:10s ease-out 750ms 1 normal both running nprogress-widen;animation:10s ease-out 750ms 1 normal both running nprogress-widen}@-webkit-keyframes nprogress-widen{0%{width:0}100%{width:90%}}@-moz-keyframes nprogress-widen{0%{width:0}100%{width:90%}}@-o-keyframes nprogress-widen{0%{width:0}100%{width:90%}}@keyframes nprogress-widen{0%{width:0}100%{width:90%}}.nprogress-peg{display:block;position:absolute;right:0px;width:100px;height:100%;-webkit-box-shadow:0 0 10px var(--accent-primary-default),0 0 5px var(--accent-primary-default);-moz-box-shadow:0 0 10px var(--accent-primary-default),0 0 5px var(--accent-primary-default);box-shadow:0 0 10px var(--accent-primary-default),0 0 5px var(--accent-primary-default);opacity:1;-webkit-transform:rotate(3deg)translate(0px,-4px);-ms-transform:rotate(3deg)translate(0px,-4px);-moz-transform:rotate(3deg)translate(0px,-4px);-o-transform:rotate(3deg)translate(0px,-4px);transform:rotate(3deg)translate(0px,-4px)}</style><style type="text/css" data-styled-jsx="">.toggle.jsx-1734542601{position:fixed;top:0;left:0;z-index:1003;width:48px;height:60px}.content.jsx-1734542601{background-color:var(--background-root);min-height:100vh;width:100%;position:relative;padding-top:60px}.banner.jsx-1734542601{position:absolute;top:60px;left:0;width:100%;z-index:1}.no-header.jsx-1734542601 .content.jsx-1734542601{padding-top:0;min-height:100vh}.banner.jsx-1734542601+.content.jsx-1734542601{margin-top:32px;min-height:-webkit-calc(100vh - 32px);min-height:-moz-calc(100vh - 32px);min-height:calc(100vh - 32px)}.overlay.jsx-1734542601{display:block;position:fixed;top:0;left:0;width:100%;height:100%;background-color:var(--background-overlay);z-index:1001;pointer-events:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;opacity:0;-webkit-transition:.2s opacity;-moz-transition:.2s opacity;-o-transition:.2s opacity;transition:.2s opacity}.sidebar-open.jsx-1734542601 .overlay.jsx-1734542601{pointer-events:all;opacity:1}@media screen and (min-width:768px){.sidebar-open.jsx-1734542601{padding-left:240px}.sidebar-open.drawer.jsx-1734542601{padding-left:0}.sidebar-open.jsx-1734542601 .overlay.jsx-1734542601{display:none}.sidebar-open.drawer.jsx-1734542601 .overlay.jsx-1734542601{display:block}}@media screen and (max-width:480px){.toggle.is-hidden.jsx-1734542601{display:none}.content.jsx-1734542601{overflow-x:hidden}}</style><style type="text/css" data-styled-jsx="">.oldModalOverlay{position:fixed;top:0;right:0;bottom:0;left:0;overflow:auto;z-index:300000;background-color:var(--background-overlay);-webkit-transition:opacity 100ms;-moz-transition:opacity 100ms;-o-transition:opacity 100ms;transition:opacity 100ms;opacity:0;padding:0 var(--space-16)}.oldModalContent{margin:20vh auto;outline:none;position:relative;background-color:var(--background-default);-webkit-box-shadow:var(--shadow-2);-moz-box-shadow:var(--shadow-2);box-shadow:var(--shadow-2);-webkit-border-radius:var(--border-radius-8);-moz-border-radius:var(--border-radius-8);border-radius:var(--border-radius-8);border:1px solid var(--background-highest)}.oldModalOverlay.is-open{opacity:1}.close-control.jsx-1990811228{position:absolute;top:0;right:0;-webkit-transform:translate(0,-webkit-calc(-100% - var(--space-8)));-moz-transform:translate(0,-moz-calc(-100% - var(--space-8)));-ms-transform:translate(0,calc(-100% - var(--space-8)));-o-transform:translate(0,calc(-100% - var(--space-8)));transform:translate(0,-webkit-calc(-100% - var(--space-8)));transform:translate(0,-moz-calc(-100% - var(--space-8)));transform:translate(0,calc(-100% - var(--space-8)))}</style><style type="text/css" data-styled-jsx="">.side-nav-item.jsx-fec3cffb12bc633b{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;cursor:pointer;-webkit-border-radius:var(--border-radius-4);-moz-border-radius:var(--border-radius-4);border-radius:var(--border-radius-4);height:-webkit-calc(var(--space-48) - var(--space-8));height:-moz-calc(var(--space-48) - var(--space-8));height:calc(var(--space-48) - var(--space-8));width:-webkit-calc(var(--space-48) - var(--space-8));width:-moz-calc(var(--space-48) - var(--space-8));width:calc(var(--space-48) - var(--space-8));margin-bottom:var(--space-4)}.side-nav-item.jsx-fec3cffb12bc633b:hover{background:var(--background-higher)}.side-nav-item.jsx-fec3cffb12bc633b:active{background:var(--background-higher)}.side-nav-item-active.jsx-fec3cffb12bc633b{background:var(--accent-primary-dimmest);color:var(--foreground-default)}.side-nav-item-img.jsx-fec3cffb12bc633b{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;height:20px;width:20px;color:var(--foreground-dimmest)}.side-nav-item-img.jsx-fec3cffb12bc633b svg.jsx-fec3cffb12bc633b{height:100%;width:100%}.side-nav-item.jsx-fec3cffb12bc633b:hover .side-nav-item-img.jsx-fec3cffb12bc633b,.side-nav-item-active.jsx-fec3cffb12bc633b .side-nav-item-img.jsx-fec3cffb12bc633b{color:var(--accent-primary-strongest)}</style><style type="text/css" data-styled-jsx="">.side-nav.jsx-47d475dde80a5cb8{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;-moz-box-orient:vertical;-moz-box-direction:normal;-ms-flex-direction:column;flex-direction:column;height:100%;background-color:var(--background-default);-webkit-border-top-left-radius:var(--border-radius-4);-moz-border-radius-topleft:var(--border-radius-4);border-top-left-radius:var(--border-radius-4);-webkit-border-bottom-left-radius:var(--border-radius-4);-moz-border-radius-bottomleft:var(--border-radius-4);border-bottom-left-radius:var(--border-radius-4);border-right:1px solid var(--background-higher)}.side-nav-options.jsx-47d475dde80a5cb8{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;-moz-box-orient:vertical;-moz-box-direction:normal;-ms-flex-direction:column;flex-direction:column;width:100%;height:100%;padding:var(--space-4)0}.side-nav-active-pane.jsx-47d475dde80a5cb8{-webkit-box-flex:1;-webkit-flex:1;-moz-box-flex:1;-ms-flex:1;flex:1;height:100%;overflow:hidden}</style><style type="text/css" data-styled-jsx="">.heading.jsx-2181209103{font-size:var(--font-size-subhead-big);font-family:var(--font-family-default);font-weight:var(--font-weight-medium);color:var(--foreground-default);text-align:left}.truncate.jsx-2181209103{overflow:hidden;white-space:nowrap;-o-text-overflow:ellipsis;text-overflow:ellipsis;max-width:100%}</style><style type="text/css" data-styled-jsx="">button.jsx-3998413586{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;font-size:var(--font-size-default);font-family:var(--font-family-default);-webkit-border-radius:var(--border-radius-4);-moz-border-radius:var(--border-radius-4);border-radius:var(--border-radius-4);cursor:pointer;outline:0;padding:var(--space-8);text-align:center;-webkit-transition:.1s all ease-in-out;-moz-transition:.1s all ease-in-out;-o-transition:.1s all ease-in-out;transition:.1s all ease-in-out;font-weight:var(--font-weight-medium);width:auto;white-space:nowrap;line-height:var(--font-size-default)}button.default.jsx-3998413586{background-color:var(--background-default);border:1px solid var(--background-default);color:var(--foreground-dimmer)}button.default.jsx-3998413586:hover{background-color:var(--background-default);border:1px solid inherit;color:var(--foreground-dimmer)}button.default.jsx-3998413586:active{background-color:var(--background-default)}button.default.jsx-3998413586:focus{outline-offset:2px;-webkit-box-shadow:0 0 0 3px var(--accent-primary-default);-moz-box-shadow:0 0 0 3px var(--accent-primary-default);box-shadow:0 0 0 3px var(--accent-primary-default)}button.jsx-3998413586:disabled{opacity:.5;pointer-events:none}.content.jsx-3998413586{margin:0 0 0 var(--space-4)}.icon-container.jsx-3998413586{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;color:currentColor;-webkit-box-ordinal-group:0;-webkit-order:0;-moz-box-ordinal-group:0;-ms-flex-order:0;order:0}@media only screen and (max-width:480px){.content.jsx-3998413586{display:inherit;margin:0 0 0 var(--space-4)}}</style><style type="text/css" data-styled-jsx="">.node-actions-menu.jsx-3436279308{position:relative;width:20px;height:100%}.is-touch-device .protip.jsx-3436279308{display:none}.protip.jsx-3436279308{font-size:13px;padding:10px 5px;text-align:center;color:var(--foreground-default);border-top:1px solid var(--outline-dimmest)}.protip.jsx-3436279308>span.jsx-3436279308{color:var(--accent-positive-default);font-weight:var(--font-weight-bold);font-size:12px}button.jsx-3436279308{top:0;width:100%;height:100%;display:block;background-color:transparent;border:0 none;cursor:pointer;color:var(--foreground-dimmest);-webkit-border-radius:var(--border-radius-4);-moz-border-radius:var(--border-radius-4);border-radius:var(--border-radius-4)}button.jsx-3436279308:hover{color:var(--foreground-default)}ul.jsx-3436279308{width:130px;display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;-moz-box-orient:vertical;-moz-box-direction:normal;-ms-flex-direction:column;flex-direction:column;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;background-color:var(--background-default);-webkit-border-radius:var(--border-radius-4);-moz-border-radius:var(--border-radius-4);border-radius:var(--border-radius-4);-webkit-box-shadow:var(--shadow-2);-moz-box-shadow:var(--shadow-2);box-shadow:var(--shadow-2);list-style:none;position:absolute;right:var(--space-8);top:-webkit-calc(100% - var(--space-8));top:-moz-calc(100% - var(--space-8));top:calc(100% - var(--space-8));z-index:1}ul.jsx-3436279308:focus{outline:none}</style><style type="text/css" data-styled-jsx="">input.jsx-2ff4f6cb1b2dc3a5{display:none}</style><style type="text/css" data-styled-jsx="">div.jsx-2967244382{display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:flex-start;-webkit-justify-content:flex-start;-moz-box-pack:flex-start;-ms-flex-pack:flex-start;justify-content:flex-start;-webkit-flex-wrap:nowrap;-ms-flex-wrap:nowrap;flex-wrap:nowrap}.h-stack.jsx-2967244382>*{margin-right:0}.h-stack.jsx-2967244382>*:last-child{margin-right:0}.v-stack.jsx-2967244382>*{margin-bottom:0}.v-stack.jsx-2967244382>*:last-child{margin-bottom:0}.constrain-width.jsx-2967244382{max-width:100%}</style><style type="text/css" data-styled-jsx="">.dir-node.jsx-87d0738bc3f946a6{-webkit-border-radius:var(--border-radius-4);-moz-border-radius:var(--border-radius-4);border-radius:var(--border-radius-4);width:100%}.root-node.jsx-87d0738bc3f946a6{overflow-y:auto;-webkit-box-flex:1;-webkit-flex-grow:1;-moz-box-flex:1;-ms-flex-positive:1;flex-grow:1;padding:var(--space-8);padding-top:0}.node-info.jsx-87d0738bc3f946a6{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;overflow:hidden;-webkit-box-flex:1;-webkit-flex-grow:1;-moz-box-flex:1;-ms-flex-positive:1;flex-grow:1}.hidden.jsx-87d0738bc3f946a6{display:none;height:0;width:0}.is-removing.jsx-87d0738bc3f946a6{opacity:.5;pointer-events:none}.is-dropping.jsx-87d0738bc3f946a6{background-color:var(--accent-primary-dimmer)}.is-dragging.jsx-87d0738bc3f946a6{opacity:.7}</style><style type="text/css" data-styled-jsx="">.filetree.jsx-2474109695{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;-moz-box-orient:vertical;-moz-box-direction:normal;-ms-flex-direction:column;flex-direction:column;height:100%;overflow:hidden;-webkit-border-top-right-radius:var(--border-radius-4);-moz-border-radius-topright:var(--border-radius-4);border-top-right-radius:var(--border-radius-4);-webkit-border-bottom-right-radius:var(--border-radius-4);-moz-border-radius-bottomright:var(--border-radius-4);border-bottom-right-radius:var(--border-radius-4);background-color:var(--background-default);min-height:auto}.filetree.jsx-2474109695 .filetree-header{padding:var(--space-8);background-color:var(--background-default);position:-webkit-sticky;position:sticky;top:0;z-index:1}.filetree-action-separator.jsx-2474109695{height:6px;width:0;border-right:1px solid var(--foreground-dimmest)}.add-button:hover{color:var(--foreground-default)!important}.heading.jsx-2474109695{margin-right:auto}</style><style type="text/css" data-styled-jsx="">.file-header.jsx-3113332693{position:relative;z-index:3;display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;height:48px;width:100%;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:start;-webkit-justify-content:flex-start;-moz-box-pack:start;-ms-flex-pack:start;justify-content:flex-start;background-color:var(--background-root);-webkit-border-top-right-radius:var(--border-radius-4);-moz-border-radius-topright:var(--border-radius-4);border-top-right-radius:var(--border-radius-4);-webkit-border-top-left-radius:var(--border-radius-4);-moz-border-radius-topleft:var(--border-radius-4);border-top-left-radius:var(--border-radius-4);-webkit-box-shadow:0;-moz-box-shadow:0;box-shadow:0;-webkit-clip-path:none;clip-path:none}.file-header.jsx-3113332693 .os-host{height:100%;-webkit-box-flex:1;-webkit-flex:auto;-moz-box-flex:1;-ms-flex:auto;flex:auto;min-width:0}.os-content-glue{height:50px!important}.file-header.jsx-3113332693 .os-scrollbar-handle{max-width:300px}.file-header-name.jsx-3113332693{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;width:100%;background-color:var(--background-root);color:var(--foreground-dimmer);font-size:var(--font-size-default);height:100%;text-align:center;-webkit-box-align:end;-webkit-align-items:flex-end;-moz-box-align:end;-ms-flex-align:end;align-items:flex-end}.loading-wrapper.jsx-3113332693{position:absolute;bottom:0;left:0;right:0;height:2px;overflow:hidden}.file-header-loading-bar.jsx-3113332693{width:40px;height:2px;position:absolute;bottom:0;left:0;background:var(--background-higher);-webkit-animation:loading-bar-move 2.5s ease-in-out 0s infinite;-moz-animation:loading-bar-move 2.5s ease-in-out 0s infinite;-o-animation:loading-bar-move 2.5s ease-in-out 0s infinite;animation:loading-bar-move 2.5s ease-in-out 0s infinite;-webkit-animation-fill-mode:forward;-moz-animation-fill-mode:forward;-o-animation-fill-mode:forward;animation-fill-mode:forward}@-webkit-keyframes loading-bar-move{0%{left:-7%}100%{left:105%}}@-moz-keyframes loading-bar-move{0%{left:-7%}100%{left:105%}}@-o-keyframes loading-bar-move{0%{left:-7%}100%{left:105%}}@keyframes loading-bar-move{0%{left:-7%}100%{left:105%}}</style><style type="text/css" data-styled-jsx="">button.jsx-985b6491a57edf8a{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;-webkit-border-radius:var(--border-radius-4);-moz-border-radius:var(--border-radius-4);border-radius:var(--border-radius-4);padding:var(--space-4);background-color:var(--background-root);color:var(--foreground-default);-webkit-transition:background-color.2s;-moz-transition:background-color.2s;-o-transition:background-color.2s;transition:background-color.2s;border:none;cursor:pointer}button.jsx-985b6491a57edf8a:hover{background-color:var(--background-higher)}button.jsx-985b6491a57edf8a:focus{outline:none}</style><style type="text/css" data-styled-jsx="">.xterm .xterm-viewport{overflow-y:auto!important}</style><style type="text/css" data-styled-jsx="">.console.jsx-c6ae3a1d7966c39d{height:100%;position:relative;background-color:var(--background-default);-webkit-border-radius:var(--border-radius-4);-moz-border-radius:var(--border-radius-4);border-radius:var(--border-radius-4);overflow:hidden;padding-left:1em;padding-top:10px;z-index:1}.controls.jsx-c6ae3a1d7966c39d{position:absolute;top:var(--space-8);right:var(--space-16);z-index:5;opacity:0}.console.jsx-c6ae3a1d7966c39d:hover .controls.jsx-c6ae3a1d7966c39d{opacity:1}.xterm-container.jsx-c6ae3a1d7966c39d{width:100%;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;height:100%}</style><style type="text/css" data-styled-jsx="">.floating-run.jsx-3788974936{display:none;position:absolute;bottom:24px;right:24px;height:50px;width:50px;-webkit-border-radius:100%;-moz-border-radius:100%;border-radius:100%;border:solid 2px var(--accent-positive-dimmer);cursor:pointer;background-image:url(/public/images/run_green.svg);-webkit-background-size:20px 20px;-moz-background-size:20px 20px;-o-background-size:20px 20px;background-size:20px 20px;background-position:center;background-repeat:no-repeat;background-color:var(--accent-positive-dimmest);z-index:1000;opacity:.5}.floating-run-loading.jsx-3788974936{background-image:url(/public/images/loading_dots.gif)}.floating-run-stop.jsx-3788974936{background-image:url(/public/images/stop_green.svg)}.run-cta.jsx-3788974936{background:var(--accent-primary-default);padding:var(--space-16);color:var(--white);-webkit-border-radius:var(--border-radius-4);-moz-border-radius:var(--border-radius-4);border-radius:var(--border-radius-4)}@media screen and (max-width:580px){.floating-run.jsx-3788974936{display:block}}</style><style type="text/css" data-styled-jsx="">.help-container.jsx-9a1cd8c5ee126c5d{position:absolute;left:var(--space-8);bottom:var(--space-16);z-index:20;display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;width:var(--space-32);height:var(--space-32);cursor:pointer;-webkit-border-radius:100%;-moz-border-radius:100%;border-radius:100%;background-color:var(--background-default);color:var(--foreground-dimmer);border:1px solid var(--background-highest);-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-box-shadow:var(--shadow-1);-moz-box-shadow:var(--shadow-1);box-shadow:var(--shadow-1);-webkit-transition:.1s;-moz-transition:.1s;-o-transition:.1s;transition:.1s}.help-container.jsx-9a1cd8c5ee126c5d:hover{border:1px solid var(--outline-default);-webkit-box-shadow:var(--shadow-2);-moz-box-shadow:var(--shadow-2);box-shadow:var(--shadow-2)}.help-container.jsx-9a1cd8c5ee126c5d:active{border:1px solid var(--accent-primary-default);-webkit-box-shadow:var(--shadow-1);-moz-box-shadow:var(--shadow-1);box-shadow:var(--shadow-1)}</style><style type="text/css" data-styled-jsx="">.chat-icon-svg{width:100%;height:100%}.chat-icon-svg .cls-1{fill:currentColor}</style><style type="text/css" data-styled-jsx="">.floating-icon-wrapper.jsx-2993337382{height:36px;width:50px;-webkit-border-radius:var(--border-radius-8) 0 0 var(--border-radius-8);-moz-border-radius:var(--border-radius-8) 0 0 var(--border-radius-8);border-radius:var(--border-radius-8) 0 0 var(--border-radius-8);position:absolute;right:0px;bottom:var(--space-16);z-index:10;display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;cursor:pointer;opacity:1;-webkit-transition:300ms;-moz-transition:300ms;-o-transition:300ms;transition:300ms}.chat-icon-wrapper.jsx-2993337382{width:32px;height:32px;padding:5px;color:#fff}.unread-icon.jsx-2993337382{position:absolute;top:5px;left:12px;background:red;width:8px;height:8px;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px;z-index:11}</style><style type="text/css" data-styled-jsx="">.annotations-container.jsx-31cde6afe9fc4a3c{z-index:10;position:absolute;height:0;width:0}.new-annotation-button.jsx-31cde6afe9fc4a3c{position:absolute;-webkit-transform:translateY(-webkit-calc(-100% - 8px))translateX(56px);-moz-transform:translateY(-moz-calc(-100% - 8px))translateX(56px);-ms-transform:translateY(calc(-100% - 8px))translateX(56px);-o-transform:translateY(calc(-100% - 8px))translateX(56px);transform:translateY(-webkit-calc(-100% - 8px))translateX(56px);transform:translateY(-moz-calc(-100% - 8px))translateX(56px);transform:translateY(calc(-100% - 8px))translateX(56px);-webkit-border-radius:var(--border-radius-4);-moz-border-radius:var(--border-radius-4);border-radius:var(--border-radius-4);background-color:var(--background-higher);color:var(--foreground-default);cursor:pointer;border:.5px solid var(--outline-dimmest);-webkit-box-shadow:var(--shadow-1);-moz-box-shadow:var(--shadow-1);box-shadow:var(--shadow-1);-webkit-transition:width.2s,background-color.2s,-webkit-transform.1s,opacity.2s ease.3s;-moz-transition:width.2s,background-color.2s,-moz-transform.1s,opacity.2s ease.3s;-o-transition:width.2s,background-color.2s,-o-transform.1s,opacity.2s ease.3s;transition:width.2s,background-color.2s,-webkit-transform.1s,opacity.2s ease.3s;transition:width.2s,background-color.2s,-moz-transform.1s,opacity.2s ease.3s;transition:width.2s,background-color.2s,-o-transform.1s,opacity.2s ease.3s;transition:width.2s,background-color.2s,transform.1s,opacity.2s ease.3s;z-index:1;white-space:pre;font-weight:var(--font-weight-medium);font-size:var(--font-size-small);padding:4px 8px;display:grid;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;grid-auto-flow:column;grid-gap:4px}.new-annotation-button.jsx-31cde6afe9fc4a3c:hover{-webkit-transform:translateY(-webkit-calc(-100% - 8px))translateX(56px)scale(1.1);-moz-transform:translateY(-moz-calc(-100% - 8px))translateX(56px)scale(1.1);-ms-transform:translateY(calc(-100% - 8px))translateX(56px)scale(1.1);-o-transform:translateY(calc(-100% - 8px))translateX(56px)scale(1.1);transform:translateY(-webkit-calc(-100% - 8px))translateX(56px)scale(1.1);transform:translateY(-moz-calc(-100% - 8px))translateX(56px)scale(1.1);transform:translateY(calc(-100% - 8px))translateX(56px)scale(1.1)}</style><style type="text/css" data-styled-jsx="">svg.jsx-247521165{width:100%;height:auto}path.jsx-247521165{fill:currentColor}</style><style type="text/css" data-styled-jsx="">div.jsx-584582790{-webkit-border-radius:50%;-moz-border-radius:50%;border-radius:50%;overflow:hidden;width:32px;height:32px}</style><style type="text/css" data-styled-jsx="">.icon.jsx-1114786659{display:none}@media screen and (min-width:1024px){.icon.jsx-1114786659{display:block}}</style><style type="text/css" data-styled-jsx="">.workspace-header-info.jsx-2ea6ce89e086b07b,.workspace-header-title.jsx-2ea6ce89e086b07b{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:start;-webkit-justify-content:start;-moz-box-pack:start;-ms-flex-pack:start;justify-content:start;overflow:hidden;-webkit-flex-wrap:nowrap;-ms-flex-wrap:nowrap;flex-wrap:nowrap;font-size:var(--font-size-default)}.workspace-header-info.jsx-2ea6ce89e086b07b{width:100%}.workspace-header-user-link.jsx-2ea6ce89e086b07b{color:var(--accent-primary-default);text-decoration:none}.language-icon-container.jsx-2ea6ce89e086b07b{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;padding:var(--space-4);background-color:var(--background-higher);-webkit-border-radius:var(--border-radius-8);-moz-border-radius:var(--border-radius-8);border-radius:var(--border-radius-8);position:relative}.breadcrumb.jsx-2ea6ce89e086b07b{display:-webkit-inline-box;display:-webkit-inline-flex;display:-moz-inline-box;display:-ms-inline-flexbox;display:inline-flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;-webkit-border-radius:var(--border-radius-4);-moz-border-radius:var(--border-radius-4);border-radius:var(--border-radius-4);padding:2px var(--space-4);width:auto}.breadcrumb.interactive.jsx-2ea6ce89e086b07b:hover{background-color:var(--background-higher)}.breadcrumb-content.jsx-2ea6ce89e086b07b{display:inline-block;overflow:hidden;-o-text-overflow:ellipsis;text-overflow:ellipsis;max-width:152px}.spacer.jsx-2ea6ce89e086b07b{width:var(--space-8);-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;pointer-events:none}.username.jsx-2ea6ce89e086b07b,.repl-title.jsx-2ea6ce89e086b07b{white-space:nowrap;color:var(--foreground-default)}.slash.jsx-2ea6ce89e086b07b{color:var(--foreground-dimmest);padding:0 2px}.repl-title.jsx-2ea6ce89e086b07b{overflow:hidden}</style><style type="text/css" data-styled-jsx="">header.jsx-2355845231{position:fixed;top:0px;left:0px;width:100%;height:60px;background-color:var(--background-default);border-bottom:.5px solid var(--background-highest);--button-width:60px;--center-width:var(--button-width)}@media screen and (min-width:1024px){header.jsx-2355845231{--button-width:100px}}.logo-link.jsx-2355845231{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;color:var(--foreground-default);width:32px;height:32px}.left.jsx-2355845231,.right.jsx-2355845231{height:100%;padding:0 var(--space-8);display:grid;grid-auto-flow:column;grid-column-gap:var(--space-8);-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center}.left.jsx-2355845231{padding-left:48px;-webkit-box-flex:1;-webkit-flex:1 1 auto;-moz-box-flex:1;-ms-flex:1 1 auto;flex:1 1 auto;-webkit-box-pack:start;-webkit-justify-content:flex-start;-moz-box-pack:start;-ms-flex-pack:start;justify-content:flex-start}.right.jsx-2355845231{-webkit-box-flex:0;-webkit-flex:0 0 auto;-moz-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto;-webkit-box-pack:end;-webkit-justify-content:flex-end;-moz-box-pack:end;-ms-flex-pack:end;justify-content:flex-end}.center.jsx-2355845231{display:none;width:var(--center-width);position:absolute;top:0;left:50%;height:100%;-webkit-transform:translateX(-50%);-moz-transform:translateX(-50%);-ms-transform:translateX(-50%);-o-transform:translateX(-50%);transform:translateX(-50%);padding:var(--space-8)0}.run-button-container.jsx-2355845231{height:100%}.run-button.jsx-2355845231{height:100%}.center.jsx-2355845231>div,.left.jsx-2355845231>div{margin:0!important}.explorer-badge.jsx-2355845231{display:none}@media screen and (min-width:580px){.left.jsx-2355845231,.right.jsx-2355845231{width:50%;-webkit-box-flex:0;-webkit-flex:0 0 auto;-moz-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto}.center.jsx-2355845231{display:block}.left.jsx-2355845231{padding-right:-webkit-calc(var(--center-width)/2 + var(--space-8));padding-right:-moz-calc(var(--center-width)/2 + var(--space-8));padding-right:calc(var(--center-width)/2 + var(--space-8))}.right.jsx-2355845231{padding-left:-webkit-calc(var(--center-width)/2 + var(--space-8));padding-left:-moz-calc(var(--center-width)/2 + var(--space-8));padding-left:calc(var(--center-width)/2 + var(--space-8))}}@media screen and (min-width:480px){.explorer-badge.jsx-2355845231{display:unset;color:var(--foreground-default);-webkit-border-radius:var(--border-radius-8);-moz-border-radius:var(--border-radius-8);border-radius:var(--border-radius-8);background-color:var(--accent-negative-dimmest);height:28px}}</style><link as="script" rel="prefetch" href="./tren_files/1526-edbef23a826a2ef2.js"><link as="script" rel="prefetch" href="./tren_files/1124-42f4320d1af603c1.js"><link as="script" rel="prefetch" href="./tren_files/5191-c4b7fb45714b76ba.js"><link as="script" rel="prefetch" href="./tren_files/3811-d1db0282d6c1f0b2.js"><link as="script" rel="prefetch" href="./tren_files/2037-cf1711fa051f415a.js"><link as="script" rel="prefetch" href="./tren_files/home-dffeb5fad3728a29.js"><style id="replit-icons-font" type="text/css">
@font-face {
  font-family: 'replit-icons';
  font-style: normal;
  font-weight: normal;
  font-stretch: normal;
  src: url(data:application/font-woff;base64,d09GRgABAAAAAAPUAA4AAAAABaQAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAABGRlRNAAADuAAAABwAAAAchB3b2kdERUYAAAOUAAAAJAAAACYAKQAqT1MvMgAAAawAAAA5AAAAYENBXFNjbWFwAAAB+AAAAD4AAAFCAA/yUmN2dCAAAAI4AAAABAAAAAQAIgKIZ2FzcAAAA4wAAAAIAAAACAAAAAFnbHlmAAACSAAAAHwAAACIpDV7CWhlYWQAAAFEAAAAMQAAADYPsR5/aGhlYQAAAXgAAAAYAAAAJAYBBAVobXR4AAAB6AAAABAAAAAQDAAAomxvY2EAAAI8AAAACgAAAAoAbgBUbWF4cAAAAZAAAAAaAAAAIAAIADxuYW1lAAACxAAAAKgAAAFuIGxtGnBvc3QAAANsAAAAHgAAADKwqUy9eJxjYGQAg75rH9bE89t8ZeBmAfOvm9l/AdPWs54wKDEwMDEwrQJyOYAMIAAARtIKWgAAAHicY2BkYGBhAAEIycTAwMiAClgAAWwAEXicY2BkYGBgYeBhYGYAASYGBNADEQADJABFAAB4nGNgZmFgnMDAysDA1MDMAAQNEJoJiBkZ0ACjABInIM01hcHh3fJ3y1nAfBaoGiQlCgyMAFRaBy8AAAAEAAAiAAAAAAQAAAAEAACAeJxjYGBgZoBgGQZGBhCwAfIYwXwWBgUgzQKEQP675f//Q0jBGKhKBkY2BhiTgZEJSDAxoAJGhmEPAP2eCE8AAAAiAogAAAAqACoAKgBEAAB4nGNgYlBiYGA0YlrFwMzAzqC3kZFB32YTOwvDW6ONbKx3bDYxMwGZDBuZQcKsIOFN7GyMf2w2MYLEjQUVBdWNBZWVGAXenTnDtOpvmBJTGgPQpAYGBiYGJgewmdxA80WNTVmBmBmIGR0O/Gs4cOAAI4iAUAwMDAARHSJHeJyNzU0KgzAUBOCJRqE/dFkK3WTnolT0FL1A6QUki4AkEl30GD1Az9BVD9hRX6HQjcbAl5dhAmCHFxS+XyJW2OAoHmcncYotLmLNTCvO6Ic4p99MKr2S1tkKe2p2wlWIUxxwFmtmruKMvotz+jlWRVh0fNZh4G4Q4NFzbLvWDa4Jnof19P8mzX/WSHhJ4Y2ZyKmbbg1qlKg4trF3wZu6rBb1fACKDTLseJxjYGJABowM6IAFLMrEyMRempfp6upoDgAL4gJjAAAAAQAB//8AAHicY2BkYGDgAWIxBjkGJgZGBmYgZGRgAYowATEjBAMACK0AVAAAAAEAAAAA1awBAQAAAADXNj/0AAAAANc7muQ=) format('woff'),
    url(data:application/x-font-ttf;base64,AAEAAAAOAIAAAwBgRkZUTYQd29oAAAWIAAAAHEdERUYAKQAqAAAFYAAAACZPUy8yQ0FcUwAAAWgAAABgY21hcAAP8lIAAAHYAAABQmN2dCAAIgKIAAADHAAAAARnYXNwAAAAAQAABVgAAAAIZ2x5ZqQ1ewkAAAMsAAAAiGhlYWQPsR5/AAAA7AAAADZoaGVhBgEEBQAAASQAAAAkaG10eAwAAKIAAAHIAAAAEGxvY2EAbgBUAAADIAAAAAptYXhwAAgAPAAAAUgAAAAgbmFtZSBsbRoAAAO0AAABbnBvc3SwqUy9AAAFJAAAADIAAQAAAAAAAI7W8KxfDzz1AAsEAAAAAADXNj/0AAAAANc7muQAIgAAAgACqgAAAAgAAgAAAAAAAAABAAAEAAAAAAAEAAAAAAACAAABAAAAAAAAAAAAAAAAAAAABAABAAAABAAMAAMAAAAAAAIAAAAAAAAAAAAAAC4AAAAAAAMEAAGQAAUAAAKAAwAAAACAAoADAAAAAgAAAAEAAAAAAAAAAAAAAAAAAAAAARAAAAAAAAAAAAAAAFBmRWQAQO6n7qcEAAAAAAAEAAAAAAAAAQAAAAAAAAAAAAAAIAABBAAAIgAAAAAEAAAABAAAgAAAAAMAAAADAAAAHAABAAAAAAA8AAMAAQAAABwABAAgAAAABAAEAAEAAO6n//8AAO6n//8RXAABAAAAAAAAAQYAAAEAAAAAAAAAAQIAAAACAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAiAogAAAAqACoAKgBEAAAAAgAiAAABMgKqAAMABwAusQEALzyyBwQA7TKxBgXcPLIDAgDtMgCxAwAvPLIFBADtMrIHBgH8PLIBAgDtMjMRIREnMxEjIgEQ7szMAqr9ViICZgAAAwCAAAACAAJAAAMABwALAAABFTM1BRUzNQMVMzUBQMD+gMDAwAGAwMDAwMABgMDAAAAAAAAADgCuAAEAAAAAAAAAAAACAAEAAAAAAAEACwAbAAEAAAAAAAIAAQArAAEAAAAAAAMADABHAAEAAAAAAAQACwBsAAEAAAAAAAUACwCQAAEAAAAAAAYACwC0AAMAAQQJAAAAAAAAAAMAAQQJAAEAFgADAAMAAQQJAAIAAgAnAAMAAQQJAAMAGAAtAAMAAQQJAAQAFgBUAAMAAQQJAAUAFgB4AAMAAQQJAAYAFgCcAAAAAHIAZQBwAGwAaQB0AGkAYwBvAG4AcwAAcmVwbGl0aWNvbnMAAAoAAAoAAHIAZQBwAGwAaQB0ACAAaQBjAG8AbgBzAAByZXBsaXQgaWNvbnMAAHIAZQBwAGwAaQB0AGkAYwBvAG4AcwAAcmVwbGl0aWNvbnMAAFYAZQByAHMAaQBvAG4AIAAxAC4AMAAAVmVyc2lvbiAxLjAAAHIAZQBwAGwAaQB0AGkAYwBvAG4AcwAAcmVwbGl0aWNvbnMAAAAAAgAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAEAAAAAQACAQIHdW5pRUVBNwAAAAEAAf//AAAAAQAAAAwAAAAWAB4AAgABAAMAAwABAAQAAAACAAAAAQAAAAEAAAAAAAAAAQAAAADVrAEBAAAAANc2P/QAAAAA1zua5A==) format('truetype');
}</style><style type="text/css" id="l2darkness38-multiplayer-cursor-style">.cursor-l2darkness38 {
  position: relative;
  background-color: var(--accent-primary-strongest);
  border-left: 2px solid #1BC47D;
  pointer-events: none;
}
.selection-l2darkness38 {
  position: relative;
  background-color: #1BC47D;
  opacity: 0.2;
  pointer-events: none;
}
.cursor-tag-l2darkness38::after {
  content: "l2darkness38";
  position: relative;
  bottom: calc(100% - 4px);
  left: -2px;
  background-color: #1BC47D;
  color: white;
  z-index: 10;
  padding: 1px;
  border-radius: 3px;
  pointer-events: none;
  animation: fadeOut 2s ease-in forwards;
}

@keyframes fadeOut {
  0% {opacity: 1;}
  100% {opacity: 0;} 
}
</style><style type="text/css" data-styled-jsx="">.loader.jsx-505344430{width:100%;height:100%;overflow:hidden;padding-left:-webkit-calc(0 * var(--space-16));padding-left:-moz-calc(0 * var(--space-16));padding-left:calc(0 * var(--space-16))}.loader.jsx-505344430>svg{width:250px;display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex}</style><style type="text/css" data-styled-jsx="">.chevron.jsx-2962249647{-webkit-transform:rotate(-90deg);-moz-transform:rotate(-90deg);-ms-transform:rotate(-90deg);-o-transform:rotate(-90deg);transform:rotate(-90deg)}</style><style type="text/css" data-styled-jsx="">.node-icon.jsx-e863968756ad722e{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-moz-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between}.icon.jsx-e863968756ad722e{-webkit-box-flex:0;-webkit-flex:0 0 auto;-moz-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto;width:24px;height:24px;display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center}.gutter.jsx-e863968756ad722e{-webkit-box-flex:0;-webkit-flex:0 0 auto;-moz-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto;width:var(--space-16);display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:end;-webkit-justify-content:flex-end;-moz-box-pack:end;-ms-flex-pack:end;justify-content:flex-end}.chevron.jsx-e863968756ad722e{-webkit-transition:.1s -webkit-transform;-moz-transition:.1s -moz-transform;-o-transition:.1s -o-transform;transition:.1s -webkit-transform;transition:.1s -moz-transform;transition:.1s -o-transform;transition:.1s transform;display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:end;-webkit-justify-content:flex-end;-moz-box-pack:end;-ms-flex-pack:end;justify-content:flex-end}</style><style type="text/css" data-styled-jsx="">div.jsx-55d3ca1db7a8ec81{font-size:var(--font-size-default);-webkit-box-flex:1;-webkit-flex:1 1 auto;-moz-box-flex:1;-ms-flex:1 1 auto;flex:1 1 auto;padding-left:var(--space-8);padding-right:var(--space-4);overflow:hidden;-o-text-overflow:ellipsis;text-overflow:ellipsis;white-space:nowrap}</style><style type="text/css" data-styled-jsx="">.node.jsx-3577969711{height:var(--space-32);cursor:pointer;color:var(--foreground-dimmer);-webkit-border-radius:var(--border-radius-4);-moz-border-radius:var(--border-radius-4);border-radius:var(--border-radius-4);display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-moz-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between;padding-left:-webkit-calc(0 * var(--space-16));padding-left:-moz-calc(0 * var(--space-16));padding-left:calc(0 * var(--space-16));font-size:var(--font-size-default)}.node.interactive.jsx-3577969711:hover{background-color:var(--background-higher);color:var(--foreground-default)}.node.interactive.jsx-3577969711:active{background-color:var(--background-higher)}.node.interactive.active.jsx-3577969711{background-color:var(--accent-primary-default);color:var(--white)}.node.interactive.active.jsx-3577969711 .content.jsx-3577969711{background-color:var(--accent-primary-default);color:var(--white);font-weight:var(--font-weight-medium)}.actions.jsx-3577969711{display:none;opacity:0;-webkit-box-pack:justify;-webkit-justify-content:space-between;-moz-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;margin-left:auto;-webkit-transition:opacity;-moz-transition:opacity;-o-transition:opacity;transition:opacity;height:100%}.is-touch-device .actions.jsx-3577969711,.node.jsx-3577969711:hover .actions.jsx-3577969711{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;opacity:1}</style><style type="text/css" data-styled-jsx="">svg.jsx-1576278405{min-width:20px;min-height:20px}</style><style type="text/css" data-styled-jsx="">div.jsx-f31f21e5502207f1{max-width:100%;width:100%}.node-info.jsx-f31f21e5502207f1{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;overflow:hidden;-webkit-box-flex:1;-webkit-flex-grow:1;-moz-box-flex:1;-ms-flex-positive:1;flex-grow:1}.is-removing.jsx-f31f21e5502207f1{opacity:.5;pointer-events:none}.is-dragging.jsx-f31f21e5502207f1{opacity:.7}</style><style type="text/css" data-styled-jsx="">svg.jsx-3917775609{min-width:12px;min-height:12px;
            
          }</style><style type="text/css" data-styled-jsx="">button.jsx-985764147{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;font-size:var(--font-size-small);font-family:var(--font-family-default);-webkit-border-radius:var(--border-radius-4);-moz-border-radius:var(--border-radius-4);border-radius:var(--border-radius-4);cursor:pointer;outline:0;padding:var(--space-4);text-align:center;-webkit-transition:.1s all ease-in-out;-moz-transition:.1s all ease-in-out;-o-transition:.1s all ease-in-out;transition:.1s all ease-in-out;font-weight:var(--font-weight-medium);width:auto;white-space:nowrap;line-height:var(--font-size-small)}button.default.jsx-985764147{background-color:transparent;border:1px solid transparent;color:var(--foreground-default)}button.default.jsx-985764147:hover{background-color:var(--background-highest);border:1px solid inherit;color:var(--foreground-default)}button.default.jsx-985764147:active{background-color:var(--outline-dimmest)}button.default.jsx-985764147:focus{outline-offset:2px;-webkit-box-shadow:0 0 0 3px var(--accent-primary-default);-moz-box-shadow:0 0 0 3px var(--accent-primary-default);box-shadow:0 0 0 3px var(--accent-primary-default)}button.jsx-985764147:disabled{opacity:.5;pointer-events:none}.content.jsx-985764147{margin:0 0 0 var(--space-4)}.icon-container.jsx-985764147{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;color:currentColor;-webkit-box-ordinal-group:0;-webkit-order:0;-moz-box-ordinal-group:0;-ms-flex-order:0;order:0}@media only screen and (max-width:480px){.content.jsx-985764147{display:inherit;margin:0 0 0 var(--space-4)}}</style><style type="text/css" data-styled-jsx="">.root.jsx-1926135942{position:relative;overflow-y:auto;width:100%;height:100%;font-size:14px;background-color:var(--background-default);z-index:3;-webkit-box-shadow:0;-moz-box-shadow:0;box-shadow:0}.editor.jsx-1926135942{position:relative;overflow-y:auto;width:100%;height:100%;font-size:14px;background-color:var(--background-default)}.editor.jsx-1926135942>div.jsx-1926135942{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:stretch;-webkit-align-items:stretch;-moz-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;width:100%;height:100%}.editor.jsx-1926135942>div.jsx-1926135942>.cm-editor{-webkit-box-flex:1;-webkit-flex:1 1 auto;-moz-box-flex:1;-ms-flex:1 1 auto;flex:1 1 auto;width:100%}.loader.jsx-1926135942{position:absolute;left:0;top:0;height:100%;width:100%;overflow:hidden;z-index:5}</style><style type="text/css" data-styled-jsx="">svg.jsx-2595747570{min-width:16px;min-height:16px;transform: rotate(-90deg);
            webkit-transform: rotate(-90deg);
          }</style><style type="text/css" data-styled-jsx="">svg.jsx-2524426002{min-width:16px;min-height:16px;transform: rotate(90deg);
            webkit-transform: rotate(90deg);
          }</style><style type="text/css" data-styled-jsx="">.packages-icon-svg{width:100%;height:100%}.packages-icon-svg path{fill:currentColor}</style><style type="text/css" data-styled-jsx="">.debugger-icon-svg{width:100%;height:100%}.debugger-icon-svg path{fill:currentColor;fill-rule:evenodd}</style><style type="text/css" data-styled-jsx="">div.jsx-3440812350{display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:flex-start;-webkit-justify-content:flex-start;-moz-box-pack:flex-start;-ms-flex-pack:flex-start;justify-content:flex-start;-webkit-flex-wrap:nowrap;-ms-flex-wrap:nowrap;flex-wrap:nowrap}.h-stack.jsx-3440812350>*{margin-right:var(--space-8)}.h-stack.jsx-3440812350>*:last-child{margin-right:0}.v-stack.jsx-3440812350>*{margin-bottom:var(--space-8)}.v-stack.jsx-3440812350>*:last-child{margin-bottom:0}.constrain-width.jsx-3440812350{max-width:100%}</style><style type="text/css" data-styled-jsx="">.multiplayer-users-container.jsx-2938004337{padding:0 var(--space-8)}@media only screen and (max-width:580px){.multiplayer-users-container.jsx-2938004337{display:none}}</style><style type="text/css" id="l2darkness38-multiplayer-cursor-style">.cursor-l2darkness38 {
  position: relative;
  background-color: var(--accent-primary-strongest);
  border-left: 2px solid #1BC47D;
  pointer-events: none;
}
.selection-l2darkness38 {
  position: relative;
  background-color: #1BC47D;
  opacity: 0.2;
  pointer-events: none;
}
.cursor-tag-l2darkness38::after {
  content: "l2darkness38";
  position: relative;
  bottom: calc(100% - 4px);
  left: -2px;
  background-color: #1BC47D;
  color: white;
  z-index: 10;
  padding: 1px;
  border-radius: 3px;
  pointer-events: none;
  animation: fadeOut 2s ease-in forwards;
}

@keyframes fadeOut {
  0% {opacity: 1;}
  100% {opacity: 0;} 
}
</style><style type="text/css" data-styled-jsx="">.file-header-tab.jsx-1431496361{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;padding:0 var(--space-24)0 var(--space-8);cursor:pointer;height:100%;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;position:relative;background-color:var(--background-default);color:var(--foreground-default);-webkit-box-shadow:var(--shadow-1);-moz-box-shadow:var(--shadow-1);box-shadow:var(--shadow-1);min-width:var(--space-80);-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;-webkit-border-top-right-radius:var(--border-radius-4);-moz-border-radius-topright:var(--border-radius-4);border-top-right-radius:var(--border-radius-4);-webkit-border-top-left-radius:var(--border-radius-4);-moz-border-radius-topleft:var(--border-radius-4);border-top-left-radius:var(--border-radius-4)}.sidenav-closed .file-header-tab.first{-webkit-border-top-left-radius:0px;-moz-border-radius-topleft:0px;border-top-left-radius:0px}.close-file-button{opacity:.7;position:absolute;right:var(--space-4);padding:2px!important;color:var(--foreground-dimmer)!important}.file-header-tab.jsx-1431496361:hover{background-color:auto;color:var(--foreground-default)}.file-header-tab.jsx-1431496361:hover .file-path{color:var(--foreground-default)}.file-header-tab.jsx-1431496361:hover .close-file-button{opacity:1}.close-file-button:hover{color:var(--foreground-default)!important}.file-path.jsx-1431496361{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;height:100%}.spacer.jsx-1431496361{width:var(--space-8)}</style><style type="text/css" data-styled-jsx="">.xterm{height:100%}.xterm .xterm-viewport{overflow-y:auto!important;height:100%}</style><style type="text/css" data-styled-jsx="">.container.jsx-d20ffa1910a8638b{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;-moz-box-orient:vertical;-moz-box-direction:normal;-ms-flex-direction:column;flex-direction:column;height:100%;background-color:var(--background-default);-webkit-border-radius:var(--border-radius-4);-moz-border-radius:var(--border-radius-4);border-radius:var(--border-radius-4)}.root.jsx-d20ffa1910a8638b{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;-moz-box-orient:vertical;-moz-box-direction:normal;-ms-flex-direction:column;flex-direction:column;position:relative;height:100%;padding-left:1em;padding-top:var(--space-8);overflow:hidden;-webkit-border-radius:var(--border-radius-4);-moz-border-radius:var(--border-radius-4);border-radius:var(--border-radius-4);z-index:1}.xterm-container.jsx-d20ffa1910a8638b{min-height:1px;height:100%}code.jsx-d20ffa1910a8638b{color:var(--foreground-dimmest)}.container.jsx-d20ffa1910a8638b:focus-within .controls.jsx-d20ffa1910a8638b{opacity:1}.controls.jsx-d20ffa1910a8638b{opacity:0;position:absolute;top:var(--space-8);right:var(--space-16);z-index:5;height:30px;display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-orient:horizontal;-webkit-box-direction:normal;-webkit-flex-direction:row;-moz-box-orient:horizontal;-moz-box-direction:normal;-ms-flex-direction:row;flex-direction:row;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center}.contextual-hint.jsx-d20ffa1910a8638b{margin:var(--space-8)0 0 var(--space-16)}</style><style type="text/css" data-styled-jsx="">.rendered-markdown.jsx-830554550d72df57{word-break:break-word;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;line-height:1.5;color:var(--foreground-default);font-family:var(--font-family-default)!important;font-size:var(--font-size-subhead-default);-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}.rendered-markdown.jsx-830554550d72df57 h1,.rendered-markdown.jsx-830554550d72df57 h2,.rendered-markdown.jsx-830554550d72df57 h3,.rendered-markdown.jsx-830554550d72df57 h4,.rendered-markdown.jsx-830554550d72df57 h5,.rendered-markdown.jsx-830554550d72df57 h6{color:var(--foreground-default);font-weight:var(--font-weight-medium);margin-bottom:var(--space-16);line-height:1.25;word-wrap:break-word}.rendered-markdown.jsx-830554550d72df57 h1,.rendered-markdown.jsx-830554550d72df57 h2{padding-bottom:var(--space-8);border-bottom:1px solid var(--background-higher);margin-top:var(--space-48)}.rendered-markdown.jsx-830554550d72df57 h1{font-size:2em}.rendered-markdown.jsx-830554550d72df57 h2{font-size:1.5em}.rendered-markdown.jsx-830554550d72df57 h3{font-size:1.25em;margin-top:var(--space-24)}.rendered-markdown.jsx-830554550d72df57 h4{font-size:1em;margin-top:var(--space-16)}.rendered-markdown.jsx-830554550d72df57 h5{font-size:.875em}.rendered-markdown.jsx-830554550d72df57 h6{color:var(--foreground-dimmer);font-size:.85em}.rendered-markdown.jsx-830554550d72df57 .anchor{float:left;line-height:1;margin-left:-webkit-calc(-1*var(--space-16));margin-left:-moz-calc(-1*var(--space-16));margin-left:calc(-1*var(--space-16));padding-right:var(--space-4)}.rendered-markdown.jsx-830554550d72df57 .anchor:focus{outline:none}.rendered-markdown.jsx-830554550d72df57 p{margin-bottom:var(--space-16);font-size:var(--font-size-subhead-default);font-family:var(--font-family-default)!important}.rendered-markdown.jsx-830554550d72df57 table{display:block;width:100%;overflow:auto;margin-bottom:var(--space-16);word-break:normal}.rendered-markdown.jsx-830554550d72df57 table th{font-weight:var(--font-weight-medium)}.rendered-markdown.jsx-830554550d72df57 table td,.rendered-markdown.jsx-830554550d72df57 table th{padding:var(--space-8)var(--space-12);border:1px solid var(--background-highest);min-width:16ch}.rendered-markdown.jsx-830554550d72df57 table tr{background-color:var(--background-default);border-top:1px solid var(--background-highest)}.rendered-markdown.jsx-830554550d72df57 table tr:nth-child(2n){background-color:var(--background-root)}.rendered-markdown.jsx-830554550d72df57 hr:after{clear:both}.rendered-markdown.jsx-830554550d72df57 table{border-spacing:0;border-collapse:collapse}.rendered-markdown.jsx-830554550d72df57 li>p{margin-bottom:0}.rendered-markdown.jsx-830554550d72df57 li{word-wrap:break-all;margin-top:var(--space-4)}.rendered-markdown.jsx-830554550d72df57 dd{margin-left:0}.rendered-markdown.jsx-830554550d72df57 ol,.rendered-markdown.jsx-830554550d72df57 ul{padding-left:var(--space-16);padding-bottom:var(--space-16);margin-top:0;margin-bottom:0}.rendered-markdown.jsx-830554550d72df57 ul{list-style:initial}.rendered-markdown.jsx-830554550d72df57 ol{list-style:decimal}.rendered-markdown.jsx-830554550d72df57 ol ol,.rendered-markdown.jsx-830554550d72df57 ol ul,.rendered-markdown.jsx-830554550d72df57 ul ol,.rendered-markdown.jsx-830554550d72df57 ul ul{padding-left:var(--space-16);margin-top:0;margin-bottom:0;padding-bottom:0}.rendered-markdown.jsx-830554550d72df57 ul{list-style-type:disc}.rendered-markdown.jsx-830554550d72df57 ul ul{list-style-type:circle}.rendered-markdown.jsx-830554550d72df57 ul ul ul{list-style-type:square}.rendered-markdown.jsx-830554550d72df57 ol ol,.rendered-markdown.jsx-830554550d72df57 ul ol{list-style-type:lower-roman}.rendered-markdown.jsx-830554550d72df57 ol ol ol,.rendered-markdown.jsx-830554550d72df57 ol ul ol,.rendered-markdown.jsx-830554550d72df57 ul ol ol,.rendered-markdown.jsx-830554550d72df57 ul ul ol{list-style-type:lower-alpha}.rendered-markdown.jsx-830554550d72df57 pre{line-height:18px;font-family:var(--font-family-code)!important}.rendered-markdown.jsx-830554550d72df57 pre{margin:var(--space-16)0;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px;word-break:break-all;word-wrap:break-word;white-space:pre-wrap;color:var(--foreground-default)}.rendered-markdown.jsx-830554550d72df57 pre:last-child{margin-bottom:0!important}.rendered-markdown.jsx-830554550d72df57 blockquote{padding:0 1em;margin-bottom:var(--space-16);border-left:var(--space-2)solid var(--background-highest);padding-left:var(--space-16)}.rendered-markdown.jsx-830554550d72df57 blockquote>*{color:var(--foreground-dimmer)!important}.rendered-markdown.jsx-830554550d72df57 blockquote>:last-child{margin-bottom:0!important;border-bottom:none!important}.rendered-markdown.jsx-830554550d72df57 blockquote>:first-child{margin-top:0!important}.rendered-markdown.jsx-830554550d72df57 kbd{display:inline-block;padding:3px 5px;font:11px var(--font-family-code);line-height:10px;color:var(--foreground-dimmer);vertical-align:middle;background-color:var(--background-higher);border:none;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:3px;-webkit-box-shadow:inset 0 -1px 0 var(--background-highest);-moz-box-shadow:inset 0 -1px 0 var(--background-highest);box-shadow:inset 0 -1px 0 var(--background-highest)}.rendered-markdown.jsx-830554550d72df57 a{color:var(--accent-primary-stronger);background-color:initial}.rendered-markdown.jsx-830554550d72df57>:first-child{margin-top:0!important;padding-top:0!important}.rendered-markdown.jsx-830554550d72df57>:last-child{margin-bottom:0!important;padding-bottom:0!important;border-bottom:none!important}.rendered-markdown.jsx-830554550d72df57 [type="checkbox"]{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;margin-right:var(--space-8);padding:0}.rendered-markdown.jsx-830554550d72df57 details{margin-bottom:var(--space-8);display:block;background:var(--background-higher);-webkit-border-radius:var(--border-radius-4);-moz-border-radius:var(--border-radius-4);border-radius:var(--border-radius-4);padding:var(--space-8)}.rendered-markdown.jsx-830554550d72df57 summary{display:list-item;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;cursor:pointer;font-weight:var(--font-weight-bold)}.rendered-markdown.jsx-830554550d72df57 details[open]>summary{border-bottom:solid 1px var(--background-highest);padding-bottom:var(--space-8);margin-bottom:var(--space-8)}.rendered-markdown.jsx-830554550d72df57 hr{height:.25em;background-color:var(--background-higher);margin:var(--space-24)0;border:0}</style><style type="text/css" id="l2darkness38-multiplayer-cursor-style">.cursor-l2darkness38 {
  position: relative;
  background-color: var(--accent-primary-strongest);
  border-left: 2px solid #1BC47D;
  pointer-events: none;
}
.selection-l2darkness38 {
  position: relative;
  background-color: #1BC47D;
  opacity: 0.2;
  pointer-events: none;
}
.cursor-tag-l2darkness38::after {
  content: "l2darkness38";
  position: relative;
  bottom: calc(100% - 4px);
  left: -2px;
  background-color: #1BC47D;
  color: white;
  z-index: 10;
  padding: 1px;
  border-radius: 3px;
  pointer-events: none;
  animation: fadeOut 2s ease-in forwards;
}

@keyframes fadeOut {
  0% {opacity: 1;}
  100% {opacity: 0;} 
}
</style><style type="text/css" id="l2darkness38-multiplayer-cursor-style">.cursor-l2darkness38 {
  position: relative;
  background-color: var(--accent-primary-strongest);
  border-left: 2px solid #1BC47D;
  pointer-events: none;
}
.selection-l2darkness38 {
  position: relative;
  background-color: #1BC47D;
  opacity: 0.2;
  pointer-events: none;
}
.cursor-tag-l2darkness38::after {
  content: "l2darkness38";
  position: relative;
  bottom: calc(100% - 4px);
  left: -2px;
  background-color: #1BC47D;
  color: white;
  z-index: 10;
  padding: 1px;
  border-radius: 3px;
  pointer-events: none;
  animation: fadeOut 2s ease-in forwards;
}

@keyframes fadeOut {
  0% {opacity: 1;}
  100% {opacity: 0;} 
}
</style><style type="text/css" id="l2darkness38-multiplayer-cursor-style">.cursor-l2darkness38 {
  position: relative;
  background-color: var(--accent-primary-strongest);
  border-left: 2px solid #1BC47D;
  pointer-events: none;
}
.selection-l2darkness38 {
  position: relative;
  background-color: #1BC47D;
  opacity: 0.2;
  pointer-events: none;
}
.cursor-tag-l2darkness38::after {
  content: "l2darkness38";
  position: relative;
  bottom: calc(100% - 4px);
  left: -2px;
  background-color: #1BC47D;
  color: white;
  z-index: 10;
  padding: 1px;
  border-radius: 3px;
  pointer-events: none;
  animation: fadeOut 2s ease-in forwards;
}

@keyframes fadeOut {
  0% {opacity: 1;}
  100% {opacity: 0;} 
}
</style><style type="text/css" data-styled-jsx="">.node-actions-menu.jsx-1329316516{position:relative;width:20px;height:100%}.is-touch-device .protip.jsx-1329316516{display:none}.protip.jsx-1329316516{font-size:13px;padding:10px 5px;text-align:center;color:var(--foreground-default);border-top:1px solid var(--outline-dimmest)}.protip.jsx-1329316516>span.jsx-1329316516{color:var(--accent-positive-default);font-weight:var(--font-weight-bold);font-size:12px}button.jsx-1329316516{top:0;width:100%;height:100%;display:block;background-color:transparent;border:0 none;cursor:pointer;color:var(--white);-webkit-border-radius:var(--border-radius-4);-moz-border-radius:var(--border-radius-4);border-radius:var(--border-radius-4)}button.jsx-1329316516:hover{color:auto}ul.jsx-1329316516{width:130px;display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;-moz-box-orient:vertical;-moz-box-direction:normal;-ms-flex-direction:column;flex-direction:column;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;background-color:var(--background-default);-webkit-border-radius:var(--border-radius-4);-moz-border-radius:var(--border-radius-4);border-radius:var(--border-radius-4);-webkit-box-shadow:var(--shadow-2);-moz-box-shadow:var(--shadow-2);box-shadow:var(--shadow-2);list-style:none;position:absolute;right:var(--space-8);top:-webkit-calc(100% - var(--space-8));top:-moz-calc(100% - var(--space-8));top:calc(100% - var(--space-8));z-index:1}ul.jsx-1329316516:focus{outline:none}</style><style type="text/css" data-styled-jsx="">.node.jsx-3663979731{height:var(--space-32);cursor:pointer;color:var(--foreground-dimmer);-webkit-border-radius:var(--border-radius-4);-moz-border-radius:var(--border-radius-4);border-radius:var(--border-radius-4);display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-moz-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between;padding-left:-webkit-calc(0 * var(--space-16));padding-left:-moz-calc(0 * var(--space-16));padding-left:calc(0 * var(--space-16));font-size:var(--font-size-default)}.node.interactive.jsx-3663979731:hover{background-color:var(--background-higher);color:var(--foreground-default)}.node.interactive.jsx-3663979731:active{background-color:var(--background-higher)}.node.interactive.active.jsx-3663979731{background-color:var(--accent-primary-default);color:var(--white)}.node.interactive.active.jsx-3663979731 .content.jsx-3663979731{background-color:var(--accent-primary-default);color:var(--white);font-weight:var(--font-weight-medium)}.actions.jsx-3663979731{display:flex;opacity:1;-webkit-box-pack:justify;-webkit-justify-content:space-between;-moz-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;margin-left:auto;-webkit-transition:opacity;-moz-transition:opacity;-o-transition:opacity;transition:opacity;height:100%}.is-touch-device .actions.jsx-3663979731,.node.jsx-3663979731:hover .actions.jsx-3663979731{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;opacity:1}</style><style type="text/css" data-styled-jsx="">.placeholder.jsx-761223062c9d62b5{font-family:var(--font-family-code);color:var(--foreground-dimmest)}.link.jsx-761223062c9d62b5{cursor:pointer;pointer-events:all;color:var(--accent-primary-default);text-decoration:none}.link.jsx-761223062c9d62b5:hover{text-decoration:underline}</style><style type="text/css" id="l2darkness38-multiplayer-cursor-style">.cursor-l2darkness38 {
  position: relative;
  background-color: var(--accent-primary-strongest);
  border-left: 2px solid #1BC47D;
  pointer-events: none;
}
.selection-l2darkness38 {
  position: relative;
  background-color: #1BC47D;
  opacity: 0.2;
  pointer-events: none;
}
.cursor-tag-l2darkness38::after {
  content: "l2darkness38";
  position: relative;
  bottom: calc(100% - 4px);
  left: -2px;
  background-color: #1BC47D;
  color: white;
  z-index: 10;
  padding: 1px;
  border-radius: 3px;
  pointer-events: none;
  animation: fadeOut 2s ease-in forwards;
}

@keyframes fadeOut {
  0% {opacity: 1;}
  100% {opacity: 0;} 
}