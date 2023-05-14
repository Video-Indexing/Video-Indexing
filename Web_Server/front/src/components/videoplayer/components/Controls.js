import React, { forwardRef, useState } from "react";
import PropTypes from "prop-types";
import Typography from "@mui/material/Typography";
import { makeStyles, withStyles } from '@mui/styles';
import Button from "@mui/material/Button";
import IconButton from "@mui/material/IconButton";
// import BookmarkIcon from "@mui/icons-material/Bookmark";
import FastRewindIcon from "@mui/icons-material/FastRewind";
import FastForwardIcon from "@mui/icons-material/FastForward";
import PlayArrowIcon from "@mui/icons-material/PlayArrow";
import PauseIcon from "@mui/icons-material/Pause";
import Slider from "@mui/material/Slider";
import Tooltip from "@mui/material/Tooltip";
import Grid from "@mui/material/Grid";
import VolumeUp from "@mui/icons-material/VolumeUp";
import VolumeDown from "@mui/icons-material/VolumeDown";
import VolumeMute from "@mui/icons-material/VolumeMute";
import FullScreen from "@mui/icons-material/Fullscreen";
import Popover from "@mui/material/Popover";

const useStyles = makeStyles((theme) => ({
  controlsWrapper: {
    visibility: "hidden",
    position: "absolute",
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    height: "100%",
    background: "rgba(0,0,0,0.6)",
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-between",
  },

  button: {
    margin: "8px",
  },
  controlIcons: {
    color: "#fff",

    fontSize: 50,
    transform: "scale(0.9)",
    "&:hover": {
      color: "#fff",
      transform: "scale(1)",
    },
  },

  bottomIcons: {
    color: "#fff",
    "&:hover": {
      color: "#fff",
    },
  },

  volumeSlider: {
    maxWidth: "100px",
  },


  top:{
    height: "50%"
  },
  bottom: {
    height: "50%",
    display: "flex",
    alignItems: "flex-end"
  },
  column:{
    display:"flex",
    flexFlow:"column",
    width:"100%"
  },
  title: {
    color: "white",
    fontSize: "28px",
    padding: "16px"
    
  },
  mark: {
    color: "red",
    padding: 10
  },
}));

const PrettoSlider = withStyles({
  root: {
    height: 8,
  },
  thumb: {
    // height: 24,
    // width: 24,
    // backgroundColor: "#fff",
    // border: "2px solid currentColor",
    // marginTop: -8,
    // marginLeft: -12,
    // width: "100%",
    "&:focus, &:hover, &$active": {
      boxShadow: "inherit",
    },
  },
  active: {},
  valueLabel: {
    left: "calc(-50% + 4px)",
  },
  track: {
    height: 8,
    borderRadius: 4,
  },
  rail: {
    height: 8,
    borderRadius: 4,
  },
})(Slider);

function ValueLabelComponent(props) {
  const { children, open, value } = props;

  return (
    <Tooltip open={open} enterTouchDelay={0} placement="top" title={value}>
      {children}
    </Tooltip>
  );
}
const marks = [
    {
      value: 0,
      label: 'KNN',
    },
    {
      value: 20,
      label: 'Test1',
    },
    {
      value: 37,
      label: 'Test2',
    },
    {
      value: 100,
      label: 'Test3',
    },
  ];
  
  function valuetext(value) {
    return `${value}°C`;
  }
  
  function valueLabelFormat(value) {
    return marks.findIndex((mark) => mark.value === value) + 1;
  }

