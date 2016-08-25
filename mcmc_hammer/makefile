OBS = o1 o2 o3 o4

OBSDIR = mcmc_steps

DUST         := $(addprefix $(OBSDIR)/, dust_on dust_off)
DUSTonOBS    := $(addprefix $(OBSDIR)/dust_on/,  $(OBS))
DUSToffOBS   := $(addprefix $(OBSDIR)/dust_off/, $(OBS))

Folders      := $(OBSDIR) $(DUST) $(DUSTonOBS) $(DUSToffOBS)

# target : normal-prerequisites | order-only-prerequisites
# 	recipe...

all:   | $(Folders)
	@echo Hola Mundo
	@echo $(Folders)

$(Folders):
	mkdir $(Folders)

#$(OBSDIR):
#	mkdir $(OBSDIR)

#$(DUST): |$(OBSDIR)
	mkdir $(DUST)

#$(DUSTonOBS):  | $(DUST)
#	mkdir $(DUSTonOBS)

#$(DUSToffOBS): | $(DUST)
#	mkdir $(DUSToffOBS)

.PHONY : clean
clean:
	rm -r mcmc_steps

