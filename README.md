# PySaw

## Description

PySaw is a module that assists with logging to many endpoint modules.  This is more or less a learning project to mimic what I built in PowerShell.  Found the tool to be helpful for my processes.

PySaw was made so the logger can be enabled from a configuration file stored in the applications directory.

## Values

PySaw currently will work on picking up the following values.

### Level

Level is picked up based off the method that is called.

```Python
logger = PySaw()
logger.Emergency()
logger.Alert()
logger.Critical()
logger.Error()
logger.Warning()
logger.Notice()
logger.Information()
logger.Debug()
```

### Message

Message is the value passed to the logger method.

```Python
logger = PySaw()
logger.Debug("This is a test message")
```

To collect this value, use $$Message$$ in your MessageTemplate for it to be collected.

### LineNumber

Line number is based off the method that was called.  This is collected in the background and will be recorded if called for.

#### FileName

File name is collected in the background.  This will contain the file that made the call to the logger.  If it is not needed, it will be ignored.

### Method

If calling from a 