const Controls = forwardRef(
  (
    {
      onSeek,
      onSeekMouseDown,
      onSeekMouseUp,
      onDuration,
      onRewind,
      onPlayPause,
      onFastForward,
      playing,
      played,
      elapsedTime,
      totalDuration,
      onMute,
      muted,
      onVolumeSeekDown,
      onChangeDispayFormat,
      playbackRate,
      onPlaybackRateChange,
      onToggleFullScreen,
      volume,
      onVolumeChange,
      onBookmark,
    },
    ref
  ) => {
    const classes = useStyles();
    const [anchorEl, setAnchorEl] = React.useState(null);
    const handleClick = (event) => {
      setAnchorEl(event.currentTarget);
    };

    const handleClose = () => {
      setAnchorEl(null);
    };

    const open = Boolean(anchorEl);
    const id = open ? "simple-popover" : undefined;

    return (
      <div ref={ref} className={classes.controlsWrapper}>
        <div className={classes.top}>
            <div className={classes.title}>
                VideoTitle
            </div>
        </div>
        <div className={classes.bottom}>
            <div className={classes.column}>
            <Grid
                container
                direction="row"
                justify="space-between"
                alignItems="flex-end"
                style={{ paddingRight: 16, paddingLeft: 16 , width : "100%"}}
            >
                <Grid item xs={12}>
                <PrettoSlider
                    min={0}
                    max={100}
                    valueLabelFormat={valueLabelFormat}
                    getAriaValueText={valuetext}
                    valueLabelDisplay="auto"
                    track={false}
                    marks={marks}
                    // ValueLabelComponent={(props) => (
                    // <ValueLabelComponent {...props} value={elapsedTime} />
                    // )}
                    aria-label="custom thumb label"
                    value={played * 100}
                    onChange={onSeek}
                    onMouseDown={onSeekMouseDown}
                    onChangeCommitted={onSeekMouseUp}
                    onDuration={onDuration}
                    // sx={{markLabel: classes.mark }}
                    // classes={{ markLabel: classes.mark }}
                    
                />
                </Grid>
            </Grid>
            <Grid  
                container
                direction="row"
                justifyContent="space-between"
                alignItems="center"            
                style={{paddingLeft:"16px",paddingRight:"16px", width: "100%"}}
            > 
                <div
                  onClick={onPlayPause}
                  className={classes.bottomIcons}
                >
                  {playing ? (
                    <PauseIcon fontSize="large" />
                  ) : (
                    <PlayArrowIcon fontSize="large" />
                  )}
                </div>

                <div
                  // onClick={() => setState({ ...state, muted: !state.muted })}
                  onClick={onMute}
                  className={`${classes.bottomIcons} ${classes.volumeButton}`}
                >
                  {muted ? (
                    <VolumeMute fontSize="large" />
                  ) : volume > 0.5 ? (
                    <VolumeUp fontSize="large" />
                  ) : (
                    <VolumeDown fontSize="large" />
                  )}
                </div>
                <Slider
                  min={0}
                  max={100}
                  value={muted ? 0 : volume * 100}
                  onChange={onVolumeChange}
                  aria-labelledby="input-slider"
                  className={classes.volumeSlider}
                  onMouseDown={onSeekMouseDown}
                  onChangeCommitted={onVolumeSeekDown}
                />

                <div
                    onClick={onRewind}
                    className={classes.bottomIcons}
                    aria-label="rewind"
                    >
                    <FastRewindIcon
                        // className={classes.bottomIcons}
                        fontSize="inherit"
                    />
                </div>
                <div
                    onClick={onFastForward}
                    className={classes.bottomIcons}
                    aria-label="forward"
                    >
                    <FastForwardIcon fontSize="inherit" />
                </div>

                <Button
                  variant="text"
                  onClick={
                    onChangeDispayFormat
                    //     () =>
                    //   setTimeDisplayFormat(
                    //     timeDisplayFormat == "normal" ? "remaining" : "normal"
                    //   )
                  }
                >
                  <Typography
                    variant="body1"
                    style={{ color: "#fff", marginLeft: 16 }}
                  >
                    {elapsedTime}/{totalDuration}
                  </Typography>
                </Button>
                <Button
                onClick={handleClick}
                aria-describedby={id}
                className={classes.bottomIcons}
                variant="text"
              >
                <Typography>{playbackRate}X</Typography>
              </Button>

              <Popover
                container={ref.current}
                open={open}
                id={id}
                onClose={handleClose}
                anchorEl={anchorEl}
                anchorOrigin={{
                  vertical: "top",
                  horizontal: "left",
                }}
                transformOrigin={{
                  vertical: "bottom",
                  horizontal: "left",
                }}
              >
                <Grid container direction="column-reverse">
                  {[0.5, 1, 1.5, 2].map((rate) => (
                    <Button
                      key={rate}
                      //   onClick={() => setState({ ...state, playbackRate: rate })}
                      onClick={() => onPlaybackRateChange(rate)}
                      variant="text"
                    >
                      <Typography
                        color={rate === playbackRate ? "secondary" : "inherit"}
                      >
                        {rate}X
                      </Typography>
                    </Button>
                  ))}
                </Grid>
              </Popover>
              <div
                onClick={onToggleFullScreen}
                className={classes.bottomIcons}
              >
                <FullScreen fontSize="large" />
              </div>
            </Grid>

            </div>
        </div>
      </div>
    );
  }
);

Controls.propTypes = {
  onSeek: PropTypes.func,
  onSeekMouseDown: PropTypes.func,
  onSeekMouseUp: PropTypes.func,
  onDuration: PropTypes.func,
  onRewind: PropTypes.func,
  onPlayPause: PropTypes.func,
  onFastForward: PropTypes.func,
  onVolumeSeekDown: PropTypes.func,
  onChangeDispayFormat: PropTypes.func,
  onPlaybackRateChange: PropTypes.func,
  onToggleFullScreen: PropTypes.func,
  onMute: PropTypes.func,
  playing: PropTypes.bool,
  played: PropTypes.number,
  elapsedTime: PropTypes.string,
  totalDuration: PropTypes.string,
  muted: PropTypes.bool,
  playbackRate: PropTypes.number,
};
export default Controls;