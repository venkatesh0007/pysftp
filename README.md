# pysftp
remote srver file watcher using python




A friendly Python SFTP interface.

class pysftp.Connection(host, username=None, private_key=None, password=None, port=22, private_key_pass=None, ciphers=None, log=False)¶
Connects and logs into the specified hostname. Arguments that are not given are guessed from the environment.

Parameters:	
host (str) – The Hostname or IP of the remote machine.
username (str|None) – Default: None - Your username at the remote machine.
private_key (str|obj|None) – Default: None - path to private key file(str) or paramiko.AgentKey
password (str|None) – Default: None - Your password at the remote machine.
port (int) – Default: 22 - The SSH port of the remote machine.
private_key_pass (str|None) – Default: None - password to use, if private_key is encrypted.
ciphers (list|None) – Default: None - List of ciphers to use in order.
log (bool|str) – Default: False - log connection/handshake details? If set to True, pysftp creates a temporary file and logs to that. If set to a valid path and filename, pysftp logs to that. The name of the logfile can be found at .logfile
Returns:	
(obj) connection to the requested host

Raises:	
ConnectionException –
CredentialException –
SSHException –
AuthenticationException –
PasswordRequiredException –
active_ciphers¶
Get tuple of currently used local and remote ciphers.

Returns:	(tuple of str) currently used ciphers (local_cipher, remote_cipher)
cd(remotepath=None)¶
context manager that can change to a optionally specified remote directory and restores the old pwd on exit.

Parameters:	remotepath (str|None) – Default: None - remotepath to temporarily make the current directory
Returns:	None
Raises:	IOError, if remote path doesn’t exist
chdir(remotepath)¶
change the current working directory on the remote

Parameters:	remotepath (str) – the remote path to change to
Returns:	None
Raises:	IOError, if path does not exist
chmod(remotepath, mode=777)¶
set the mode of a remotepath to mode, where mode is an integer representation of the octal mode to use.

Parameters:	
remotepath (str) – the remote path/file to modify
mode (int) – Default: 777 - int representation of octal mode for directory
Returns:	
None

Raises:	
IOError, if the file doesn’t exist

chown(remotepath, uid=None, gid=None)¶
set uid and/or gid on a remotepath, you may specify either or both. Unless you have permission to do this on the remote server, you will raise an IOError: 13 - permission denied

Parameters:	
remotepath (str) – the remote path/file to modify
uid (int) – the user id to set on the remotepath
gid (int) – the group id to set on the remotepath
Returns:	
None

Raises:	
IOError, if you don’t have permission or the file doesn’t exist

close()¶
Closes the connection and cleans up.

cwd(remotepath)¶
change the current working directory on the remote

Parameters:	remotepath (str) – the remote path to change to
Returns:	None
Raises:	IOError, if path does not exist
execute(command)¶
Execute the given commands on a remote machine. The command is executed without regard to the remote pwd.

Parameters:	command (str) – the command to execute.
Returns:	(list of str) representing the results of the command
Raises:	Any exception raised by command will be passed through.
exists(remotepath)¶
Test whether a remotepath exists.

Parameters:	remotepath (str) – the remote path to verify
Returns:	(bool) True, if remotepath exists, else False
get(remotepath, localpath=None, callback=None, preserve_mtime=False)¶
Copies a file between the remote host and the local host.

Parameters:	
remotepath (str) – the remote path and filename, source
localpath (str) – the local path and filename to copy, destination. If not specified, file is copied to local current working directory
callback (callable) – optional callback function (form: func(int, int)) that accepts the bytes transferred so far and the total bytes to be transferred.
preserve_mtime (bool) – Default: False - make the modification time(st_mtime) on the local file match the time on the remote. (st_atime can differ because stat’ing the localfile can/does update it’s st_atime)
Returns:	
None

Raises:	
IOError

get_d(remotedir, localdir, preserve_mtime=False)¶
get the contents of remotedir and write to locadir. (non-recursive)

Parameters:	
remotedir (str) – the remote directory to copy from (source)
localdir (str) – the local directory to copy to (target)
preserve_mtime (bool) – Default: False - preserve modification time on files
Returns:	
None

Raises:	
get_r(remotedir, localdir, preserve_mtime=False)¶
recursively copy remotedir structure to localdir

