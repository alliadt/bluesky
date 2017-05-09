from bluesky import settings
if __name__ == "__main__":
    print "   *****   BlueSky Open ATM simulator *****"
    print "Distributed under GNU General Public License v3"
    settings.init('pygame')

from bluesky import stack
from bluesky.ui.pygame import Gui
from bluesky.sim.pygame import Simulation


# Global gui and sim objects for easy access in interactive python shell
gui   = None
sim   = None


def MainLoop():
    # =============================================================================
    # Create gui and simulation objects
    # =============================================================================
    global gui, sim
    gui   = Gui()
    sim   = Simulation()

    # =============================================================================
    # Start the mainloop (and possible other threads)
    # =============================================================================
    stack.init()
    sim.start()

    # Main loop for tmx object
    while not sim.mode == sim.end:
        sim.update()  # Update sim
        gui.update()  # Update GUI

        # Restart traffic simulation:
        if sim.mode == sim.init:
            sim.reset()
            gui.reset()

    # After the simulation is done, close the gui
    sim.stop()
    gui.close()
    # =============================================================================
    # Clean up before exit. Comment this out when debugging for checking variables
    # in the shell.
    # =============================================================================
    del gui
    #-debug del sim
    print 'BlueSky normal end.'
    return

#==============================================================================

# Run mainloop if BlueSky_pygame is called directly

if __name__ == '__main__':
    MainLoop()
