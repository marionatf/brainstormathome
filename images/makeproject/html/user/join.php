<?php

// This file is part of BOINC.
// http://boinc.berkeley.edu
// Copyright (C) 2016 University of California
//
// BOINC is free software; you can redistribute it and/or modify it
// under the terms of the GNU Lesser General Public License
// as published by the Free Software Foundation,
// either version 3 of the License, or (at your option) any later version.
//
// BOINC is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
// See the GNU Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public License
// along with BOINC.  If not, see <http://www.gnu.org/licenses/>.

require_once("../inc/util.inc");

function show_choose($is_old) {
    panel(null,
        function() use($is_old) {
            if ($is_old) {
                echo ' <a href="join.php">'.tra('I\'m new').'</a> &nbsp; |&nbsp; '.tra('I\'m a BOINC user').'
                ';
            } else {
                echo tra('I\'m new')
                    .' &nbsp; |&nbsp;  <a href="join.php?old=1">'
                    .tra('I\'m a BOINC user')
                    .'</a>
                ';
            }
        }
    );
}

function show_new() {
    global $master_url;
    panel(null,
        function() use ($master_url) {
            echo '
                <ol>
                <li> '
                .tra('Read our %1 Rules and Policies %2.', '<a href="info.php">', '</a>')
                .'<li> <p>'
                .tra('Download and install the BOINC desktop software.')
                    .'</p><p>
                    <a href="http://boinc.berkeley.edu/download.php" class="btn btn-success">'.tra('Download BOINC').'</a>
                    </p><li> <p>'
                .tra('Download and install Virtualbox.')
                    .'</p><p>
                    <a href="https://www.virtualbox.org/wiki/Downloads" class="btn btn-success">'.tra('Download Virtualbox').'</a>
                    </p>
		<p>On Windows you can just use the "+Virtualbox" link when downloading BOINC and Virtualbox will be installed automatically.</p>
                <li> '.tra("Run BOINC and select 'Add project'. Then enter %2", "<strong>".PROJECT."</strong>", "<strong>$master_url</strong> at 'Project URL'.").'
                <li> '.tra("You are all set! Your computer will now automatically download and run jobs.").'
                </ol>
            ';
        }
    );
}

function show_old() {
    global $master_url;
    panel(null,
        function() use($master_url) {
            echo '
                <ul>
                <li> '
                .tra('Install BOINC on this device if not already present.')
                .'<p>
                <li> '
                .tra('Download and install Virtualbox.')
                    .'</p><p>
                    <a href="https://www.virtualbox.org/wiki/Downloads" class="btn btn-success">'.tra('Download Virtualbox').'</a>
                    </p>
		<p>'.tra('On Windows you can just use the "+Virtualbox" link when downloading BOINC and Virtualbox will be installed automatically.').'</p>
                <li> '.tra("Run BOINC and select 'Add project'. Then enter %2", "<strong>".PROJECT."</strong>", "<strong>$master_url</strong> at 'Project URL'.").'<li>
                

                '.tra('If you\'re running a command-line version of BOINC on this computer, %1 create an account %2, then use %3 boinccmd --project_attach %4 to add the project.',
                    '<a href="create_account_form.php">',
                    '</a>',
                    '<strong><a href="http://boinc.berkeley.edu/wiki/Boinccmd_tool">',
                    '</a></strong>'
                )
                .'
                </ul>
            ';
        }
    );
}


function show_requirements() {
    panel(null,
        function() {
            echo '
                <p><strong>'.tra('Requirements').'</strong></p>
                <ul>
                <li> '
                .tra('64-bit processor').'
                <li> '
                .tra('Virtualbox version 4.3 or later
').'
                <li> '
                .tra('VT-x or AMD-v enabled in your BIOS (To ckeck if it is disabled: login, go to %1 this page %2  > Details > Virtualisation)','<a href="http://brainstormhome.org/hosts_user.php">','</a>').'
                <li> '
                .tra('Operating System').'
                    <ul>
                    <li>'.tra('Windows XP or later').'
                    <li>'.tra('Mac OSX 10.8 or later').'
                    <li>'.tra('Linux (many recent versions work)').'
                    </ul>
                </ul>

';
        }
    );
}



$old = get_int('old', true);

page_head(tra("Join %1", PROJECT));
show_choose($old);
if ($old) {
    show_old();
} else {
    show_new();
}
show_requirements();
page_tail();