Parameters:	
remotedir (str) – the remote directory to copy from
localdir (str) – the local directory to copy to
preserve_mtime (bool) – Default: False - preserve modification time on files
Returns:	
None

Raises:	
getcwd()¶
return the current working directory on the remote. This is a wrapper for paramiko’s method and not to be confused with the SFTP command, cwd.

Returns:	(str) the current remote path. None, if not set.
getfo(remotepath, flo, callback=None)¶
Copy a remote file (remotepath) to a file-like object, flo.

Parameters:	
remotepath (str) – the remote path and filename, source
flo – open file like object to write, destination.
callback (callable) – optional callback function (form: func(int, int)) that accepts the bytes transferred so far and the total bytes to be transferred.
Returns:	
(int) the number of bytes written to the opened file object

Raises:	
Any exception raised by operations will be passed through.

isdir(remotepath)¶
return true, if remotepath is a directory

Parameters:	remotepath (str) – the path to test
Returns:	(bool)
isfile(remotepath)¶
return true if remotepath is a file

Parameters:	remotepath (str) – the path to test
Returns:	(bool)
lexists(remotepath)¶
Test whether a remotepath exists. Returns True for broken symbolic links

Parameters:	remotepath (str) – the remote path to verify
Returns:	(bool), True, if lexists, else False
listdir(remotepath='.')¶
return a list of files/directories for the given remote path. Unlike, paramiko, the directory listing is sorted.

Parameters:	remotepath (str) – path to list on the server
Returns:	(list of str) directory entries, sorted
listdir_attr(remotepath='.')¶
return a list of SFTPAttribute objects of the files/directories for the given remote path. The list is in arbitrary order. It does not include the special entries ‘.’ and ‘..’.

The returned SFTPAttributes objects will each have an additional field: longname, which may contain a formatted string of the file’s attributes, in unix format. The content of this string will depend on the SFTP server.

Parameters:	remotepath (str) – path to list on the server
Returns:	(list of SFTPAttributes), sorted
logfile¶
return the name of the file used for logging or False it not logging

Returns:	(str)logfile or (bool) False
lstat(remotepath)¶
return information about file/directory for the given remote path, without following symbolic links. Otherwise, the same as .stat()

Parameters:	remotepath (str) – path to stat
Returns:	(obj) SFTPAttributes object
makedirs(remotedir, mode=777)¶
create all directories in remotedir as needed, setting their mode to mode, if created.

If remotedir already exists, silently complete. If a regular file is in the way, raise an exception.

Parameters:	
remotedir (str) – the directory structure to create
mode (int) – Default: 777 - int representation of octal mode for directory
Returns:	
None

Raises:	
OSError

mkdir(remotepath, mode=777)¶
Create a directory named remotepath with mode. On some systems, mode is ignored. Where it is used, the current umask value is first masked out.

Parameters:	
remotepath (str) – directory to create`
mode (int) – Default: 777 - int representation of octal mode for directory
Returns:	
None

normalize(remotepath)¶
Return the expanded path, w.r.t the server, of a given path. This can be used to resolve symlinks or determine what the server believes to be the pwd, by passing ‘.’ as remotepath.

Parameters:	remotepath (str) – path to be normalized
Returns:	(str) normalized form of the given path
Raises:	IOError, if remotepath can’t be resolved
open(remote_file, mode='r', bufsize=-1)¶
Open a file on the remote server.

See http://paramiko-docs.readthedocs.org/en/latest/api/sftp.html?highlight=open#paramiko.sftp_client.SFTPClient.open for details.

Parameters:	
remote_file (str) – name of the file to open.
mode (str) – mode (Python-style) to open file (always assumed binary)
bufsize (int) – Default: -1 - desired buffering
Returns:	
(obj) SFTPFile, a handle the remote open file

Raises:	
IOError, if the file could not be opened.

put(localpath, remotepath=None, callback=None, confirm=True, preserve_mtime=False)¶
Copies a file between the local host and the remote host.

Parameters:	
localpath (str) – the local path and filename
remotepath (str) – the remote path, else the remote pwd and filename is used.
callback (callable) – optional callback function (form: func(int, int)) that accepts the bytes transferred so far and the total bytes to be transferred..
confirm (bool) – whether to do a stat() on the file afterwards to confirm the file size
preserve_mtime (bool) – Default: False - make the modification time(st_mtime) on the remote file match the time on the local. (st_atime can differ because stat’ing the localfile can/does update it’s st_atime)
Returns:	
(obj) SFTPAttributes containing attributes about the given file

Raises:	
IOError – if remotepath doesn’t exist
OSError – if localpath doesn’t exist
put_d(localpath, remotepath, confirm=True, preserve_mtime=False)¶
Copies a local directory’s contents to a remotepath

Parameters:	
localpath (str) – the local path to copy (source)
remotepath (str) – the remote path to copy to (target)
confirm (bool) – whether to do a stat() on the file afterwards to confirm the file size
preserve_mtime (bool) – Default: False - make the modification time(st_mtime) on the remote file match the time on the local. (st_atime can differ because stat’ing the localfile can/does update it’s st_atime)
Returns:	
None

Raises:	
IOError – if remotepath doesn’t exist
OSError – if localpath doesn’t exist
put_r(localpath, remotepath, confirm=True, preserve_mtime=False)¶
Recursively copies a local directory’s contents to a remotepath

Parameters:	
localpath (str) – the local path to copy (source)
remotepath (str) – the remote path to copy to (target)
confirm (bool) – whether to do a stat() on the file afterwards to confirm the file size
preserve_mtime (bool) – Default: False - make the modification time(st_mtime) on the remote file match the time on the local. (st_atime can differ because stat’ing the localfile can/does update it’s st_atime)
Returns:	
None

Raises:	
IOError – if remotepath doesn’t exist
OSError – if localpath doesn’t exist
putfo(flo, remotepath=None, file_size=0, callback=None, confirm=True)¶
Copies the contents of a file like object to remotepath.

Parameters:	
flo – a file-like object that supports .read()
remotepath (str) – the remote path.
file_size (int) – the size of flo, if not given the second param passed to the callback function will always be 0.
callback (callable) – optional callback function (form: func(int, int)) that accepts the bytes transferred so far and the total bytes to be transferred..
confirm (bool) – whether to do a stat() on the file afterwards to confirm the file size
Returns:	
(obj) SFTPAttributes containing attributes about the given file

Raises:	
TypeError, if remotepath not specified, any underlying error

pwd¶
return the current working directory

Returns:	(str) current working directory
readlink(remotelink)¶
Return the target of a symlink (shortcut). The result will be an absolute pathname.

Parameters:	remotelink (str) – remote path of the symlink
Returns:	(str) absolute path to target
remove(remotefile)¶
remove the file @ remotefile, remotefile may include a path, if no path, then pwd is used. This method only works on files

Parameters:	remotefile (str) – the remote file to delete
Returns:	None
Raises:	IOError
rename(remote_src, remote_dest)¶
rename a file or directory on the remote host.

Parameters:	
remote_src (str) – the remote file/directory to rename
remote_dest (str) – the remote file/directory to put it
Returns:	
None

Raises:	
IOError

rmdir(remotepath)¶
remove remote directory

Parameters:	remotepath (str) – the remote directory to remove
Returns:	None
security_options¶
return the available security options recognized by paramiko.

Returns:	(obj) security preferences of the ssh transport. These are tuples of acceptable .ciphers, .digests, .key_types, and key exchange algorithms .kex, listed in order of preference.
sftp_client¶
give access to the underlying, connected paramiko SFTPClient object

see http://paramiko-docs.readthedocs.org/en/latest/api/sftp.html?highlight=sftpclient

Params:	None
Returns:	(obj) the active SFTPClient object
stat(remotepath)¶
return information about file/directory for the given remote path

Parameters:	remotepath (str) – path to stat
Returns:	(obj) SFTPAttributes
symlink(remote_src, remote_dest)¶
create a symlink for a remote file on the server

Parameters:	
remote_src (str) – path of original file
remote_dest (str) – path of the created symlink
Returns:	
None

Raises:	
any underlying error, IOError if something already exists at remote_dest

timeout¶
(float|None) Default: None -
get or set the underlying socket timeout for pending read/write ops.
Returns:	(float|None) seconds to wait for a pending read/write operation before raising socket.timeout, or None for no timeout
truncate(remotepath, size)¶
Change the size of the file specified by path. Used to modify the size of the file, just like the truncate method on Python file objects. The new file size is confirmed and returned.

Parameters:	
remotepath (str) – remote file path to modify
size (int|long) – the new file size
Returns:	
(int) new size of file

Raises:	
IOError, if file does not exist

unlink(remotefile)¶
remove the file @ remotefile, remotefile may include a path, if no path, then pwd is used. This method only works on files

Parameters:	remotefile (str) – the remote file to delete
Returns:	None
Raises:	IOError
walktree(remotepath, fcallback, dcallback, ucallback, recurse=True)¶
recursively descend, depth first, the directory tree rooted at remotepath, calling discreet callback functions for each regular file, directory and unknown file type.

Parameters:	
remotepath (str) – root of remote directory to descend, use ‘.’ to start at pwd
fcallback (callable) – callback function to invoke for a regular file. (form: func(str))
dcallback (callable) – callback function to invoke for a directory. (form: func(str))
ucallback (callable) – callback function to invoke for an unknown file type. (form: func(str))
recurse (bool) – Default: True - should it recurse
Returns:	
None

Raises:	
exception pysftp.ConnectionException(host, port)¶
Exception raised for connection problems

Attributes:
message – explanation of the error
exception pysftp.CredentialException(message)¶
Exception raised for credential problems

Attributes:
message – explanation of the error
class pysftp.WTCallbacks¶
an object to house the callbacks, used internally

Variables:	
flist – list of files currently traversed
dlist – list of directories currently traversed
ulist – list of unknown entities currently traversed
dir_cb(pathname)¶
called for directories, appends pathname to .dlist

Parameters:	pathname (str) – directory path
file_cb(pathname)¶
called for regular files, appends pathname to .flist

Parameters:	pathname (str) – file path
unk_cb(pathname)¶
called for unknown file types, appends pathname to .ulist

Parameters:	pathname (str) – unknown entity path
pysftp.cd(localpath=None)¶
context manager that can change to a optionally specified local directory and restores the old pwd on exit.

Parameters:	localpath (str|None) – Default: None - local path to temporarily make the current directory
Returns:	None
Raises:	OSError, if local path doesn’t exist
pysftp.path_advance(thepath, sep='/')¶
generator to iterate over a file path forwards

Parameters:	
thepath (str) – the path to navigate forwards
sep (str) – Default: os.sep - the path separator to use
Returns:	
(iter)able of strings

pysftp.path_retreat(thepath, sep='/')¶
generator to iterate over a file path in reverse

Parameters:	
thepath (str) – the path to retreat over
sep (str) – Default: os.sep - the path separator to use
Returns:	
(iter)able of strings

pysftp.reparent(newparent, oldpath)¶
when copying or moving a directory structure, you need to re-parent the oldpath. When using os.path.join to calculate this new path, the appearance of a / root path at the beginning of oldpath, supplants the newparent and we don’t want this to happen, so we need to make the oldpath root appear as a child of the newparent.

Param:	str newparent: the new parent location for oldpath (target)
Parameters:	oldpath (str) – the path being adopted by newparent (source)
Returns:	(str) resulting adoptive path
pysftp.st_mode_to_int(val)¶
SFTAttributes st_mode returns an stat type that shows more than what can be set. Trim off those bits and convert to an int representation. if you want an object that was chmod 711 to return a value of 711, use this function

Parameters:	val (int) – the value of an st_mode attr returned by SFTPAttributes
Returns int:	integer representation of octal mode
pysftp.walktree(localpath, fcallback, dcallback, ucallback, recurse=True)¶
on the local file system, recursively descend, depth first, the directory tree rooted at localpath, calling discreet callback functions for each regular file, directory and unknown file type.

Parameters:	
localpath (str) – root of remote directory to descend, use ‘.’ to start at pwd
fcallback (callable) – callback function to invoke for a regular file. (form: func(str))
dcallback (callable) – callback function to invoke for a directory. (form: func(str))
ucallback (callable) – callback function to invoke for an unknown file type. (form: func(str))
recurse (bool) – Default: True - should it recurse
Returns:	
None

Raises:	
OSError, if localpath doesn’t exist
